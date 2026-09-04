import shutil
import uuid
import os

from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware

from graph import app as graph_app

api = FastAPI(title="Job-Fit Matcher API")

# CORS: React (jo alag port pe chalega, jaise localhost:3000) ko is API ko call karne dena
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # abhi ke liye sab allow, baad mein specific origin de sakte ho
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@api.post("/analyze")
async def analyze(resume: UploadFile, job_title: str = Form(""), jd_text: str = Form(...)):
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}.pdf")

    with open(file_path, "wb") as f:
        shutil.copyfileobj(resume.file, f)

    initial_state = {
        "resume_file_path": file_path,
        "job_title_input": job_title,
        "jd_raw_text": jd_text,
    }

    result = graph_app.invoke(initial_state)

    os.remove(file_path)

    report = result["match_report"]

    return {
        "semantic_score": result["semantic_score"],
        "matched_skills": result["matched_skills"],
        "missing_skills_quick": result["missing_skills"],
        "overall_fit_score": report.overall_fit_score,
        "strengths": report.strengths,
        "missing_skills": report.missing_skills,
        "suggestions": report.suggestions,
    }