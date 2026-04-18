# 台灣即時天氣數據分析器 🌦️

這是一個結合資料爬蟲與數據視覺化的 Python Side Project。透過中央氣象署 API 獲取全台各測站的即時觀測資料，並利用 Pandas 與 Matplotlib 進行數據整理與繪圖。

## 🚀 功能特點
- **即時數據：** 直接連接 CWA 開放資料平台 API。
- **自動化處理：** 自動解析 JSON 格式數據並轉換為 DataFrame 表格。
- **數據視覺化：** 生成直觀的氣溫對比長條圖。

## 🛠️ 環境配置與安裝
本專案使用 Python 虛擬環境開發，請依照以下步驟設定：

1. **建立並啟動虛擬環境：**
   ```bash
   python -m venv .venv
   .\venv\Scripts\activate
2. **安裝必要函式庫：**
   ```bash
   pip install requests pandas matplotlib
