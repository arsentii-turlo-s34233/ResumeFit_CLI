from ResumeFit.text_tools import edu_rank

def calc_perc_score (matched_items, required_items):
    if len (required_items) == 0:
        return 100
    return  len(matched_items) / len(required_items) * 100

def calc_exp_score (resume_years, job_years):
    if job_years == 0:
        return 100
    if resume_years >= job_years:
        return 100
    return resume_years/job_years * 100

def get_match_lvl(ovrl_score):
    if ovrl_score >= 85:
        return "Strong candidate fit"
    if ovrl_score >= 70:
        return "Good candidate fit"
    if ovrl_score >= 40:
        return "Weak candidate fit"
    return "Too low match"

def calc_edu_score (resume_edu, job_edu):
    if job_edu == "not detected":
        return 100
    if edu_rank(resume_edu) >= edu_rank(job_edu):
        return 100
    return 0

def calc_ovrl_score (hard_skill_score, soft_skill_score, exp_score, edu_score):
    return (
        hard_skill_score * 0.5 +
        soft_skill_score * 0.2 +
        exp_score * 0.2 +
        edu_score * 0.1
    )