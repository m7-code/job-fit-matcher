from llm_config import llm
from schemas import ResumeInfo


def extract_resume_entities(state: dict) -> dict:
    print(">>> extract_resume_entities node chal raha hai...")

    structured_llm = llm.with_structured_output(ResumeInfo)

    prompt = f"Extract structured information from this resume:\n\n{state['resume_text']}"
    result = structured_llm.invoke(prompt)

    return {"resume_struct": result}