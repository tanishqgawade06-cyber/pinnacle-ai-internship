import streamlit as st
import requests

# 1. Setup the Webpage
st.set_page_config(page_title="AI Autocorrect", page_icon="✍️")
st.title("Intelligent Autocorrect ✍️")
st.write("Type a sentence below. Use `[MASK]` for the word you want the AI to fix or predict.")

# 2. Create the Text Box
user_text = st.text_area("Draft your text here:", "I want to read a good [MASK] tonight.")

# 3. Create the Action Button
if st.button("Analyze & Fix Text"):
    if "[MASK]" in user_text:
        with st.spinner("AI is thinking..."):
            # 4. Send the text to your FastAPI backend
            api_url = "https://pinnacle-ai-internship.onrender.com/predict"
            payload = {"sentence": user_text}
            
            try:
                response = requests.post(api_url, json=payload)
                data = response.json()
                
                # 5. Display the Results beautifully
                st.subheader("Top Suggestions:")
                for item in data['top_suggestions']:
                    st.success(f"**{item['word']}** — Confidence: {item['confidence']}%")
            
            except Exception as e:
                st.error("Could not connect to the AI brain. Is your FastAPI server running in the other terminal?")
    else:
        st.warning("Please include `[MASK]` in your sentence so the AI knows which word to analyze!")