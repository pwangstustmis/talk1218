import google.generativeai as genai
from google.colab import drive
import json
drive.mount("/content/drive")

genai.configure(api_key="API金鑰")
#model = genai.GenerativeModel("gemini-1.5-flash")
pdf_file = genai.upload_file("dp2a-11-網路記帳與支出管家.pdf")
lecture_prompt = """
* 根據上載文件產生10張投影片內容
* 每張投影片包含下列訊息:
  - 標題: 一行文字總結每張投影片內容
  - 內容: 包含3到5簡短敘述
  - 講稿: 對每個簡短敘述提供5到10行敘述
"""
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
slides=json.loads(response.text)
print(response.text)
for slide in slides['slides']:
  print(slide['title'])
  print(slide['content'])
  print(slide['script'])