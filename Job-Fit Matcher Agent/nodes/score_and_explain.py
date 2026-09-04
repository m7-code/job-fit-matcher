from llm_config import llm
from schemas import MatchReport


def score_and_explain(state: dict) -> dict:
    print(">>> score_and_explain node chal raha hai...")

    structured_llm = llm.with_structured_output(MatchReport)

    prompt = f"""
You are an expert career coach and technical recruiter.

Compare the following resume with the job description and provide an honest, detailed evaluation.

Resume:
{state['resume_text']}

Job Description:
{state['jd_text']}

A rough automated similarity score (for reference only, you don't have to fully agree with it): {state['semantic_score']}%

Give your own independent judgment on the overall fit score, the candidate's strengths,
the important missing skills/qualifications, and specific actionable suggestions to
improve this resume for this exact job.
"""

    result = structured_llm.invoke(prompt)

    return {"match_report": result}