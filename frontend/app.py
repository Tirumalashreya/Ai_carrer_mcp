import streamlit as st
import requests

st.set_page_config(page_title="Career & Resume Assistant", page_icon="🧠", layout="centered")

st.title("🧠 AI Career & Resume Assistant")
st.markdown("Welcome! Talk to your **Career Coach** or get help with your **Resume**.\n\n"
            "Try asking:\n"
            "- _What skills should I learn for data science?_\n"
            "- _Optimize my resume for a software engineer role._")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input area
user_input = st.chat_input("Ask a question or request resume help...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            "http://localhost:8000/mcp",
            json={
                "user_input": user_input,
                "chat_history": [msg["content"] for msg in st.session_state.chat_history if msg["role"] == "user"]
            }
        )

        if response.status_code == 200:
            reply = response.json().get("response", "🤖 No response received.")
            st.session_state.chat_history.append({"role": "coach", "content": reply})
        else:
            st.error("❌ Error: CoachGPT API could not respond.")
    except Exception as e:
        st.error(f"❌ Connection error: {e}")

# Chat history rendering
if st.session_state.chat_history:
    st.divider()
    for msg in st.session_state.chat_history:
        role = msg["role"]
        avatar = "👤" if role == "user" else "🧠"
        with st.chat_message(role, avatar=avatar):
            st.markdown(msg["content"])
