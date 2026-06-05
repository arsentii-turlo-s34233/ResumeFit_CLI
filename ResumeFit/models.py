class Document:
    def __init__ (self, path, text):
        self.path = path
        self.text = text
    def is_loaded(self):
        return bool(self.text)

class AnalysisResult:
    def __init__(self, overall_score, match_lvl, hard_skills_score, soft_skills_score, exp_score,
                 edu_score, matched_hard_skills, missing_hard_skills, matched_soft_skills,
                 missing_soft_skills, resume_years, job_years, resume_edu, job_edu,skill_summary,
                 recommendations):
        self.overall_score = overall_score
        self.match_lvl = match_lvl
        self.hard_skills_score = hard_skills_score
        self.soft_skills_score = soft_skills_score
        self.exp_score = exp_score
        self.edu_score = edu_score
        self.matched_hard_skills = matched_hard_skills
        self.missing_hard_skills = missing_hard_skills
        self.matched_soft_skills = matched_soft_skills
        self.missing_soft_skills = missing_soft_skills
        self.resume_years = resume_years
        self.job_years = job_years
        self.resume_edu = resume_edu
        self.job_edu = job_edu
        self.skill_summary = skill_summary
        self.recommendations = recommendations


    def to_dict(self):
        return {
            "overall_score": round(self.overall_score, 1),
            "match_lvl": self.match_lvl,
            "hard_skills_score": round(self.hard_skills_score, 1),
            "soft_skills_score": round(self.soft_skills_score, 1),
            "experience_score": round(self.exp_score, 1),
            "education_score": round(self.edu_score, 1),
            "matched_hard_skills": sorted(self.matched_hard_skills),
            "missing_hard_skills": sorted(self.missing_hard_skills),
            "matched_soft_skills": sorted(self.matched_soft_skills),
            "missing_soft_skills": sorted(self.missing_soft_skills),
            "resume_years": self.resume_years,
            "job_years": self.job_years,
            "resume_education": self.resume_edu,
            "job_education": self.job_edu,
            "skill_summary": self.skill_summary,
            "recommendations": self.recommendations,
        }