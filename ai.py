def resume_score(resume_text, jd_text):
    
    skills = [
        "python","java","sql","react","node","aws",
        "docker","ml","ai","django","flask","mongodb",
        "excel","git"
    ]

    resume_text = resume_text.lower()
    jd_text = jd_text.lower()

    matched = [s for s in skills if s in resume_text and s in jd_text]

    if len(jd_text.split()) == 0:
        return 0

    score = int((len(matched) / len(skills)) * 100)

    return score