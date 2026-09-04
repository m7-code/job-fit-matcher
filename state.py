from typing import TypedDict, List
from schemas import ResumeInfo, JDInfo, MatchReport


class ResumeJDState(TypedDict):
    resume_file_path: str
    resume_text: str
    job_title_input: str      # naya: user ka diya hua job title
    jd_raw_text: str          # ye ab "description/context" field hai
    jd_text: str
    resume_struct: ResumeInfo
    jd_struct: JDInfo
    semantic_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    match_report: MatchReport