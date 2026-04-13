from langgraph.graph import StateGraph
from typing import TypedDict
from openai import OpenAI

# 連接你的 vLLM
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="dummy"
)

# 定義狀態
class State(TypedDict):
    input: str
    output: str

# LLM 節點
def call_llm(state: State):
    response = client.chat.completions.create(
        model="google/gemma-2-2b-it",
        messages=[
            {"role": "user", "content": state["input"]}
        ],
        temperature=0.7
    )
    return {"output": response.choices[0].message.content}

# 建 graph
graph = StateGraph(State)
graph.add_node("llm", call_llm)

# 設定流程
graph.set_entry_point("llm")
graph.set_finish_point("llm")

app = graph.compile()

# 測試
result = app.invoke({"input": "人生是為了什麼?"})
print(result["output"])