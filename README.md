# 金融 FAQ AI Agent

本專案實作一個本地運行的 AI 客服系統，透過 LangGraph 設計 Agent workflow，結合 FAQ 知識庫與 LLM 回答能力，模擬金融客服情境。

---

## 專案介紹

此專案展示如何將 LLM 從單純的文字生成工具，提升為具備流程控制與知識查詢能力的 AI Agent 系統。

系統會先判斷問題類型，再決定使用 FAQ 查詢或 LLM 回答。

---

## 系統流程

使用者輸入問題後：

1. 透過 LLM 判斷問題類型（FAQ 或 LLM）
2. 若為 FAQ 類問題 → 查詢本地 FAQ（支援同義問法 aliases）
3. 若找不到或非 FAQ → 交由 LLM 回答
4. 回傳最終答案並顯示來源（FAQ 或 LLM）

---

## 技術架構

- LLM：本地模型（透過 vLLM 部署）
- Agent：LangGraph（流程控制）
- 前端：Streamlit
- 知識庫：JSON FAQ

---

## 系統架構圖

```text
使用者
 ↓
Streamlit UI
 ↓
LangGraph Workflow
 ↓
問題分類
 ├─ FAQ 查詢（faq.json）
 └─ LLM 回答（vLLM）
 ↓
回傳答案