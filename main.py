import os
import re
import time
import requests
import google.generativeai as genai
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from datetime import datetime,timezone
import markdown
import json
import inspect
import sys

# 加载环境变量
load_dotenv()

# 配置 Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# 创建 Gemini 模型 gemini-2.0-flash-lite/gemini-2.0-flash/gemini-2.0-pro-exp
model = genai.GenerativeModel('gemini-2.0-flash')

def fetch_top_stories(limit=100):
    """获取 Hacker News 上的热门文章链接"""
    print(f"正在获取 Hacker News 上的前 {limit} 篇热门文章...")
    
    hn_url = "https://news.ycombinator.com/news?p="
    stories = []
    page = 1
    
    while len(stories) < limit:
        response = requests.get(f"{hn_url}{page}")
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 获取文章标题和链接
        items = soup.select('tr.athing')
        for item in items:
            if len(stories) >= limit:
                break
                
            title_element = item.select_one('span.titleline > a')
            if not title_element:
                continue
                
            title = title_element.text
            url = title_element.get('href')
            
            # 跳过 Hacker News 内部链接
            if url.startswith('item?id='):
                continue
                
            # 确保 URL 是完整的
            if not url.startswith(('http://', 'https://')):
                continue
                
            stories.append({
                'id': item['id'],
                'title': title,
                'url': url
            })
        
        page += 1
        if page > 4:  # 通常前 4 页就能获取 100 篇文章
            break
            
        time.sleep(2)  # 避免请求过于频繁
    
    return stories[:limit]

def extract_article_content(url):
    """提取文章内容"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0'
        }
        
        # 增加超时时间
        response = requests.get(url, headers=headers, timeout=15)
        
        # 检查响应状态
        if response.status_code != 200:
            print(f"获取文章失败，状态码: {response.status_code}")
            return ""
            
        # 尝试检测编码
        if response.encoding == 'ISO-8859-1':
            response.encoding = response.apparent_encoding
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 移除脚本、样式和其他不需要的元素
        for element in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
            element.extract()
        
        # 尝试找到主要内容区域
        main_content = None
        for tag in ['article', 'main', '.content', '#content', '.post', '.article', '.entry']:
            if tag.startswith('.') or tag.startswith('#'):
                main_content = soup.select_one(tag)
            else:
                main_content = soup.find(tag)
                
            if main_content:
                break
                
        # 如果找到主要内容区域，则使用它，否则使用整个页面
        if main_content:
            text = main_content.get_text()
        else:
            text = soup.get_text()
        
        # 清理文本
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        # 限制文本长度，避免超出 API 限制
        return text[:15000]
    except Exception as e:
        print(f"提取文章内容时出错: {e}")
        print(f"错误类型: {type(e).__name__}")
        import traceback
        print(f"错误详情: {traceback.format_exc()}")
        return ""

def generate_summary(title, content):
    """使用 Gemini 生成文章摘要"""
    if not content:
        return "无法获取文章内容"
    
    try:
        prompt = f"""
        Title: {title}
        
        Content:
        {content}
        
        Provide a concise summary of this article (no more than 300 words), capturing the main points and key information.
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"生成摘要时出错: {e}")
        return "生成摘要时出错"

def generate_summary_from_url(title, url, max_retries=3):
    """使用 Gemini 直接从 URL 生成文章摘要"""
    retries = 0
    while retries < max_retries:
        try:
            prompt = f"""
            Please read and summarize the following article:
            Title: {title}
            URL: {url}
            
            Provide a concise summary (no more than 300 words), capturing the main points and key information.
            If you cannot access the article, please respond with "Unable to access the article link."
            """
            
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            retries += 1
            if "RATE_LIMIT_EXCEEDED" in str(e):
                wait_time = 10 * retries  # 递增等待时间
                print(f"达到速率限制，等待 {wait_time} 秒后重试 ({retries}/{max_retries})...")
                time.sleep(wait_time)
                continue
            print(f"生成摘要时出错: {e}")
            print(f"错误类型: {type(e).__name__}")
            print(f"错误详情: {str(e)}")
            return "生成摘要时出错"
    return "达到最大重试次数，生成摘要失败"

def translate_to_chinese(text):
    """使用 Gemini 将文本翻译成中文"""
    try:
        prompt = f"""
        Translate the following Original text into Chinese:
        
        Requirements:
        1. Provide only one accurate Chinese translation
        2. Output the translation directly without explanations or multiple options
        3. Maintain the meaning and style of the original text
        4. If it's a title, keep it concise and clear
        
        Original text:
        {text}
        """
        
        response = model.generate_content(prompt)
        translated_text = response.text
        
        # 去除可能的前缀说明
        prefixes_to_remove = [
            "以下是将原文翻译成中文的版本，保持了原文的意思和风格：\n\n",
            "以下是将原文翻译成中文的版本，保持了原文的意思和风格：\n",
            "以下是将原文翻译成中文的版本，保持原文的意思和风格：\n\n",
            "以下是将原文翻译成中文的版本，保持原文的意思和风格：\n",
            "以下是翻译：\n\n",
            "以下是翻译：\n",
            "翻译如下：\n\n",
            "翻译如下：\n",
            "Here is the Chinese translation:\n\n",
            "Here is the Chinese translation:\n",
            "Chinese translation:\n\n",
            "Chinese translation:\n",
            "Translation:\n\n",
            "Translation:\n",
        ]
        
        for prefix in prefixes_to_remove:
            if translated_text.startswith(prefix):
                translated_text = translated_text[len(prefix):]
                break
        
        # 移除"要求："和相关内容的模式
        requirements_patterns = [
            r'要求：\s*\n*1\.\s*只提供一个准确的中文翻译\s*\n*2\.\s*直接输出翻译.*?(?=\n\n|\Z)',
            r'要求：\s*\n*[\d\.\s]*只提供.*?(?=\n\n|\Z)',
            r'要求：\s*\n*[\d\.\s]*直接输出.*?(?=\n\n|\Z)',
            r'要求：.*?(?=\n\n|\Z)',
            r'原文：\s*\n*',
            r'原文翻译：\s*\n*',
            r'翻译：\s*\n*'
        ]
        
        for pattern in requirements_patterns:
            translated_text = re.sub(pattern, '', translated_text, flags=re.DOTALL)
        
        # 清理多余的空行
        translated_text = re.sub(r'\n{3,}', '\n\n', translated_text)
        
        return translated_text.strip()
    except Exception as e:
        print(f"翻译时出错: {e}")
        print(f"错误类型: {type(e).__name__}")
        print(f"错误详情: {str(e)}")
        return text

def create_markdown_file(stories_with_summaries):
    """创建 Markdown 文件"""
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    
    md_content = f"""# Hacker News 热门文章摘要 ({today})

这是今日 [Hacker News](https://news.ycombinator.com/) 上最热门的文章摘要。

"""
    
    for i, story in enumerate(stories_with_summaries, 1):
        md_content += f"## {i}. {story['chinese_title']}\n\n"
        md_content += f"**原文标题**: {story['title']}\n\n"
        md_content += f"**原文链接**: [{story['url']}]({story['url']})\n\n"
        md_content += f"{story['chinese_summary']}\n\n"
        md_content += "---\n\n"
    
    # 创建输出目录
    os.makedirs('output', exist_ok=True)
    
    # 保存 Markdown 文件
    file_path = f"output/hacker_news_summary_{today}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    # 创建 index.md 文件作为 GitHub Pages 的主页
#     index_content = f"""# Hacker News 每日摘要

# ## 最新摘要 ({today})

# [查看今日摘要](hacker_news_summary_{today}.md)

# """
    
#     with open('output/index.md', 'w', encoding='utf-8') as f:
#         f.write(index_content)
    
#     print(f"Markdown 文件已保存到 {file_path}")
    return file_path


def write_head_contents(stories_with_summaries):
    """写入 README.md 文件的头部信息和当日 Top 10 摘要"""
    write_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    
    # 头部内容
    head_contents = inspect.cleandoc(f"""# Hacker News 每日摘要
    
这是 Top 10 的每日摘要，更多请点击 [Top 100](output/hacker_news_summary_{today}.md)

*最后自动更新时间: {write_time}*

""")
    
    # 添加当日 Top 10
    if stories_with_summaries:
        for i, story in enumerate(stories_with_summaries[:10], 1):
            head_contents += f"\n## {i}. {story['chinese_title']}\n\n"
            head_contents += f"**原文标题**: {story['title']}\n\n"
            head_contents += f"**原文链接**: [{story['url']}]({story['url']})\n\n"
            head_contents += f"{story['chinese_summary']}\n\n"
            head_contents += "---\n"
    
    # 添加历史记录
    head_contents += "\n## 历史记录\n\n"
    head_contents += "| 序号 | 文件 |\n"
    head_contents += "| --- | --- |\n"
    
    # 获取并排序历史文件
    history_files = []
    for file in os.listdir('output'):
        if file.startswith('hacker_news_summary_') and file.endswith('.md'):
            file_path = os.path.join('output', file)
            file_time = os.path.getmtime(file_path)
            date_str = file[20:-3]  # 从文件名提取日期
            history_files.append((file, date_str, file_time))
    
    # 按时间倒序排序
    history_files.sort(key=lambda x: x[2], reverse=True)
    
    # 添加历史记录表格
    for i, (file, date_str, _) in enumerate(history_files, 1):
        head_contents += f"| {i} | [{date_str}](output/{file}) |\n"
    
    # 写入文件
    write_text("README.md", 'w', head_contents)
    print("README.md 更新完成")

def main():
    print("开始运行 Hacker News 文章摘要提取器...")
    
    # 获取热门文章
    stories = fetch_top_stories(limit=100)
    print(f"成功获取 {len(stories)} 篇文章")
    
    stories_with_summaries = []
    
    for i, story in enumerate(stories, 1):
        print(f"\n正在处理第 {i}/{len(stories)} 篇文章: {story['title']}")
        
        # 提取文章内容
        content = extract_article_content(story['url'])
        
        # 生成摘要
        if content:
            print(f"成功提取文章内容，长度: {len(content)} 字符")
            summary = generate_summary(story['title'], content)
        else:
            print("无法提取文章内容，尝试直接生成摘要（可能会失败）")
            summary = generate_summary_from_url(story['title'], story['url'])
        
        time.sleep(3)  # 增加等待时间到 3 秒,RPM=15
        
        # 翻译标题和摘要
        chinese_title = translate_to_chinese(story['title'])
        time.sleep(3)  # 每次 API 调用之间添加等待
        chinese_summary = translate_to_chinese(summary)
        time.sleep(3)  # 每次 API 调用之间添加等待
        
        stories_with_summaries.append({
            **story,
            'summary': summary,
            'chinese_title': chinese_title,
            'chinese_summary': chinese_summary
        })
        
        # 保存进度
        with open('progress.json', 'w', encoding='utf-8') as f:
            json.dump(stories_with_summaries, f, ensure_ascii=False, indent=2)
        
        print(f"已完成第 {i} 篇文章的处理")
        time.sleep(2)
    
    # 创建 Markdown 文件
    md_file = create_markdown_file(stories_with_summaries)
    
    # 更新 README.md
    write_head_contents(stories_with_summaries)
    
    print("处理完成！")

def write_text(file_name, method, text):
    """
    write text to file
    method: 'a'-append, 'w'-overwrite
    """
    with open(file_name, method, encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    main()