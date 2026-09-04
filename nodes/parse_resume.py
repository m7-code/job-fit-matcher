from pypdf import PdfReader


def parse_resume(state: dict) -> dict:
    print(">>> parse_resume node running...")

    file_path = state["resume_file_path"]

    reader = PdfReader(file_path)

    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text() + "\n"

    return {"resume_text": full_text}