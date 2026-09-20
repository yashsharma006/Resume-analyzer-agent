from llm import ask_llm

def analyze_resume(resume_text):

    prompt = f"""
Analyze this resume.

Resume:
{resume_text}

Give:

1. Name
2. Skills
3. Education
4. Experience
5. Projects
6. Strengths
7. Weaknesses
"""

    return ask_llm(prompt)