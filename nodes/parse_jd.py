def parse_jd(state: dict) -> dict:
    print(">>> parse_jd node running...")

    raw_text = state["jd_raw_text"]

    # Extra spaces aur empty lines saaf karo
    cleaned = "\n".join(line.strip() for line in raw_text.splitlines() if line.strip())

    return {"jd_text": cleaned}