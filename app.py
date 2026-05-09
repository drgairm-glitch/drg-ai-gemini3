import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash")

st.title("DRG AI")

text = st.text_area("Vlož epikrízu / operačný protokol / otázku")

if st.button("Analyzovať"):
    with st.spinner("Analyzujem..."):
        response = model.generate_content(text)
        st.write(response.text)
