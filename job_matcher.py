from llm import ask_llm

def match_job(resume_text, job_description):

    prompt = f"""
Compare this resume with the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Give:

1. Match Score
2. Matching Skills
3. Missing Skills
4. Relevant Experience
5. Suggestions
"""

    return ask_llm(prompt)