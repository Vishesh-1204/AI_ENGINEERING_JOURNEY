import streamlit as st
from PyPDF2 import PdfReader

def extract_text(pdf_file):

    pdf = PdfReader(pdf_file)

    text = ""

    for page in pdf.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text.lower()

from skills import SKILLS

def extract_skills(text):

    found_skills = set()

    for skill in SKILLS:

        if skill in text:

            found_skills.add(skill)

    return list(found_skills)

def calculate_match_score(
    resume_skills,
    job_keywords
):

    matched = []

    for keyword in job_keywords:

        if keyword in resume_skills:

            matched.append(keyword)

    if len(job_keywords) == 0:
        return 0, []

    score = (
        len(matched)
        /
        len(job_keywords)
    ) * 100

    return score, matched

st.title(
    "AI Resume Analyzer"
)

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_input = st.text_area(
    "Required Skills",
    placeholder=
    "Python, SQL, FastAPI"
)

if st.button("Analyze Resume"):

    if uploaded_file:

        text = extract_text(
            uploaded_file
        )
        
        word_count = len(text.split())

        resume_skills = extract_skills(
            text
        )

        job_keywords = [
            skill.strip().lower()
            for skill in job_input.split(",")
            if skill.strip()
        ]

        if len(job_keywords) == 0:

            st.error(
                "Please enter required skills."
            )

        else:

            score, matched = calculate_match_score(
                resume_skills,
                job_keywords
            )

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Skills Found",
                    len(resume_skills)
                )

            with col2:
                st.metric(
                    "Match %",
                    f"{score:.0f}%"
                )
            
            with col3:
                st.metric(
                    "Words",
                    word_count
                )

            st.subheader(
                "Extracted Skills"
            )

            for skill in resume_skills:
                    st.write(f"✓ {skill}")

            st.subheader(
                "Matched Skills"
            )

            for skill in matched:
                st.write(f"✓ {skill}")

            st.subheader(
                "Missing Skills"
            )

            missing = [
                skill
                for skill in job_keywords
                if skill not in matched
            ]

            for skill in missing:
                st.write(f"✗ {skill}")

            st.subheader(
                "Match Score"
            )

            st.success(
                f"{score:.2f}%"
            )

    else:

        st.error(
            "Please upload a resume PDF."
        )