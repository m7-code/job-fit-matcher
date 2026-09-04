from graph import app

sample_jd_raw = """
We are looking for a Python Developer with 2+ years experience.
Required Skills: Python, Django, REST APIs, SQL, Git
Nice to have: Docker, AWS, React
"""

initial_state = {
    "resume_file_path": "sample_resume.pdf",
    "jd_raw_text": sample_jd_raw,
}

result = app.invoke(initial_state)

report = result["match_report"]

print("\n=== Job-Fit Match Report ===")
print(f"Overall Fit Score: {report.overall_fit_score}/100")

print("\nStrengths:")
for s in report.strengths:
    print(" -", s)

print("\nMissing Skills:")
for s in report.missing_skills:
    print(" -", s)

print("\nSuggestions:")
for s in report.suggestions:
    print(" -", s)