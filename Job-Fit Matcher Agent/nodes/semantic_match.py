import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


def semantic_match(state: dict) -> dict:
    print(">>> semantic_match node chal raha hai...")

    resume_struct = state["resume_struct"]
    jd_struct = state["jd_struct"]

    resume_skills = resume_struct.skills
    jd_skills = jd_struct.required_skills

    resume_skills_lower = [s.lower().strip() for s in resume_skills]

    matched_skills = []
    missing_skills = []

    # Exact / substring match — reliable tareeqa skill-level comparison ke liye
    for jd_skill in jd_skills:
        jd_skill_lower = jd_skill.lower().strip()

        found = any(
            jd_skill_lower == r or jd_skill_lower in r or r in jd_skill_lower
            for r in resume_skills_lower
        )

        if found:
            matched_skills.append(jd_skill)
        else:
            missing_skills.append(jd_skill)

    # Overall score — semantic similarity (ye aggregate comparison ke liye reliable hai)
    resume_vectors = embeddings_model.embed_documents(resume_skills)
    jd_vectors = embeddings_model.embed_documents(jd_skills)
    resume_avg = np.mean(resume_vectors, axis=0)
    jd_avg = np.mean(jd_vectors, axis=0)
    overall_score = cosine_similarity([resume_avg], [jd_avg])[0][0]

    return {
        "semantic_score": round(float(overall_score) * 100, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }