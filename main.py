import requests
import pandas as pd
import matplotlib.pyplot as plt
import urllib3

# 1. 基礎設定
# 關閉 SSL 安全警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# 解決中文顯示問題 (Windows 專用)
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 2. 參數設定
api_key = "CWA-7BEF9C09-ED27-4C17-A691-03A7EA62A2F2"
url = f"https://opendata.cwa.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization={api_key}"

# 3. 主程式執行
try:
    print("正在抓取氣象署即時數據...")
    # verify=False 解決你剛才遇到的 SSL 憑證問題
    response = requests.get(url, verify=False)
    data = response.json()
    
    # 解析資料
    stations = data['records']['Station']
    
    # 建立兩個列表來存圖表數據
    names = []
    temps = []
    
    # 只取前 10 個觀測站，避免圖表太擁擠
    for s in stations[:10]:
        names.append(s['StationName'])
        # 轉換氣溫為數字 (float)
        temps.append(float(s['WeatherElement']['AirTemperature']))

    # 4. 繪製圖表
    print("正在產生分析圖表...")
    plt.figure(figsize=(10, 6))
    plt.bar(names, temps, color='skyblue')
    plt.title('台灣部分測站即時氣溫圖', fontsize=16)
    plt.xlabel('測站名稱', fontsize=12)
    plt.ylabel('攝氏溫度 (°C)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # 顯示圖表
    plt.show()

except Exception as e:
    print(f"程式執行過程中發生錯誤：{e}")
