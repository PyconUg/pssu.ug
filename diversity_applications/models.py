from django.db import models
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone
from datetime import date

from .constants import (
    COUNTRIES,
    STATUS_CHOICES,
    PYTHON_LEVEL_CHOICES,
    PYTHON_DURATION_CHOICES,
    INTEREST_CHOICES,
    FINANCIAL_SUPPORT_CHOICES,
    APPLICATION_STATUS_CHOICES,
)


class Application(models.Model):
    country = models.CharField(
        max_length=50,
        choices=COUNTRIES,
        help_text="Country of residence"
    )
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    dob = models.DateField(verbose_name="Date of Birth")
    is_18 = models.BooleanField(
        verbose_name="I confirm that I am 18 years or older",
        help_text="Applicant must be 18 or older"
    )

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        help_text="Current employment/student status"
    )
    field = models.CharField(
        max_length=255,
        verbose_name="Field of study or work",
        help_text="Your field of study or professional field"
    )
    python_level = models.CharField(
        max_length=50,
        choices=PYTHON_LEVEL_CHOICES,
        verbose_name="Python proficiency level"
    )
    python_duration = models.CharField(
        max_length=50,
        choices=PYTHON_DURATION_CHOICES,
        verbose_name="How long have you been using Python?"
    )

    why_attend = models.TextField(
        verbose_name="Why do you want to attend PyCon Uganda?",
        help_text="Tell us about your motivation for attending"
    )
    hope_to_gain = models.TextField(
        verbose_name="What do you hope to gain from the conference?",
        help_text="What skills, knowledge, or connections are you looking for?"
    )
    interests = models.CharField(
        max_length=500,
        verbose_name="Areas of interest (comma-separated)",
        help_text="e.g., AI/ML, Web Development, Data Science, Open Source, DevOps/Cloud"
    )

    community = models.TextField(
        blank=True,
        null=True,
        verbose_name="Are you part of any community or organization?",
        help_text="Optional: Tell us about your involvement in tech communities"
    )
    contributions = models.TextField(
        blank=True,
        null=True,
        verbose_name="How have you contributed to the tech community?",
        help_text="Optional: Open source, mentoring, organizing events, etc."
    )
    knowledge_sharing = models.TextField(
        blank=True,
        null=True,
        verbose_name="How do you share knowledge with others?",
        help_text="Optional: Blogging, teaching, talks, etc."
    )

    attend_all = models.BooleanField(
        verbose_name="I can attend all days of the conference",
        help_text="Confirm your commitment to attend the full conference"
    )
    represent_professionally = models.BooleanField(
        verbose_name="I will represent PyCon Uganda professionally",
        help_text="Agree to represent the event and community professionally"
    )
    share_publicly = models.BooleanField(
        verbose_name="I agree to share my experience publicly",
        help_text="Permission to share your experience on social media, etc."
    )
    represent_how = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="How will you represent the event?",
        help_text="Optional: Social media, blog posts, presentations, etc."
    )

    has_national_id = models.BooleanField(
        verbose_name="I have a valid national ID",
        help_text="Confirm you have a national ID"
    )
    has_passport = models.BooleanField(
        verbose_name="I have a valid passport",
        help_text="Confirm you have a valid passport"
    )
    can_travel = models.BooleanField(
        verbose_name="I can obtain travel documents if needed",
        help_text="Confirm you can get travel documents for attending"
    )

    financial_support = models.CharField(
        max_length=100,
        choices=FINANCIAL_SUPPORT_CHOICES,
        verbose_name="Do you need financial support?",
        help_text="Select the type of support you may need"
    )

    anything_else = models.TextField(
        blank=True,
        null=True,
        verbose_name="Anything else you'd like us to know?",
        help_text="Optional: Additional information about yourself"
    )

    application_status = models.CharField(
        max_length=50,
        choices=APPLICATION_STATUS_CHOICES,
        default='submitted',
        verbose_name="Application Status",
        help_text="Tracks the review status of the application"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Application"
        verbose_name_plural = "Applications"
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['application_status']),
            models.Index(fields=['email']),
        ]

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    def is_age_eligible(self):
        if not self.dob:
            return False
        today = date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age >= 18

    def get_interests_list(self):
        if self.interests:
            return [i.strip() for i in self.interests.split(',')]
        return []
