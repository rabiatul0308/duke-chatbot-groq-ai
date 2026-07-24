import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


st.set_page_config(page_title="Duke Chatbot", page_icon="👑")
st.title("The Duke's Chambers")
st.caption("A formal and courteous AI assistant powered by Groq & Llama 3.3")

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

if "riwayat_chat" not in st.session_state:
    st.session_state.riwayat_chat = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant that provides information and answers"
                " questions. Pretend you are a Duke of a grand estate, and respond"
                " in a formal and courteous manner."
            ),
        }
    ]

for msg in st.session_state.riwayat_chat:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])


if user_prompt := st.chat_input("Enter your message for the Duke..."):

    with st.chat_message("user"):
        st.markdown(user_prompt)


    st.session_state.riwayat_chat.append({"role": "user", "content": user_prompt})

   
    try:
        with st.chat_message("assistant"):
            with st.spinner("The Duke is pondering..."):
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=st.session_state.riwayat_chat,
                    temperature=0.7,
                    max_tokens=100,
                )
                response_content = response.choices[0].message.content
                st.markdown(response_content)

        st.session_state.riwayat_chat.append(
            {"role": "assistant", "content": response_content}
        )

    except Exception as e:
        st.error(f"An error occurred: {e}")
