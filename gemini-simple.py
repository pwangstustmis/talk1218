import google.generativeai as genai

genai.configure(api_key='API金鑰')
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content("生成李白風格五言絕句")