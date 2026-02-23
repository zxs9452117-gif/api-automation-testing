# RESTful API Automation Testing Framework

本專案是一個基於 **Python + Pytest** 構建的 API 自動化測試框架。採用 **API Object Model (AOM)** 設計模式，旨在提供高可維護性、可擴展性且易於偵錯的測試解決方案。

## 🚀 技術棧
| 分類 | 工具/技術 |
| :--- | :--- |
| **程式語言** | Python 3.10+ |
| **測試框架** | Pytest |
| **網路請求** | Requests (Session-based) |
| **設計模式** | API Object Model (POM 變體), Data-Driven Testing (DDT) |
| **配置管理** | ConfigParser (ini) |
| **CI/CD** | GitHub Actions |

---

## 🛠️ 專案架構
```text
api-automation-testing/
├── apis/                # API 業務邏輯封裝 (API Object Model)
│   ├── base_api.py      # 底層請求封裝、全域 Log、Headers 處理
│   ├── user_api.py      # 用戶模組 API
│   └── product_api.py   # 產品(Posts)模組 API
├── data/                # 測試資料管理 (Data-Driven)
│   └── user_data.json
├── tests/               # 測試腳本
│   ├── conftest.py      # Pytest Fixtures (依賴注入)
│   ├── test_users.py
│   └── test_products.py # 包含完整的 CRUD 測試
├── utils/               # 通用工具類
│   ├── config_reader.py # 環境變數與配置讀取
│   └── data_loader.py   # JSON 資料載入器
├── .github/workflows/   # CI/CD 流水線設定
├── config.ini           # 多環境配置 (Base URL, Timeout)
├── requirements.txt     # 相依套件清單
└── README.md
```

---

## ✨ 核心亮點

### 1. 完善的底層封裝 (Base API)
* **自動日誌**：統一攔截 Request 與 Response，自動輸出格式化 JSON 與視覺化分隔線，極大降低 Debug 成本。
* **防禦性設計**：全域 `timeout` 設置避免 CI/CD 卡死；動態 `User-Agent` 偽裝應對基礎 WAF 防護。
* **Session 管理**：利用 `requests.Session()` 維持連線狀態，提升執行效率。

### 2. 環境與資料分離 (DDT)
* **環境切換**：透過 `config.ini` 管理 `Base URL`，無需修改程式碼即可切換 Dev/Staging 環境。
* **資料驅動**：測試案例與測試資料 (JSON) 完全解耦，支援多組邊界案例快速測試。

### 3. CI/CD 自動化執行
* 整合 **GitHub Actions**，在每次代碼 Push 或 Pull Request 時自動執行測試，並將測試結果上傳為 Artifact。

---

## 💡 實戰心得：遇到的挑戰與解決方案
在開發過程中，我經歷了從「技術攻堅」到「架構優先」的思維轉變：
* **靈活應對 403 Forbidden**：原計畫使用 Reqres.in 作為測試靶場，但因其 Cloudflare 防護等級提升導致 403 錯誤。在嘗試 Header 偽裝後，評估繼續攻克 WAF 的邊際效益較低，因此**果斷將專案切換至更具測試友善性的 JSONPlaceholder**。此舉不僅解決了阻塞，更驗證了本框架「低耦合、易遷移」的架構優勢——僅需修改 `config.ini` 即可完成全專案的靶場轉移。
* **Fake API 非持久化處理**：針對 JSONPlaceholder 不儲存 POST 資料的特性，在整合測試流中採用「模擬驗證 + 既有資源操作」的策略，成功規避了伺服器端的 500 錯誤。
* **配置讀取魯棒性**：處理了 `configparser` 讀取數值時的型別轉換，確保 `timeout` 參數符合 `requests` 規範。

---

## 快速開始

1. **複製專案**
   ```bash
   git clone https://github.com/zxs9452117-gif/api-automation-testing.git
   cd api-automation-testing
   ```

2. **安裝依賴**
   ```bash
   pip install -r requirements.txt
   ```

3. **執行測試**
   ```bash
   # 執行所有測試並顯示詳細日誌
   pytest -v -s
   ```