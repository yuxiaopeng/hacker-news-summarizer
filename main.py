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

# 创建 Gemini 模型
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
            
        time.sleep(1)  # 避免请求过于频繁
    
    return stories[:limit]

def extract_article_content(url):
    """提取文章内容"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 移除脚本和样式元素
        for script in soup(["script", "style"]):
            script.extract()
        
        # 获取文本
        text = soup.get_text()
        
        # 清理文本
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        # 限制文本长度，避免超出 API 限制
        return text[:15000]
    except Exception as e:
        print(f"提取文章内容时出错: {e}")
        return ""

def generate_summary(title, content):
    """使用 Gemini 生成文章摘要"""
    if not content:
        return "无法获取文章内容"
    
    try:
        prompt = f"""
        文章标题: {title}
        
        文章内容:
        {content}
        
        请提供这篇文章的简洁摘要（不超过 300 字），捕捉文章的主要观点和关键信息。
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"生成摘要时出错: {e}")
        return "生成摘要时出错"

def translate_to_chinese(text):
    """使用 Gemini 将文本翻译成中文"""
    try:
        prompt = f"""
        请将以下文本翻译成中文，保持原文的意思和风格:
        
        {text}
        """
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"翻译时出错: {e}")
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
            date_str = file[11:-3]  # 从文件名提取日期
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
    stories = fetch_top_stories(limit=10)
    print(f"成功获取 {len(stories)} 篇文章")
    
    stories_with_summaries = []
    
    for i, story in enumerate(stories, 1):
        print(f"\n正在处理第 {i}/{len(stories)} 篇文章: {story['title']}")
        
        # 提取文章内容
        content = extract_article_content(story['url'])
        
        # 生成摘要
        summary = generate_summary(story['title'], content)
        
        # 翻译标题和摘要
        chinese_title = translate_to_chinese(story['title'])
        chinese_summary = translate_to_chinese(summary)
        
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


# def deploy_to_github_pages():
#     """部署到 GitHub Pages 的说明"""
#     instructions = """
# 要将生成的文件部署到 GitHub Pages，请按照以下步骤操作：

# 1. 创建一个新的 GitHub 仓库
# 2. 将 output 目录中的文件推送到该仓库
# 3. 在仓库设置中启用 GitHub Pages，选择 main 分支作为源

# 以下是命令示例：

# ```bash
# cd output
# git init
# git add .
# git commit -m "Initial commit"
# git remote add origin https://github.com/你的用户名/你的仓库名.git
# git push -u origin main


if __name__ == "__main__":
    main()