import streamlit as st
from agent_faq import app as agent_app

st.title("我的 AI Agent 🤖")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if msg["role"] == "assistant" and "route" in msg:
            st.caption(f"來源：{msg['route']}")

if prompt := st.chat_input("請輸入訊息"):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.write(prompt)

    result = agent_app.invoke({"user_input": prompt})

    reply = result["final_answer"]
    route = result.get("route", "llm")

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply,
        "route": route
    })

    with st.chat_message("assistant"):
        st.write(reply)
        st.caption(f"來源：{route}")