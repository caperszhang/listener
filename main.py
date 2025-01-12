import streamlit as st
from langchain.memory import ConversationBufferMemory

from utils import get_chat_response



st.title("💬 树洞，阅后即焚")

openai_api_key = "sk-a8acecc0a0aa4bc5a0ff27c8fe8f42c8"

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "我是你的树洞，你可以在这里倾诉你的心声，我会倾听你的故事。"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input(placeholder="请输入你的心声")
if prompt:
    if not openai_api_key:
        st.info("请输入你的OpenAI API Key")
        st.stop()
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("树洞沉吟片刻..."):
        response = get_chat_response(prompt, st.session_state["memory"],
                                     openai_api_key)
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)