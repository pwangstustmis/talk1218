import google.generativeai as genai
from google.colab import drive
import json
drive.mount('/content/drive')

genai.configure(api_key="API金鑰")
#model = genai.GenerativeModel("gemini-1.5-flash")
pdf_file = genai.upload_file("dp2a-11-網路記帳與支出管家.pdf")
lecture_prompt = "根據上載文件產生2頁類似內容文章"
model = genai.GenerativeModel("gemini-1.5-flash-001",
    system_instruction=[lecture_prompt]
)
generation_config={
    "temperature":0.7,
    "response_mime_type": "application/json",
}
response = model.generate_content(
    [pdf_file],
    generation_config=generation_config,
    stream=False
)
print(response.text)