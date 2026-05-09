import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="DRG.ai", page_icon="🩺", layout="wide")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash-latest")

SYSTEM_PROMPT = """
Si skúsený slovenský DRG kóder a lekársky analytik so silným klinickým porozumením chirurgii, interným odborom a nemocničnej dokumentácii.

Tvoja úloha:
- analyzovať epikrízy
- analyzovať operačné protokoly
- rozpoznať hlavné a vedľajšie diagnózy
- navrhnúť možné MKCH kódy
- navrhnúť možné zdravotnícke výkony
- upozorniť na chýbajúcu dokumentáciu
- navrhnúť doplnenie textu pre lepšie DRG kódovanie

Dôležité pravidlá:
- nikdy nevymýšľaj presný kód, ak si nie si istý
- ak nemáš číselník, napíš "potrebné overiť v číselníku"
- rozlišuj diagnózu, výkon, komplikáciu a komorbiditu
- pri MKCH nepoužívaj skrátené kódy ako konečné, ak môže existovať presnejší podkód
- pri výkone odlišuj laparoskopiu, laparotómiu, revíziu, drenáž, resekciu, anastomózu, sutúru a konverziu

Výstup vždy štruktúruj:

1. Typ vstupu
2. Hlavná diagnóza
3. Vedľajšie diagnózy
4. Výkony
5. Možné pripočítateľné položky
6. Chýbajúce informácie
7. DRG odporúčania
8. Čo overiť v číselníkoch
"""

st.title("DRG.ai")
st.caption("Vlož epikrízu, operačný protokol, výkon alebo otázku.")

user_text = st.text_area(
    "Text na analýzu",
    height=360,
    placeholder="Sem vlož epikrízu, operačný protokol alebo otázku..."
)

if st.button("Analyzovať", type="primary"):
    if not user_text.strip():
        st.warning("Najprv vlož text.")
    else:
        prompt = f"{SYSTEM_PROMPT}\n\nVSTUP:\n{user_text}"

        with st.spinner("Analyzujem..."):
            response = model.generate_content(prompt)

        st.subheader("Výsledok")
        st.write(response.text)
