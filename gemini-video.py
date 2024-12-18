import google.generativeai as genai
from google.colab import drive
import json
import time
drive.mount('/content/drive')

genai.configure(api_key="API金鑰")
myfile = genai.upload_file("JFK-speech.mp4")
while myfile.state.name == "PROCESSING":
    print('.', end='')
    time.sleep(10)
    myfile = genai.get_file(myfile.name)
print(f"{myfile=}")

model = genai.GenerativeModel("gemini-1.5-flash")
result = model.generate_content(
    [myfile, "\n\n", "請問影片談論內容是甚麼?"]
)
print(f"{result.text=}")