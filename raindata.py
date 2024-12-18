import requests
import json
from datetime import datetime

# API 金鑰
API_KEY = ''  # 請將 'YOUR_API_KEY' 替換為你的 API 金鑰

# 設定 API URL 和參數
url = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001'
params = {
    'Authorization': API_KEY,
    'format': 'JSON',
    'locationName': '臺南市'  # 你可以將 '台北市' 改為其他城市名稱
}

# 發送請求並取得回應
response = requests.get(url, params=params)

# 檢查請求是否成功
if response.status_code == 200:
    data = response.json()

    # 顯示資料中的預測時間和降雨量
    locations = data['records']['location']
    for location in locations:
        print(f"地區: {location['locationName']}")
        
        # 取出預測時間和降雨量資料
        for weather_element in location['weatherElement']:
            if weather_element['elementName'] == 'PoP':  # PoP6h 代表 6 小時內的降雨機率
                print(f"預測時間: {weather_element['time']}")
                for time in weather_element['time']:
                    start_time = time['startTime']
                    end_time = time['endTime']
                    value = time['parameter']['parameterName']
                    print(f"  期間: {start_time} 至 {end_time}，降雨機率: {value}%")
else:
    print(f"API 請求失敗，狀態碼: {response.status_code}")
