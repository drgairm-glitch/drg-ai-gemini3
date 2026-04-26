import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="DRG Gemini", page_icon="🩺")

st.title("DRG asistent Gemini")
st.caption("Vlož epikrízu, operačný protokol alebo otázku")

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-pro")

SYSTEM_PROMPT = """
Si skúsený DRG kóder pre slovenský DRG systém.

Pomáhaš analyzovať:
- diagnózy
- výkony
- DRG pravidlá
- epikrízy
- operačné protokoly

Odpovedaj presne, stručne a medicínsky správne.
"""

user_text = st.text_area("Text", height=300)

if st.button("Analyzovať"):

    prompt = SYSTEM_PROMPT + "\n\nPoužívateľ:\n" + user_text

    response = model.generate_content(prompt)

    st.subheader("Výsledok")
    st.write(response.text)

