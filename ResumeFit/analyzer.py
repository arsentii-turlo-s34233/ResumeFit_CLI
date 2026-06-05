from ResumeFit.constants import HARD_SKILLS, SOFT_SKILLS
from ResumeFit.decorators import require_loaded_docs
from ResumeFit.models import AnalysisResult
from ResumeFit.scoring import (calc_perc_score, calc_exp_score, calc_edu_score, calc_ovrl_score, get_match_lvl)
from ResumeFit.text_tools import (find_skill, find_yrs_exp, find_edu_lvl, edu_rank)

def build_skill_summary(matched_hard_skills, matched_soft_skills, missing_hard_skills,
    missing_soft_skills):
    summary = {
        "matched hard skills": matched_hard_skills,
        "missing hard skills": missing_hard_skills,
        "matched soft skills": matched_soft_skills,
        "missing soft skills": missing_soft_skills
    }
    counts = {
        category: len(skills)
        for category, skills in summary.items()
    }
    sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return dict(sorted_counts)

def generate_recommendations(missing_hard_skills, missing_soft_skills,
    resume_years, job_years, resume_edu, job_edu):
    for skill in sorted(missing_hard_skills):
        yield "- Consider adding " + skill + " if you have real experience with it."

    for skill in sorted(missing_soft_skills):
        yield "- Add evidence of " + skill + " if it honestly describes you."

    if job_years > 0 and resume_years < job_years:
        yield "- Your resume may not clearly show enough years of experience."

    if job_edu != "not detected" and edu_rank(resume_edu) < edu_rank(job_edu):
        yield "- Your resume may not clearly show the required education level."


@require_loaded_docs
def analyze_documents(resume_document, job_document):
    resume_text = resume_document.text
    job_text = job_document.text
    resume_hard_skills = find_skill(resume_text, HARD_SKILLS)
    resume_soft_skills = find_skill(resume_text, SOFT_SKILLS)
    job_hard_skills = find_skill(job_text, HARD_SKILLS)
    job_soft_skills = find_skill(job_text, SOFT_SKILLS)
    matched_hard_skills = resume_hard_skills & job_hard_skills
    matched_soft_skills = resume_soft_skills & job_soft_skills
    missing_hard_skills = job_hard_skills - matched_hard_skills
    missing_soft_skills = job_soft_skills - matched_soft_skills
    resume_years = find_yrs_exp(resume_text)
    job_years = find_yrs_exp(job_text)
    resume_edu = find_edu_lvl(resume_text)
    job_edu = find_edu_lvl(job_text)
    hard_skills_score = calc_perc_score(matched_hard_skills, job_hard_skills)
    soft_skills_score = calc_perc_score(matched_soft_skills, job_soft_skills)
    exp_score = calc_exp_score(resume_years, job_years)
    edu_score = calc_edu_score(resume_edu, job_edu)
    overall_score = calc_ovrl_score(hard_skills_score, soft_skills_score, exp_score, edu_score)
    match_lvl = get_match_lvl(overall_score)
    skill_summary = build_skill_summary(matched_hard_skills, matched_soft_skills, missing_hard_skills, missing_soft_skills)
    recommendations = list(generate_recommendations(missing_hard_skills, missing_soft_skills, resume_years, job_years, resume_edu, job_edu))
    return AnalysisResult(
        overall_score, match_lvl, hard_skills_score, soft_skills_score, exp_score, edu_score,
        matched_hard_skills, missing_hard_skills, matched_soft_skills, missing_soft_skills,
        resume_years, job_years, resume_edu, job_edu, skill_summary, recommendations)

