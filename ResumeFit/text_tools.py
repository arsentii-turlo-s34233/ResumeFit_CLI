import re

def find_skill(text, skill_set):
    text = text.lower()
    return{
        skill
        for skill in skill_set
        if re.search(r"\b" + re.escape(skill) + r"\b", text) # \b = word boundary; re.escape handles symbols like + or /
    }

def find_yrs_exp(text):
    text = text.lower()
    matches = re.findall(r"(\d+)\+?\s*(?:years|year|yrs|yr)", text) #(\d+) - find one or more digits (like 1 or 10)
                                                                            #\+? - optional plus sign
                                                                            #\s* - optional spaces
                                                                            #(?:years|year|yrs|yr) - group of possible words
    years = []
    for match in matches:
        years.append(int(match))
    if years:
        return max(years)
    return 0

def find_edu_lvl(text):
    text = text.lower()
    master_pattern = r"\b(master|msc|m\.sc|ma|m\.a|graduate degree)\b"
    bachelor_pattern = r"\b(bachelor|bsc|b\.sc|ba|b\.a|undergraduate degree|university degree|degree)\b"
    student_pattern = r"\b(student|undergraduate student|computer science student)\b"
    high_school_pattern = r"\b(high school|secondary school)\b"
    if re.search (master_pattern, text):
        return "master"
    if re.search (bachelor_pattern, text):
        return "bachelor"
    if re.search (student_pattern, text):
        return "student"
    if re.search (high_school_pattern, text):
        return "high school"
    return "not detected"

def edu_rank (level):
    ranks = {
        "not detected": 0,
        "high school": 1,
        "student": 2,
        "bachelor": 3,
        "master": 4,
    }
    return ranks.get(level, 0)

def format_skills(skills):
    return [skill.title() for skill in sorted(skills)]