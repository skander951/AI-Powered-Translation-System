#we run client after launchig serve.py and we must keep the cmd concerning serve.py open

import requests
import streamlit as st


def get_groq_response(input_text):
    payload = {
        "input": {
            "language": "French",
            "text": input_text
        },
        "config": {},
        "kwargs": {}
    }
    
    try:
        response = requests.post(
            "http://localhost:8000/chain/invoke",
            json=payload,
            timeout=5
        )
        return response.json()
    except requests.exceptions.ConnectionError:
        st.error("Le serveur n'est pas disponible. Lancez d'abord 'python serve.py'")
        return None

## Streamlit app
st.title("LLM Application Using LCEL")
input_text=st.text_input("Enter the text you want to convert to french")

if input_text:
    st.write(get_groq_response(input_text))