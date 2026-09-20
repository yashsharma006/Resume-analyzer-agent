import streamlit as st

from resume_parser import extract_text
from resume_analyzer import analyze_resume
from job_matcher import match_job
from recruiter import generate_questions, evaluate_answer

#frontend

st.title("📄 Resume Analyzer & Job Matcher")

resume = st.file_uploader("Upload Resume", type=["pdf"])

job = st.text_area("Paste Job Description")

#if button click

if st.button("Analyze"):

    if resume and job:

        resume_text = extract_text(resume)

        st.subheader("📊 Resume Analysis")
        st.write(analyze_resume(resume_text))

        st.subheader("🎯 Job Match")
        st.write(match_job(resume_text, job))
#temp memory
        st.session_state.resume = resume_text
        st.session_state.job = job

    else:
        st.warning("Upload resume and enter job description")


if "resume" in st.session_state:

    st.subheader("🎤 AI Recruiter")

    if st.button("Start Interview"):
#generate question
        questions = generate_questions(
            st.session_state.resume,
            st.session_state.job
        )

        st.session_state.questions = questions
#check answers
    if "questions" in st.session_state:

        question = st.text_area(
            "Interview Question",
            st.session_state.questions
        )

        answer = st.text_area("Your Answer")

        if st.button("Evaluate Answer"):

            result = evaluate_answer(
                question,
                answer
            )

            st.write(result)