# FAQ AI Agent

本專案實作一個本地運行的 AI 客服系統，透過 LangGraph 設計 Agent workflow，結合 FAQ 知識庫與 LLM 回答能力。

---

## 技術架構

- LLM：本地模型（透過 vLLM 部署）
- Agent：LangGraph（流程控制）
- 前端：Streamlit
- 知識庫：JSON FAQ

---

## 系統流程

使用者輸入問題後：

1. 先由 LLM 判斷問題類型（FAQ 或 LLM）
2. 如果是 FAQ 類問題 → 查詢本地 FAQ（支援同義問法）
3. 如果找不到或非 FAQ → 交由 LLM 回答
4. 回傳最終結果並顯示來源

---

## 功能特色

- 本地 LLM（不依賴外部 API）
- Agent workflow（非單純聊天）
- FAQ + LLM 混合回答
- 支援同義問法（aliases）
- Streamlit 即時聊天介面

---

## 啟動方式

### 1️⃣ 啟動 vLLM

```bash
python -m vllm.entrypoints.openai.api_server \
  --model google/gemma-2-2b-it