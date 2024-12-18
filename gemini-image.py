import google.generativeai as genai
from google.colab import drive
import json
drive.mount('/content/drive')

genai.configure(api_key="API金鑰")
myfile = genai.upload_file("flowers.png")
print(f"{myfile=}")

model = genai.GenerativeModel("gemini-1.5-flash")
result = model.generate_content(
    [myfile, "\n\n", "請問圖片中是甚麼花?"]
)
print(f"{result.text=}")