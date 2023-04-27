import streamlit as st
import requests
import json
from scraping import scrape_aspx, scrape, fetch
from summarize import load_model, summarize

default_url = "https://www.gov.il/he/Departments/policies?OfficeId=e744bba9-d17e-429f-abc3-50f7a8a55667&blockCollector=true&limit=10&PmoMinistersComittee=a0d9709c-f07d-4b0e-8c48-0939643eb020&skip=0"
with open('secrets/tokens.json', 'r') as f:
    tokens = json.load(f)
    api_token = tokens['HF']


keywords = [
"הומו",
"הומואים",
"הקהילה הגאה",
"התאמה מגדרית",
"טיפול המרה",
"טיפולי המרה",
"טרנסג'נדר",
'להט"ב'
"לסביות",
"לסבית",
"נטיות הפוכות",
"פונדקאות",
"קהילה גאה",
"שינוי מין",
    "נשים"
]

scrape_url = False
analyze_text = False

# Using "with" notation
with st.sidebar:
    with st.form("url_form"):
        url = st.text_input('אתר לחיפוש')
        if not url:
            url = st.radio(
                "בחרו אתר לחיפוש טקסטים",
                ("אתר א",
                 "אתר ב",
                 "אתר ג",
                 "אתר ד")
            )
        submitted = st.form_submit_button("Submit")
        if submitted:
            scrape_url = True

    with st.form("text_form"):
        text_input = st.text_area('הכניסו טקסט')

        submitted_text = st.form_submit_button("Submit")
        if submitted_text:
            analyze_text = True



def is_relevant(text, kwords):
    excerpts = text.split(". ")
    for i, excerpt in enumerate(excerpts):
        if any(k in text for k in kwords):
            st.write(f'this text contains lgbtq relevant text: ')
            text_to_print = ""
            if i > 0:
                text_to_print += excerpts[i-1] + ". "
            text_to_print += f"<b>{excerpt}</b>. "
            if i < len(excerpts):
                text_to_print += excerpts[i+1] + "."
            st.markdown(text_to_print, unsafe_allow_html=True)

model_name = "google/mt5-small"
# model_name = "csebuetnlp/mT5_multilingual_XLSum"

def main():
    st.title('זיהוי נושאים להטבים בהחלטות ממשלה')
    # user_input = st.text_input('enter text', 'type here...')
    # model, tokenizer = load_model(model_name)
    if scrape_url:
        st.write(url)
    if analyze_text:
        if text_input:
            # summary = summarize(tokenizer, model, text=user_input)
            st.subheader('summary')
            # print(summary, type(summary))
            is_relevant(text_input, keywords)


if __name__ == '__main__':
    main()