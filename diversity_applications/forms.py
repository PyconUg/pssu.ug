from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import date

from .models import Application
from .constants import INTEREST_CHOICES


class ApplicationForm(forms.ModelForm):
    """
    Form for diversity applications with validation.
    """

    interests = forms.MultipleChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Select all areas that interest you"
    )

    class Meta:
        model = Application
        fields = [
            'country',
            'full_name',
            'email',
            'phone',
            'city',
            'dob',
            'is_18',
            'status',
            'field',
            'python_level',
            'python_duration',
            'why_attend',
            'hope_to_gain',
            'interests',
            'community',
            'contributions',
            'knowledge_sharing',
            'attend_all',
            'represent_professionally',
            'share_publicly',
            'represent_how',
            'has_national_id',
            'has_passport',
            'can_travel',
            'financial_support',
            'anything_else',
        ]
        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+256 or local format',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your city',
            }),
            'dob': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'is_18': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'field': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Computer Science, Software Development, etc.',
            }),
            'python_level': forms.Select(attrs={'class': 'form-control'}),
            'python_duration': forms.Select(attrs={'class': 'form-control'}),
            'why_attend': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us why you want to attend...',
            }),
            'hope_to_gain': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'What skills, knowledge, or connections are you looking for?',
            }),
            'community': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional: Describe your involvement in tech communities',
            }),
            'contributions': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional: Open source, mentoring, organizing events, etc.',
            }),
            'knowledge_sharing': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional: Blogging, teaching, talks, etc.',
            }),
            'attend_all': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'represent_professionally': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'share_publicly': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'represent_how': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional: Social media, blog, presentations, etc.',
            }),
            'has_national_id': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_passport': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'can_travel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'financial_support': forms.Select(attrs={'class': 'form-control'}),
            'anything_else': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Optional: Tell us anything else about yourself',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        # Validate age
        dob = cleaned_data.get('dob')
        is_18 = cleaned_data.get('is_18')

        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                raise ValidationError("You must be 18 years or older to apply.")

        if not is_18:
            raise ValidationError("You must confirm that you are 18 years or older.")

        # Validate commitment checkboxes
        if not cleaned_data.get('attend_all'):
            raise ValidationError("You must confirm your ability to attend all days.")
        if not cleaned_data.get('represent_professionally'):
            raise ValidationError("You must agree to represent PyCon Uganda professionally.")
        if not cleaned_data.get('share_publicly'):
            raise ValidationError("You must agree to share your experience publicly.")

        # Validate travel documents
        if not cleaned_data.get('has_national_id') and not cleaned_data.get('has_passport'):
            raise ValidationError("You must have either a national ID or passport.")

        return cleaned_data

    def clean_interests(self):
        """Validate interests field."""
        interests = self.cleaned_data.get('interests')
        if not interests:
            raise ValidationError("Please select at least one area of interest.")
        # Convert list to comma-separated string for storage
        return ', '.join(interests)

    def save(self, commit=True):
        """Save the form and ensure interests are properly formatted."""
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
