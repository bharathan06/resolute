from django.db import models
from resume.models import Resume
from job_desc.models import JobDescription

class SkillMatchResult(models.Model):
    matched_skills = models.JSONField()
    unmatched_skills = models.JSONField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    analysis_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Skill Match Result for {self.resume} and {self.job_description}"

class History(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    job_description = models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    rating = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for {self.resume} and {self.job_description} - Rating: {self.rating}"
