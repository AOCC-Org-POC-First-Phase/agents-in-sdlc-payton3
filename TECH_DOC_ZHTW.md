# Tailspin Toys 技術文件

## 專案簡介

Tailspin Toys 是一個專為以開發者為主題的桌上遊戲打造的眾籌平台。本專案作為一個完整的 Web 應用程式示範，展示了如何使用現代化的技術堆疊來構建全端應用程式，同時也作為探索 GitHub Copilot 代理功能的實驗環境。

### 技術架構

本專案採用前後端分離架構：

- **後端**: 使用 [Flask](https://flask.palletsprojects.com/en/stable/) 框架搭配 [SQLAlchemy](https://www.sqlalchemy.org/) ORM 進行資料庫互動
- **前端**: 使用 [Astro](https://astro.build/) 作為靜態網站生成器，搭配 [Svelte](https://svelte.dev/) 處理動態頁面和互動元件
- **樣式**: 採用 [Tailwind CSS](https://tailwindcss.com/) 進行樣式設計，並維護一致的暗色主題

### 專案目標

本專案不僅是一個功能完整的眾籌平台，更是一個教學工具，用於展示：

- GitHub Copilot 在軟體開發生命週期 (SDLC) 中的應用
- 與 GitHub 議題和拉取請求的整合
- 模型上下文協定 (MCP) 的使用
- 自定義指令和提示檔案的實作
- 代理模式下的開發工作流程

## 主要功能

### 核心功能

1. **遊戲專案展示**
   - 瀏覽所有可用的遊戲眾籌專案
   - 檢視遊戲詳細資訊，包括描述、目標金額、已籌集金額等
   - 支援多種遊戲類別和發佈商

2. **專案分類**
   - 按遊戲類別進行篩選
   - 按發佈商進行篩選
   - 快速搜尋和導覽功能

3. **資料管理**
   - SQLAlchemy ORM 資料模型
   - RESTful API 端點設計
   - 資料驗證和錯誤處理

### 技術特色

1. **現代化前端體驗**
   - 使用 Astro 的島嶼架構 (Islands Architecture) 實現最佳效能
   - Svelte 元件提供流暢的互動體驗
   - Tailwind CSS 實現響應式設計

2. **強固的後端架構**
   - Flask 藍圖 (Blueprints) 組織路由結構
   - SQLAlchemy ORM 進行資料庫抽象化
   - Python 類型提示 (Type Hints) 提升程式碼品質

3. **開發工具整合**
   - 完整的測試套件
   - 自動化部署腳本
   - GitHub Actions CI/CD 工作流程

## 安裝指南

### 系統需求

在開始之前，請確保您的系統已安裝以下工具：

- **Python 3.8+**: 用於執行 Flask 後端
- **Node.js 18+**: 用於執行 Astro/Svelte 前端
- **npm**: Node.js 套件管理器
- **Git**: 版本控制系統

### 快速安裝

本專案提供自動化安裝腳本，可一次性完成所有依賴項的安裝：

```bash
# 執行安裝腳本
./scripts/setup-env.sh
```

安裝腳本會自動執行以下操作：

1. 建立 Python 虛擬環境（位於 `venv/` 目錄）
2. 啟用虛擬環境
3. 安裝所有 Python 依賴項（來自 `server/requirements.txt`）
4. 安裝所有 Node.js 依賴項（使用 `npm ci`）
5. 安裝 Playwright 瀏覽器和相關依賴
6. 安裝 `uv` 工具（來自 astral.sh）

### 手動安裝步驟

如果您偏好手動安裝，請依照以下步驟進行：

#### 1. 複製專案儲存庫

```bash
git clone https://github.com/AOCC-Org-POC-First-Phase/agents-in-sdlc-payton3.git
cd agents-in-sdlc-payton3
```

#### 2. 設定 Python 環境

```bash
# 建立虛擬環境
python3 -m venv venv

# 啟用虛擬環境 (Linux/macOS)
source venv/bin/activate

# 啟用虛擬環境 (Windows)
venv\Scripts\activate

# 安裝 Python 依賴項
pip install -r server/requirements.txt
```

#### 3. 設定前端環境

```bash
# 切換到 client 目錄
cd client

# 安裝 Node.js 依賴項
npm ci

# 安裝 Playwright（用於端對端測試）
npx playwright install
npx playwright install-deps

# 返回專案根目錄
cd ..
```

### 驗證安裝

安裝完成後，您可以執行測試來驗證環境是否正確設定：

```bash
# 執行後端測試
./scripts/run-server-tests.sh
```

如果所有測試通過，表示您的開發環境已正確設定！

## 使用指南

### 啟動應用程式

#### 使用啟動腳本（推薦）

最簡單的方法是使用提供的啟動腳本：

```bash
./scripts/start-app.sh
```

這個腳本會：
1. 確保所有依賴項已安裝
2. 啟動 Flask 後端伺服器（預設於 `http://localhost:5000`）
3. 啟動 Astro 前端開發伺服器（預設於 `http://localhost:4321`）

啟動完成後，開啟瀏覽器並訪問 [http://localhost:4321](http://localhost:4321) 即可查看應用程式！

#### 手動啟動

您也可以分別啟動前端和後端：

**啟動後端伺服器：**

```bash
# 確保虛擬環境已啟用
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate  # Windows

# 切換到 server 目錄
cd server

# 啟動 Flask 應用程式
python app.py

# 或使用 Flask CLI
flask run
```

**啟動前端開發伺服器：**

在另一個終端視窗中：

```bash
# 切換到 client 目錄
cd client

# 啟動 Astro 開發伺服器
npm run dev
```

### 開發工作流程

#### 執行測試

**後端測試：**

```bash
# 使用測試腳本
./scripts/run-server-tests.sh

# 或手動執行
cd server
python -m unittest discover -s tests -p "*.py"
```

**前端測試與建置：**

```bash
cd client

# 執行建置
npm run build

# 執行端對端測試
npm run test
```

#### 程式碼品質檢查

在提交程式碼之前，請確保：

1. **執行所有測試**: 確保後端和前端測試都通過
2. **驗證建置**: 確保前端可以成功建置
3. **遵循程式碼標準**: 
   - Python 程式碼必須包含類型提示
   - 遵循專案的程式碼格式要求
   - 確保 API 變更有對應的測試

#### 資料庫管理

資料庫檔案位於 `data/` 目錄。應用程式使用 SQLite 作為資料庫，適合開發和示範用途。

### 專案結構說明

```
agents-in-sdlc-payton3/
├── server/                 # Flask 後端
│   ├── models/            # SQLAlchemy ORM 模型
│   ├── routes/            # API 端點（按資源組織）
│   ├── tests/             # API 單元測試
│   ├── utils/             # 工具函式和輔助程式
│   ├── app.py             # Flask 應用程式進入點
│   └── requirements.txt   # Python 依賴項
├── client/                # Astro/Svelte 前端
│   ├── src/
│   │   ├── components/    # 可重用的 Svelte 元件
│   │   ├── layouts/       # Astro 版面範本
│   │   ├── pages/         # Astro 頁面路由
│   │   └── styles/        # CSS 和 Tailwind 配置
│   ├── package.json       # Node.js 依賴項
│   └── Dockerfile         # 前端容器化配置
├── scripts/               # 開發和部署腳本
│   ├── setup-env.sh       # 環境設定腳本
│   ├── run-server-tests.sh # 後端測試腳本
│   └── start-app.sh       # 應用程式啟動腳本
├── docs/                  # 專案文件
│   ├── README.md          # 英文版文件
│   ├── README.zh-TW.md    # 繁體中文版文件
│   └── ...                # 其他教學文件
├── data/                  # 資料庫檔案
├── .github/               # GitHub 配置
│   ├── copilot-instructions.md  # Copilot 指令
│   └── instructions/      # 任務特定指令檔案
├── README.md              # 專案主要說明文件
├── CONTRIBUTING.md        # 貢獻指南
└── TECH_DOC_ZHTW.md      # 技術文件（本檔案）
```

### 常見任務

#### 新增 API 端點

1. 在 `server/routes/` 中建立或修改路由檔案
2. 使用 Flask 藍圖組織端點
3. 在 `server/app.py` 中註冊藍圖
4. 在 `server/tests/` 中建立對應的測試

#### 建立新的 UI 元件

1. 在 `client/src/components/` 中建立 Svelte 元件
2. 遵循 Svelte 的響應式程式設計模型
3. 使用 Tailwind CSS 類別進行樣式設計
4. 在 Astro 頁面中引用元件

#### 新增資料模型

1. 在 `server/models/` 中建立 SQLAlchemy 模型
2. 確保包含適當的關聯和約束
3. 如需要，建立資料庫遷移
4. 更新相關的 API 端點和測試

## 貢獻指南

我們非常歡迎社群貢獻！在參與之前，請先閱讀我們的貢獻指南和行為準則。

### 開始貢獻

1. **閱讀文件**: 
   - [CONTRIBUTING.md](./CONTRIBUTING.md) - 詳細的貢獻指南
   - [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) - 社群行為準則

2. **設定開發環境**: 
   - 按照本文件的「安裝指南」章節設定環境
   - 確保所有測試都能成功執行

3. **選擇任務**: 
   - 瀏覽 [Issues](https://github.com/AOCC-Org-POC-First-Phase/agents-in-sdlc-payton3/issues) 尋找適合的任務
   - 對於初次貢獻，可以尋找標記為 `good first issue` 的議題

### 提交變更

#### 提交拉取請求 (Pull Request)

1. **Fork 並複製專案儲存庫**:
   ```bash
   # Fork 專案後複製您的分支
   git clone https://github.com/YOUR_USERNAME/agents-in-sdlc-payton3.git
   cd agents-in-sdlc-payton3
   ```

2. **建立新分支**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **進行變更**:
   - 撰寫清晰、有意義的程式碼
   - 遵循專案的程式碼標準
   - 為新功能添加測試

4. **執行測試**:
   ```bash
   # 執行後端測試
   ./scripts/run-server-tests.sh
   
   # 執行前端建置和測試
   cd client
   npm run build
   npm run test
   ```

5. **提交變更**:
   ```bash
   git add .
   git commit -m "feat: 簡短描述您的變更"
   ```
   
   撰寫[良好的提交訊息](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)的提示：
   - 使用現在式（"新增功能" 而非 "新增了功能"）
   - 第一行限制在 50 字元以內
   - 如需要，在第二行之後提供詳細說明

6. **推送並建立 Pull Request**:
   ```bash
   git push origin feature/your-feature-name
   ```
   
   然後在 GitHub 上建立 Pull Request。

### 程式碼標準

#### 提交前檢查清單

在提交每個變更之前，請確保：

- ✅ 執行 Python 測試以確保後端功能正常
- ✅ 對於前端變更，執行建置以驗證成功
- ✅ 對於前端變更，執行端對端測試以確保一切正常
- ✅ 更新 API 變更時，更新並執行對應的測試
- ✅ 更新模型時，如需要請包含資料庫遷移
- ✅ 新增新功能時，更新 README
- ✅ 更新 Copilot Instructions 檔案（如有相關變更）

#### 程式碼格式要求

**Python 程式碼**:
- 必須使用類型提示來標註回傳值和函式參數
- 使用 SQLAlchemy 模型進行資料庫互動
- 使用 Flask 藍圖組織路由
- 遵循 RESTful API 設計原則

**前端程式碼**:
- 使用 Svelte 建立互動式元件
- 遵循 Svelte 的響應式程式設計模型
- 當功能在多處使用時，建立可重用的元件
- 使用 Astro 處理頁面路由和靜態內容

**樣式**:
- 使用 Tailwind CSS 類別進行樣式設計
- 在整個應用程式中維護暗色主題
- UI 元素使用圓角設計
- 遵循現代化 UI/UX 原則，確保介面清晰、易於訪問

#### GitHub Actions 工作流程

如果您需要修改 GitHub Actions 工作流程：

- 遵循良好的安全實踐
- 確保明確設定工作流程權限
- 添加註解以記錄正在執行的任務

### 使用指令檔案

本專案廣泛使用自定義指令檔案來指導 GitHub Copilot：

- **.github/copilot-instructions.md**: 專案級別的全域指令
- **.github/instructions/*.instructions.md**: 任務特定的指令檔案

當使用 Copilot 開發時，這些指令檔案會提供上下文和指導，確保生成的程式碼符合專案標準。

### 取得協助

如果您有任何問題或需要協助：

1. 查看現有的[文件](./docs/README.zh-TW.md)
2. 在 [Issues](https://github.com/AOCC-Org-POC-First-Phase/agents-in-sdlc-payton3/issues) 中搜尋類似問題
3. 如果找不到答案，請開啟新的 Issue

### 資源連結

- [如何為開源專案貢獻](https://opensource.guide/how-to-contribute/)
- [使用拉取請求](https://help.github.com/articles/about-pull-requests/)
- [GitHub 說明](https://help.github.com)
- [專案授權條款](./LICENSE)
- [安全政策](./SECURITY.md)
- [支援資訊](./SUPPORT.md)

---

## 授權

本專案依照 MIT 開源授權條款授權。詳細資訊請參閱 [LICENSE](./LICENSE) 檔案。

## 維護者

您可以在 [CODEOWNERS](./.github/CODEOWNERS) 中找到維護者清單。

## 支援

本專案按原樣提供，並會隨時間更新。如果您有任何問題，請開啟 Issue。

---

**最後更新**: 2024年10月

**版本**: 1.0.0

**相關文件**:
- [專案主頁 (README.md)](./README.md)
- [實驗指南 (docs/README.zh-TW.md)](./docs/README.zh-TW.md)
- [貢獻指南 (CONTRIBUTING.md)](./CONTRIBUTING.md)
- [行為準則 (CODE_OF_CONDUCT.md)](./CODE_OF_CONDUCT.md)
