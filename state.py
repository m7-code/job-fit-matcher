from typing import TypedDict


class ResumeJDState(TypedDict):
    resume_file_path: str   # PDF file ka path
    resume_text: str        # PDF se nikala hua text
    jd_text: str