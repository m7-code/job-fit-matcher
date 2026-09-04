from pydantic import BaseModel, Field
from typing import List


class ResumeInfo(BaseModel):
    name: str = Field(description="Full name of the candidate")
    skills: List[str] = Field(description="All technical skills of the candidate")
    experience_years: int = Field(description="Total years of professional experience")
    education: str = Field(description="Highest qualification, e.g. 'BS Computer Science'")


class JDInfo(BaseModel):
    job_title: str = Field(description="Job title/designation")
    required_skills: List[str] = Field(description="Technical skills required for the job")
    nice_to_have_skills: List[str] = Field(description="Skills that are a bonus but not mandatory")
    min_experience_years: int = Field(description="Minimum years of experience required")
    responsibilities: List[str] = Field(description="Main responsibilities/duties of the job")


class MatchReport(BaseModel):
    overall_fit_score: int = Field(description="Overall fit score between 0-100, based on how well the resume matches the job description")
    strengths: List[str] = Field(description="Key strengths of the candidate relevant to this job")
    missing_skills: List[str] = Field(description="Important skills or qualifications required by the job but missing or not clearly shown in the resume")
    suggestions: List[str] = Field(description="Specific, actionable suggestions to improve the resume for this job — e.g. add a skill, rephrase a section, add a project")