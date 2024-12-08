from django.db import models

# job_descriptions/models.py

from django.db import models
from django.core.exceptions import ValidationError

def validate_pdf(value):
    """Custom validator to only accept PDF files."""
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')

class JobDescription(models.Model):
    """Model to store uploaded job description files."""
    file_path = models.CharField(max_length=255)  # Path to the uploaded PDF
    skills_required = models.JSONField()  # Extracted required skills as a list or dictionary
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Auto-added at the time of upload

    def __str__(self):
        return f"Job Description {self.id}"

