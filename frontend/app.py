import streamlit as st
import requests

st.title("LLaMA Text Summarizer")
user_input = st.text_area("Enter your text here:")

if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        try:
            res = requests.post(
                "http://localhost:8000/summarize/",
                json={"text": user_input},
                timeout=120
            )

            st.subheader("Summary:")

            if res.status_code != 200:
                st.error(f"Backend error {res.status_code}")
                st.code(res.text)
            else:
                data = res.json()
                if "summary" in data:
                    st.write(data["summary"])
                else:
                    st.error("No summary returned. Backend response:")
                    st.json(data)

        except Exception as e:
            st.error(str(e))
