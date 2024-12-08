from django.db import models
from django.core.exceptions import ValidationError
import os

# Custom Validator to allow only PDF files
def validate_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')

class Resume(models.Model):
    file_path = models.FileField(upload_to='resumes/', validators=[validate_pdf])
    skills_extracted = models.JSONField(default=list)  
    uploaded_at = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0)  
    suggestions = models.TextField(blank=True)

    def __str__(self):
        return f"Resume {self.id} - {self.uploaded_at}"

    class Meta:
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

