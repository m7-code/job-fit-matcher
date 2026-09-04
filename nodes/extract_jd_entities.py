from llm_config import llm
from schemas import JDInfo


def extract_jd_entities(state: dict) -> dict:
    print(">>> extract_jd_entities node running...")

    structured_llm = llm.with_structured_output(JDInfo)

    prompt = f"Extract structured information from this job description:\n\n{state['jd_text']}"
    result = structured_llm.invoke(prompt)

    return {"jd_struct": result}