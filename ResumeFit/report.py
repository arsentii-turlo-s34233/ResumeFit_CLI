from ResumeFit.text_tools import format_skills, edu_rank

def print_report(result):
    print("")
    print("|--  RESUME FIT REPORT   --|")
    print("")
    print(f"Overall score: {result.overall_score:.1f}%")
    print("Match level:", result.match_lvl)
    print("Skill summary:")
    for category, count in result.skill_summary.items():
        print("-", category + ":", count)
    print("")
    print("|--  SCORE DETAILS   --|")
    print("")
    print(f"Hard skills score: {result.hard_skills_score:.1f}%")
    print(f"Soft skills score: {result.soft_skills_score:.1f}%")
    print(f"Experience score: {result.exp_score:.1f}%")
    print(f"Education score: {result.edu_score:.1f}%")
    print("")
    print("Matched hard skills: ")
    if result.matched_hard_skills:
        for skill in format_skills(result.matched_hard_skills):
            print("+", skill)
    else:
        print("None")
    print("Missing hard skills: ")
    if result.missing_hard_skills:
        for skill in format_skills(result.missing_hard_skills):
            print("-", skill)
    else:
        print("None")
    print("Matched soft skills: ")
    if result.matched_soft_skills:
        for skill in format_skills(result.matched_soft_skills):
            print("+", skill)
    else:
        print("None")
    print("Missing soft skills: ")
    if result.missing_soft_skills:
        for skill in format_skills(result.missing_soft_skills):
            print("-", skill)
    else:
        print("None")
    print("")
    print("Resume years of experience: " + str(result.resume_years))
    print("Job years of experience: " + str(result.job_years))
    if result.job_years == 0:
        print("Experience match: not required")
    elif result.resume_years >= result.job_years:
        print("Experience match: Yes")
    else:
        print("Experience match: No")
    print("")
    print("Resume education: " + str(result.resume_edu))
    print("Job education: " + str(result.job_edu))
    if result.job_edu == "not detected":
        print("Education match: not required")
    elif edu_rank(result.resume_edu) >= edu_rank(result.job_edu):
        print("Education match: Yes")
    else:
        print("Education match: No")
    print("")
    print("|--  Recommendations  --|")
    print("")

    if result.recommendations:
        for recommendation in result.recommendations:
            print(recommendation)
    else:
        print("- Your resume looks well aligned with this job description.")