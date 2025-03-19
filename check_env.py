import sys
import os
import subprocess
import google.generativeai as genai

def check_environment():
    # 检查 Python 版本
    print(f"Python 版本: {sys.version}")
    
    # 检查已安装的包
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "list"], 
            capture_output=True, 
            text=True
        )
        packages = result.stdout
        
        # 检查关键包
        for package in ["google-generativeai", "requests", "beautifulsoup4", "python-dotenv"]:
            if package in packages:
                print(f"✅ {package} 已安装")
            else:
                print(f"❌ {package} 未安装")
        
        # 检查 google-generativeai 版本
        for line in packages.split("\n"):
            if "google-generativeai" in line:
                print(f"Google Generative AI 版本信息: {line.strip()}")
    except Exception as e:
        print(f"检查包时出错: {e}")
    
    # 检查环境变量
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        print("✅ GEMINI_API_KEY 环境变量已设置")
        # 显示密钥的前几个字符
        print(f"API 密钥前缀: {api_key[:5]}...")
    else:
        print("❌ GEMINI_API_KEY 环境变量未设置")
    
    # 检查 .env 文件
    if os.path.exists(".env"):
        print("✅ .env 文件存在")
        with open(".env", "r") as f:
            content = f.read()
            if "GEMINI_API_KEY" in content:
                print("✅ .env 文件包含 GEMINI_API_KEY")
            else:
                print("❌ .env 文件不包含 GEMINI_API_KEY")
    else:
        print("❌ .env 文件不存在")

    genai.configure(api_key=api_key)
     # 获取并打印所有可用模型
    # print("\n可用的 Gemini 模型列表：")
    # print("-" * 50)
    # for model in genai.list_models():
    #     print(f"模型名称: {model.name}")
    #     print(f"显示名称: {model.display_name}")
    #     print(f"描述: {model.description}")
    #     print(f"支持的生成内容类型: {model.supported_generation_methods}")
    #     print("-" * 50)
    model = genai.GenerativeModel('gemini-2.0-pro-exp-02-05')
    response = model.generate_content("Hello")
    print(response.text)
    

if __name__ == "__main__":
    check_environment()