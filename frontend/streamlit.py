import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/match"


st.set_page_config(page_title="AI Hiring Copilot", layout="wide")


st.title("🤯AI Hiring Copilot")
st.write("Upload a resume and a job description to see how well they matched!")

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd = st.text_area("Please upload a resume and paste a job description.")

if st.button("Analyze"):
    if resume is None or jd.strip() == "":
        st.warning("Please upload a resume and paste a job description")
    else:
     files = {"file": resume}
     data = {"job_description": jd}
    
    with st.spinner("Analysing..."):
        response = requests.post(API_URL, files=files, data=data)
        
    if response.status_code == 200:
        result = response.json()
        
        st.subheader("📁 Resume Preview")
        st.text_area(
            "Extracted Resume Text",
            result['resume_preview'],
            height=250
        )
        
        st.subheader("JD Preview 🏢")
        st.text_area(
            "Extracted JD Preview",
            result['jd_preview'],
            height=200
        )
        
        
        st.subheader("📊 Match Score")
        st.progress(result["Semantic_based_Score"] / 100)
        st.write(f"Semantic Match: {result['Semantic_based_Score']:.2f}%")
        st.metric("Rule Based Score", f"{result['Rule_based_Score']:.2f}%")
        
        col1, col2 = st.columns(2)

        with col1:
         st.success("Matched Skills")
         for skill in result["Matched_Skills"]:
          st.write("✅", skill)

        with col2:
         st.error("Missing Skills")
         for skill in result["Missing_SKills"]:
          st.write("❌", skill)  
                
        st.subheader("🧠 AI Recruiter Feedback")
        st.info(result["AI-Feedback"])
        
    else:
        st.error("Something seems broken, just like my heart 💘")
        