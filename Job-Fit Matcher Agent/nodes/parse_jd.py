def parse_jd(state: dict) -> dict:
    print(">>> parse_jd node running...")

    job_title = state.get("job_title_input", "").strip()
    raw_text = state["jd_raw_text"]

    cleaned = "\n".join(line.strip() for line in raw_text.splitlines() if line.strip())

    # Agar user ne job title diya hai, to usse top pe explicitly jod do
    if job_title:
        cleaned = f"Job Title: {job_title}\n\n{cleaned}"

    return {"jd_text": cleaned}