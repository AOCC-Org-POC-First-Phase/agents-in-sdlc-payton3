# Tailspin Toys 完整專案說明文件（繁體中文）

> **本文件整合了整個 repository 的所有說明**  
> 最後更新：2024年10月  
> 版本：1.0.0

---

## 目錄

1. [專案簡介](#專案簡介)
2. [技術架構](#技術架構)
3. [主要功能](#主要功能)
4. [安裝指南](#安裝指南)
5. [使用指南](#使用指南)
6. [專案結構說明](#專案結構說明)
7. [實驗教學](#實驗教學)
   - [練習 0：先決條件](#練習-0先決條件)
   - [練習 1：GitHub Copilot 編碼代理](#練習-1github-copilot-編碼代理)
   - [練習 2：使用 MCP 伺服器](#練習-2使用-copilot-代理模式和-github-mcp-伺服器)
   - [練習 3：自定義指令檔案](#練習-3使用指令檔案為-copilot-提供上下文)
   - [練習 4：使用代理模式添加新功能](#練習-4使用-copilot-代理模式添加新功能)
   - [練習 5：審查編碼代理的工作](#練習-5審查-github-copilot-編碼代理的工作)
   - [練習 6：使用 Spec-kit](#練習-6使用-spec-kit-與-copilot-coding-agent)
   - [練習 7：後續工作與延伸整合](#練習-7後續工作與延伸整合)
8. [貢獻指南](#貢獻指南)
9. [行為準則](#行為準則)
10. [安全政策](#安全政策)
11. [支援資訊](#支援資訊)
12. [授權資訊](#授權資訊)

---

## 專案簡介

Tailspin Toys 是一個專為以開發者為主題的桌上遊戲打造的眾籌平台。本專案作為一個完整的 Web 應用程式示範，展示了如何使用現代化的技術堆疊來構建全端應用程式，同時也作為探索 GitHub Copilot 代理功能的實驗環境。

這個專案包含了一個 1 小時的指導式工作坊，用於探索 GitHub Copilot Agent Mode 和 Visual Studio Code 中的相關功能。專案是一個虛構遊戲眾籌公司的網站，具有使用 SQLAlchemy 的 Flask 後端和使用 Svelte 動態頁面的 Astro 前端。

### 專案目標

本專案不僅是一個功能完整的眾籌平台，更是一個教學工具，用於展示：

- GitHub Copilot 在軟體開發生命週期 (SDLC) 中的應用
- 與 GitHub 議題和拉取請求的整合
- 模型上下文協定 (MCP) 的使用
- 自定義指令和提示檔案的實作
- 代理模式下的開發工作流程

---

## 技術架構

本專案採用前後端分離架構：

### 後端技術

- **框架**: [Flask](https://flask.palletsprojects.com/en/stable/) - Python Web 框架
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) - Python SQL 工具包和 ORM
- **資料庫**: SQLite（適合開發和示範）
- **開發語言**: Python 3.8+

### 前端技術

- **框架**: [Astro](https://astro.build/) - 靜態網站生成器
- **UI 元件**: [Svelte](https://svelte.dev/) - 動態頁面和互動元件
- **樣式**: [Tailwind CSS](https://tailwindcss.com/) - CSS 框架
- **主題**: 一致的暗色主題設計

### 開發工具

- **版本控制**: Git
- **CI/CD**: GitHub Actions
- **測試**: Python unittest、Playwright（端對端測試）
- **開發環境**: GitHub Codespaces

---

## 主要功能

### 核心功能

#### 1. 遊戲專案展示
- 瀏覽所有可用的遊戲眾籌專案
- 檢視遊戲詳細資訊，包括描述、目標金額、已籌集金額等
- 支援多種遊戲類別和發佈商

#### 2. 專案分類
- 按遊戲類別進行篩選
- 按發佈商進行篩選
- 快速搜尋和導覽功能

#### 3. 資料管理
- SQLAlchemy ORM 資料模型
- RESTful API 端點設計
- 資料驗證和錯誤處理

### 技術特色

#### 1. 現代化前端體驗
- 使用 Astro 的島嶼架構 (Islands Architecture) 實現最佳效能
- Svelte 元件提供流暢的互動體驗
- Tailwind CSS 實現響應式設計

#### 2. 強固的後端架構
- Flask 藍圖 (Blueprints) 組織路由結構
- SQLAlchemy ORM 進行資料庫抽象化
- Python 類型提示 (Type Hints) 提升程式碼品質

#### 3. 開發工具整合
- 完整的測試套件
- 自動化部署腳本
- GitHub Actions CI/CD 工作流程

---

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

---

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

---

## 專案結構說明

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
└── TECH_DOC_ZHTW.md      # 技術文件
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

---

## 實驗教學

這些實驗將帶您了解 GitHub Copilot 代理功能的最常見工作流程。

> **重要提示**  
> 因為 GitHub Copilot 和生成式 AI 一般來說是機率性的而不是確定性的，確切的程式碼、變更的檔案等可能會有所不同。因此，您可能會注意到實驗中的螢幕截圖和程式碼片段與您的體驗之間存在細微差異。這是可以預期的，只是使用這類工具的本質。

### 實驗情境

實驗設想您是 Tailspin Toys 的新開發者，這是一家虛構的公司，為以 DevOps 為主題的桌上遊戲提供眾籌。您的任務是建立議題來記錄應用程式和 DevOps 流程所需的更新，然後實作按類別和發佈商過濾遊戲的功能。您將迭代工作，探索網站和 Copilot 的功能，來完成任務。

---

### 練習 0：先決條件

在開始實驗之前，您需要完成一些準備任務。

#### 設定實驗程式碼庫

為了建立程式碼庫的副本，您將從範本建立一個實例。

1. 在新的瀏覽器視窗中，導覽到這個實驗的 GitHub 程式碼庫
2. 透過選擇 **Use this template** 按鈕來建立您自己的程式碼庫副本，然後選擇 **Create a new repository**
3. 如果您是作為 GitHub 或 Microsoft 主導的活動的一部分完成研討會，請遵循導師提供的命名程式碼庫的說明
4. 記下您建立的程式碼庫路徑（組織或使用者名稱/程式碼庫名稱）

#### 建立 Codespace

GitHub Codespaces 是一個基於雲端的開發環境，允許您直接在瀏覽器中編寫、執行和偵錯程式碼。

1. 導覽到您新建立的程式碼庫
2. 選擇綠色的 **Code** 按鈕
3. 選擇 **Codespaces** 標籤，然後選擇 **+** 按鈕來建立新的 Codespace

Codespace 的建立需要幾分鐘時間。在等待期間，您可以繼續進行下一個練習！

---

### 練習 1：GitHub Copilot 編碼代理

GitHub Copilot 的編碼代理旨在執行諸如更新程式碼和添加功能等任務，都是以自主的方式進行。代理完成其工作後，它會生成一個草稿 PR，準備供人類開發者審查。

#### 學習目標

- 自定義生成程式碼的環境
- 確保操作安全執行
- 明確界定議題的重要性
- 將議題分配給 Copilot

#### 情境

Tailspin Toys 有一些技術債務需要解決：
- 所有函數都需要添加文件字串
- 需要為遊戲 API 建立 CRUD 端點

#### GitHub Copilot 編碼代理介紹

GitHub Copilot 編碼代理可以在後台執行任務，很像人類開發者的方式。這是透過將 GitHub 議題分配給 Copilot 來完成的。分配後，Copilot 將：
- 建立一個草稿拉取請求來追蹤其進度
- 設定環境
- 開始處理任務
- 完成後標記您進行審查

#### 明確界定指令的重要性

GitHub Copilot 並沒有魔法。我們需要對如何將任務分配給 Copilot 編碼代理保持謹慎。將 Copilot 作為 AI 配對程式設計師來工作通常是最佳方法：
- 分階段工作
- 學習和實驗
- 相應地調整

軟體開發的基本原則不會因為生成式 AI 的加入而改變。

#### 為 Copilot 編碼代理設定開發環境

編碼代理在執行工作時使用 GitHub Actions 作為其環境。您可以透過建立特殊的設定工作流程來自定義此環境，在 `.github/workflows/copilot-setup-steps.yml` 檔案中配置。

這個工作流程確保 Copilot 能夠存取 Python、Node.JS 以及客戶端和伺服器所需的相依性。

#### 改善程式碼文件

這是分配給 Copilot 編碼代理的完美任務：

1. 在瀏覽器中導覽到您的存儲庫
2. 選擇 **Issues** 標籤
3. 選擇 **New issue**
4. 選擇 **Blank issue**
5. 將標題設定為 `Code lacks documentation`
6. 將描述設定為：
   ```
   Our organization has a requirement that all functions have docstrings or the language equivalent. Unfortunately, recent updates haven't followed this standard. We need to update the existing code to ensure docstrings (or the equivalent) are included with every function or method.
   ```
7. 將議題分配給 `@copilot`
8. 選擇 **Submit new issue**

#### 建立 CRUD 端點

類似地，建立另一個議題來添加遊戲 API 的 CRUD 端點：

1. 建立新議題
2. 標題：`Add CRUD endpoints for games API`
3. 描述詳細說明需要的端點（建立、讀取、更新、刪除）
4. 分配給 `@copilot`

Copilot 將開始非同步處理這些任務！

---

### 練習 2：使用 Copilot 代理模式和 GitHub MCP 伺服器

編寫程式碼不只是編寫程式碼。需要提交議題、呼叫外部服務，並收集資訊。透過模型上下文協定 (MCP) 的力量，您可以直接從 Copilot 存取所有這些功能！

#### 學習目標

- 使用模型上下文協定 (MCP)
- 在您的存儲庫中設定 GitHub MCP 伺服器
- 使用 GitHub Copilot Chat 代理模式在您的存儲庫中建立議題

#### 什麼是代理模式和 MCP？

**代理模式**將 Copilot 轉變為一個可以代表您執行動作的 AI 代理。此模式允許您以更動態的方式與 Copilot 互動，使其能夠：
- 使用工具和執行任務
- 執行測試或終端命令
- 從編輯器讀取問題
- 使用這些見解來更新您的程式碼

**模型上下文協定 (MCP)** 為 AI 代理提供與外部工具和服務通訊的方式。透過使用 MCP：
- AI 代理可以即時與外部工具和服務通訊
- 能夠存取最新資訊（使用資源）
- 代表您執行動作（使用工具）

#### 流行的 MCP 伺服器

- **GitHub MCP 伺服器**：提供對 GitHub API 的存取
- **Playwright MCP 伺服器**：提供瀏覽器自動化功能
- **其他參考伺服器**：還有許多其他 MCP 伺服器可用

> **安全性提醒**  
> 將 MCP 伺服器視為專案中的任何其他相依性。在使用 MCP 伺服器之前，仔細審查其原始碼，驗證發佈者，並考慮安全隱患。

#### 確保您的 Codespace 準備就緒

1. 返回到您啟動 codespace 的標籤頁
2. 在左側工作台上選擇 **Extensions**
3. 在任何有 **Update** 按鈕的擴充功能上選擇 **Update**
4. 在任何有 **Reload Window** 按鈕的擴充功能上選擇 **Reload Window**

#### 使用 GitHub Copilot Chat 和代理模式

1. 返回您的 codespace
2. 選擇 **Copilot Chat** 圖示
3. 輸入測試訊息（如 "Hello world"）來啟動 Copilot Chat
4. 如果需要，按照指示進行驗證
5. 透過下拉選單切換到 **Agent** 模式
6. 將模型設定為 **Claude Sonnet 4**

#### 設定 GitHub MCP 伺服器

1. 打開 `.vscode/mcp.json` 檔案
2. 檢視 GitHub MCP 伺服器的配置
3. 該配置使 GitHub Copilot 能夠與 GitHub API 互動

#### 建立任務待辦事項

使用 Copilot 代理模式建立任務待辦事項：

1. 在 Copilot Chat 中輸入提示來建立議題
2. Copilot 將使用 GitHub MCP 伺服器來建立議題
3. 審查並批准 Copilot 的動作

---

### 練習 3：使用指令檔案為 Copilot 提供上下文

上下文在與生成式 AI 工作時至關重要。我們可以使用指令檔案提供指導，讓 Copilot 理解我們想要它做什麼以及我們希望如何完成。

#### 學習目標

- 使用自定義指令 `.github/copilot-instructions.md` 為 Copilot 提供專案特定的上下文
- 使用指令檔案指導 Copilot 進行重複性或範本化任務
- 實作存儲庫範圍的指令和任務特定的指令

#### 情境

Tailspin Toys 有一套開發實務的指南和要求：
- API 始終需要單元測試
- UI 應該是深色模式並具有現代感
- 文件應該以文件字串的形式添加到程式碼中
- 應該在每個檔案的開頭添加一段註釋

#### 自定義指令類型

有兩種類型的指令檔案：

1. **`.github/copilot-instructions.md`**
   - 針對每個聊天提示發送給 Copilot 的單一指令檔案
   - 應包含專案級別的資訊
   - 包括技術堆疊、專案概述、全局指導

2. **`*.instructions.md`**
   - 為特定任務或檔案類型建立
   - 提供特定語言的指南
   - 或為特定任務提供指南

#### 在更新自定義指令之前測試

1. 建立新分支 `add-filters`
2. 打開空檔案 `server/routes/publishers.py`
3. 使用 Copilot 生成端點程式碼
4. 注意生成的程式碼可能缺少文件字串或註釋標頭

#### 將全域標準添加到 copilot-instructions.md

1. 打開 `.github/copilot-instructions.md`
2. 探索現有的章節（程式碼標準、腳本、GitHub Actions）
3. 在程式碼格式要求章節添加：
   ```markdown
   - Every function should have docstrings or the language equivalent
   - Before imports or any code, add a comment block that explains the purpose of the file.
   ```
4. 重新生成程式碼並注意差異

#### 任務的指令檔案

指令檔案可以為特定任務提供更詳細的指導：
- 端點建立的指令
- 測試建立的指令
- UI 元件建立的指令

---

### 練習 4：使用 Copilot 代理模式添加新功能

Copilot 代理模式被設計為在您的 IDE 中更自主地行動。它以類似開發者的方式行為，探索專案結構，執行更新，運行測試等。

#### 學習目標

- GitHub Copilot 代理模式可以在後端和前端程式碼庫中實作新功能
- Copilot 代理模式可以探索您的專案並識別相關檔案
- 在合併之前審查生成的更改和測試

#### 情境

隨著遊戲清單的增長，您希望允許使用者按類別過濾。這將需要更新 API 和 UI，並更新 API 的測試。

#### 運行 Tailspin Toys 網站

1. 返回您的 codespace
2. 打開新的終端視窗
3. 運行啟動腳本：
   ```bash
   scripts/start-app.sh
   ```
4. 通過點擊 `http://localhost:4321` 打開網站
5. 探索網站的主要功能

#### 使用 Copilot 探索待辦事項

1. 打開 Copilot Chat
2. 建立新的聊天會話
3. 確保選擇了 **Agent** 模式
4. 詢問 Copilot 關於議題待辦事項：
   ```
   Please show me the backlog of items from my GitHub repository. Help me prioritize them based on those which will be most useful to the user.
   ```

#### 實作過濾功能

要實作過濾功能，需要：
- 向 API 添加新端點
- 為新端點建立測試
- 更新 UI 以引入功能

使用 Copilot 代理模式來協助完成這些任務：

1. 提供詳細的提示描述所需功能
2. Copilot 將探索專案並識別需要更新的檔案
3. 審查 Copilot 的建議
4. 執行測試以確保一切正常

#### 建立拉取請求

1. 審查所有更改
2. 使用 Git 提交更改
3. 推送到遠端存儲庫
4. 建立拉取請求
5. 等待審查

---

### 練習 5：審查 GitHub Copilot 編碼代理的工作

當我們第一次開始這個實驗時，我們分配了幾個議題給 GitHub Copilot 編碼代理。現在是時候探索它建議的程式碼變更了。

#### 安全性和 GitHub Copilot 編碼代理

因為 Copilot 編碼代理非同步執行其任務，已實施某些安全限制：
- Copilot 只對您的存儲庫具有讀取存取權限
- 只對它將用於其程式碼的分支具有寫入存取權限
- 編碼代理在 GitHub Actions 內運行
- 任何工作流程在運行之前都需要人工批准
- 預設情況下對外部資源的存取受到限制

#### 審查生成的文件

1. 返回 GitHub.com 上的您的存儲庫
2. 選擇 **Pull Requests**
3. 打開標題類似於 **Add missing documentation** 的 PR
4. 等待 Copilot 完成工作（如果仍在處理）
5. 選擇 **Files changed** 標籤審查更改
6. 探索新更新的程式碼
7. 導覽回 **Conversation** 標籤
8. 點擊 **Approve and run workflows**

#### 向 GitHub Copilot 請求更改

您可以在拉取請求中標記 Copilot 來請求更改：

1. 添加評論請求更改，標記 `@copilot`
2. 選擇 **View Session** 觀看 Copilot 執行其工作
3. 一旦完成，審查新的更改

#### 審查新端點

對於遊戲 API CRUD 端點的 PR 重複類似的審查過程。

---

### 練習 6：使用 Spec-kit 與 Copilot Coding Agent

本章說明如何使用 GitHub 的 Spec-kit（也稱為 `specify`）產生需求規格、工作清單，並搭配 Copilot Coding Agent 將產出轉為 GitHub Issues、Wiki 與專案項目。

#### 前置需求

- 已安裝 uvx
- 已設定好 GitHub 權杖
- 建議先在獨立分支上測試

#### 安裝 Spec-kit

1. 切到上層工作目錄
2. 使用 uvx 初始化 specify 專案：
   ```bash
   uvx --from git+https://github.com/github/spec-kit.git specify init my-spec-kit
   ```
3. 將產生的檔案同步回目前 repo

#### 產生 Spec（需求）

1. 使用 Spec-kit 產生需求草稿
2. 檢視 `.specify/` 內產生的 spec 檔案
3. 確認需求敘述、驗收準則與範例介面

#### 產生 Plan（開發計畫）

1. 根據 Spec 產生分階段的開發計畫
2. Plan 應包含 Milestones 和 Steps

#### 產生 Tasks（工作項目）

1. 將 Plan 轉為可執行的 Tasks
2. 確認每個 Task 的驗收標準明確

#### 將產物發佈到 Wiki

1. 使用 Copilot Coding Agent 將文件推送到 GitHub Wiki
2. 或手動移動到 `docs/` 目錄

#### 將 Tasks 轉為 Issues

Copilot Coding Agent 支援從 Tasks 檔生成 Issues，並可將其指派到 GitHub Project。

---

### 練習 7：後續工作與延伸整合

本章整理尚未涵蓋、但很適合在本專案延伸導入的實務主題。

#### 目標與範圍

- 串接 CI/CD（建置/測試/部署）並區分 Dev/Test/Prod
- 建立自動化安全防護（CodeQL、Dependabot）
- 發佈文件與站點（GitHub Pages）
- 視覺化追蹤與治理（Projects、Releases）

#### CI/CD 工作流程建議

##### 基礎設施即程式碼（IaC）
- 管理 Dev/Test/Prod 三套環境
- 使用 Environments + Secrets 管理敏感參數

##### 持續整合（CI）
- 觸發：push、pull_request
- 任務：安裝依賴、型別檢查、單元測試
- 快取：加速建置過程

##### 持續交付（CD）
- Dev：CI 通過後自動部署
- Test/Prod：需要人工批准
- 使用可回滾策略與版本標記

#### 安全性與品質

##### CodeQL（自動程式碼掃描）
- 排程或 PR 時掃描
- 產出 Alerts 與建議修正

##### Dependabot Updates
- 維護安全更新
- 設定自動化 PR

##### ESLint / 型別檢查
- 在 CI 中加入檢查
- 加上安全規則集

#### 文件與網站發佈（Pages）

- 使用 GitHub Pages 自動部署文件
- 建立索引頁面與導覽

#### 專案與釋出管理

##### Projects（看板/規劃）
- 使用 Milestone 與 Iteration 規劃
- 自動化規則（PR 合併後移動到 Done）

##### Releases（版本管理）
- 以 Tag + Release Note 紀錄變更
- 整合自動產生變更日誌

#### 建議的導入順序

1. 先完成 CI（建置/測試）
2. 加入 CodeQL 與 Dependabot
3. 導入 CD（分環境部署）
4. 啟用 Pages 發佈文件
5. 使用 Projects/Insights 追蹤進度

---

## 貢獻指南

我們非常歡迎社群貢獻！在參與之前，請先閱讀我們的貢獻指南和行為準則。

### 開始貢獻

#### 1. 閱讀文件
- [CONTRIBUTING.md](./CONTRIBUTING.md) - 詳細的貢獻指南
- [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) - 社群行為準則

#### 2. 設定開發環境
- 按照安裝指南章節設定環境
- 確保所有測試都能成功執行

#### 3. 選擇任務
- 瀏覽 Issues 尋找適合的任務
- 對於初次貢獻，尋找標記為 `good first issue` 的議題

### 提交拉取請求

#### 1. Fork 並複製專案儲存庫

```bash
git clone https://github.com/YOUR_USERNAME/agents-in-sdlc-payton3.git
cd agents-in-sdlc-payton3
```

#### 2. 建立新分支

```bash
git checkout -b feature/your-feature-name
```

#### 3. 進行變更

- 撰寫清晰、有意義的程式碼
- 遵循專案的程式碼標準
- 為新功能添加測試

#### 4. 執行測試

```bash
# 執行後端測試
./scripts/run-server-tests.sh

# 執行前端建置和測試
cd client
npm run build
npm run test
```

#### 5. 提交變更

```bash
git add .
git commit -m "feat: 簡短描述您的變更"
```

撰寫良好的提交訊息的提示：
- 使用現在式
- 第一行限制在 50 字元以內
- 如需要，在第二行之後提供詳細說明

#### 6. 推送並建立 Pull Request

```bash
git push origin feature/your-feature-name
```

然後在 GitHub 上建立 Pull Request。

### 程式碼標準

#### 提交前檢查清單

在提交每個變更之前，請確保：

- ✅ 執行 Python 測試以確保後端功能正常
- ✅ 對於前端變更，執行建置以驗證成功
- ✅ 對於前端變更，執行端對端測試
- ✅ 更新 API 變更時，更新並執行對應的測試
- ✅ 更新模型時，如需要請包含資料庫遷移
- ✅ 新增新功能時，更新 README
- ✅ 更新 Copilot Instructions 檔案（如有相關變更）

#### 程式碼格式要求

**Python 程式碼**：
- 必須使用類型提示來標註回傳值和函式參數
- 使用 SQLAlchemy 模型進行資料庫互動
- 使用 Flask 藍圖組織路由
- 遵循 RESTful API 設計原則

**前端程式碼**：
- 使用 Svelte 建立互動式元件
- 遵循 Svelte 的響應式程式設計模型
- 當功能在多處使用時，建立可重用的元件
- 使用 Astro 處理頁面路由和靜態內容

**樣式**：
- 使用 Tailwind CSS 類別進行樣式設計
- 在整個應用程式中維護暗色主題
- UI 元素使用圓角設計
- 遵循現代化 UI/UX 原則

#### GitHub Actions 工作流程

如果您需要修改 GitHub Actions 工作流程：
- 遵循良好的安全實踐
- 確保明確設定工作流程權限
- 添加註解以記錄正在執行的任務

### 使用指令檔案

本專案廣泛使用自定義指令檔案來指導 GitHub Copilot：

- `.github/copilot-instructions.md`: 專案級別的全域指令
- `.github/instructions/*.instructions.md`: 任務特定的指令檔案

### 取得協助

如果您有任何問題或需要協助：

1. 查看現有的文件
2. 在 Issues 中搜尋類似問題
3. 如果找不到答案，請開啟新的 Issue

### 資源連結

- [如何為開源專案貢獻](https://opensource.guide/how-to-contribute/)
- [使用拉取請求](https://help.github.com/articles/about-pull-requests/)
- [GitHub 說明](https://help.github.com)

---

## 行為準則

### 我們的承諾

為了營造一個開放和歡迎的環境，我們作為貢獻者和維護者承諾，讓參與我們的專案和社群成為一個無騷擾的體驗，無論年齡、體型、殘疾、種族、性別認同和表達、經驗水平、國籍、個人外表、種族、宗教或性認同和取向。

### 我們的標準

有助於創造積極環境的行為範例包括：

- 使用歡迎和包容的語言
- 尊重不同的觀點和經驗
- 優雅地接受建設性批評
- 專注於對社群最有利的事情
- 對其他社群成員表現出同理心

參與者不可接受的行為範例包括：

- 使用性化的語言或圖像以及不受歡迎的性關注或進展
- 挑釁、侮辱/貶損評論，以及個人或政治攻擊
- 公開或私下騷擾
- 未經明確許可發布他人的私人資訊
- 在專業環境中可能被合理視為不適當的其他行為

### 我們的責任

專案維護者負責澄清可接受行為的標準，並應對任何不可接受行為的實例採取適當和公平的糾正行動。

專案維護者有權利和責任刪除、編輯或拒絕不符合本行為準則的評論、提交、程式碼、wiki 編輯、問題和其他貢獻，或暫時或永久禁止任何他們認為不適當、威脅、冒犯或有害的其他行為的貢獻者。

### 範圍

本行為準則適用於專案空間和公共空間，當個人代表專案或其社群時。代表專案或社群的範例包括使用官方專案電子郵件地址、透過官方社交媒體帳戶發布，或在線上或線下活動中擔任指定代表。

### 執行

可以通過聯繫專案團隊 opensource@github.com 報告濫用、騷擾或其他不可接受的行為實例。所有投訴都將被審查和調查，並將產生被認為必要和適當的回應。專案團隊有義務對事件報告者保密。

---

## 安全政策

GitHub 重視我們的軟體產品和服務的安全性，包括透過我們的 GitHub 組織管理的所有開源程式碼存儲庫。

### 報告安全問題

如果您認為在任何 GitHub 擁有的存儲庫中發現了安全漏洞，請透過協調披露向我們報告。

**請不要透過公開的 GitHub 問題、討論或拉取請求報告安全漏洞。**

請發送電子郵件至 opensource-security[@]github.com。

請包含盡可能多的以下資訊：

- 問題類型（例如，緩衝區溢位、SQL 注入或跨站腳本）
- 與問題表現相關的源文件的完整路徑
- 受影響源代碼的位置（標籤/分支/提交或直接 URL）
- 重現問題所需的任何特殊配置
- 重現問題的逐步說明
- 概念驗證或漏洞利用代碼（如果可能）
- 問題的影響，包括攻擊者如何利用該問題

這些資訊將幫助我們更快地分類您的報告。

### 政策

請參閱 [GitHub 的安全港政策](https://docs.github.com/en/github/site-policy/github-bug-bounty-program-legal-safe-harbor#1-safe-harbor-terms)

---

## 支援資訊

### 如何提交問題和獲得幫助

本專案使用 GitHub issues 來追蹤錯誤和功能請求。在提交新問題之前，請搜尋現有問題以避免重複。對於新問題，請將您的錯誤或功能請求作為新問題提交。

如需有關使用本專案的幫助或問題，請[提交問題](/issues)。

### GitHub 支援政策

對本專案的支援僅限於上面列出的資源。本專案正在積極開發中，由 GitHub 員工和社群維護。我們將盡最大努力及時回應支援、功能請求和社群問題。

---

## 授權資訊

本專案依照 MIT 開源授權條款授權。詳細資訊請參閱 [LICENSE](./LICENSE) 檔案。

### MIT 授權條款摘要

MIT 授權是一個寬鬆的開源授權，允許：

- ✅ 商業使用
- ✅ 修改
- ✅ 分發
- ✅ 私人使用

條件是：

- 📋 必須包含授權和版權聲明

---

## 維護者

您可以在 [CODEOWNERS](./.github/CODEOWNERS) 中找到維護者清單。

維護者負責：
- 審查拉取請求
- 管理議題
- 指導專案方向
- 確保程式碼品質
- 維護文件

---

## 相關資源

### 官方文件

- [專案主頁 (README.md)](./README.md)
- [實驗指南 (docs/README.zh-TW.md)](./docs/README.zh-TW.md)
- [技術文件 (TECH_DOC_ZHTW.md)](./TECH_DOC_ZHTW.md)
- [貢獻指南 (CONTRIBUTING.md)](./CONTRIBUTING.md)
- [行為準則 (CODE_OF_CONDUCT.md)](./CODE_OF_CONDUCT.md)
- [安全政策 (SECURITY.md)](./SECURITY.md)
- [支援資訊 (SUPPORT.md)](./SUPPORT.md)

### 技術資源

- [Flask 文件](https://flask.palletsprojects.com/)
- [SQLAlchemy 文件](https://www.sqlalchemy.org/)
- [Astro 文件](https://astro.build/)
- [Svelte 文件](https://svelte.dev/)
- [Tailwind CSS 文件](https://tailwindcss.com/)
- [GitHub Copilot 文件](https://docs.github.com/copilot)
- [GitHub Actions 文件](https://docs.github.com/actions)
- [Model Context Protocol](https://modelcontextprotocol.io/)

### 社群資源

- [GitHub 存儲庫](https://github.com/AOCC-Org-POC-First-Phase/agents-in-sdlc-payton3)
- [提交 Issue](https://github.com/AOCC-Org-POC-First-Phase/agents-in-sdlc-payton3/issues)
- [查看 Pull Requests](https://github.com/AOCC-Org-POC-First-Phase/agents-in-sdlc-payton3/pulls)

---

## 總結

本文件整合了 Tailspin Toys 專案的所有繁體中文說明文件，涵蓋：

- ✅ 專案簡介與技術架構
- ✅ 完整的安裝與使用指南
- ✅ 詳細的專案結構說明
- ✅ 完整的實驗教學（練習 0-7）
- ✅ 貢獻指南與開發標準
- ✅ 行為準則與安全政策
- ✅ 支援資訊與相關資源

希望這份整合文件能幫助您更好地理解和使用 Tailspin Toys 專案，並充分利用 GitHub Copilot 的強大功能來提升開發效率！

如果您有任何問題或建議，歡迎透過 GitHub Issues 與我們聯繫。

---

**感謝您使用 Tailspin Toys！**

本專案按原樣提供，並會隨時間更新。如果您有任何問題，請開啟 Issue。

最後更新：2024年10月  
版本：1.0.0
