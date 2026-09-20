from llm import ask_llm


def generate_questions(resume, job_description):

    prompt = f"""
You are a technical recruiter.

Based on the candidate's resume and the job description,
generate 5 interview questions.

RESUME:
{resume}

JOB DESCRIPTION:
{job_description}

Questions should include:
- 2 technical questions
- 1 project-based question
- 1 behavioral question
- 1 question about a missing skill

Return only the questions.
"""

    return ask_llm(prompt)


def evaluate_answer(question, answer):

    prompt = f"""
You are a technical recruiter.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Give:

1. Score out of 10
2. What was good
3. What was missing
4. How to improve the answer
5. Better sample answer
"""

    return ask_llm(prompt)