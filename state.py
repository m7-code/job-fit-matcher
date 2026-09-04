from typing import TypedDict, List
from schemas import ResumeInfo, JDInfo, MatchReport


class ResumeJDState(TypedDict):
    resume_file_path: str
    resume_text: str
    jd_raw_text: str
    jd_text: str
    resume_struct: ResumeInfo
    jd_struct: JDInfo
    semantic_score: float
    matched_skills: List[str]
    missing_skills: List[str]
    match_report: MatchReport