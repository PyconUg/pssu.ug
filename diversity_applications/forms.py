from django import forms
from django.core.exceptions import ValidationError
from datetime import date

from .models import Application
from .constants import INTEREST_CHOICES


INPUT_CLASS = (
    "block w-full rounded-lg border border-slate-300 bg-white px-3.5 py-2.5 "
    "text-sm text-slate-900 placeholder:text-slate-400 shadow-sm "
    "focus:border-sky-500 focus:outline-none focus:ring-2 focus:ring-sky-500/30 "
    "transition"
)

SELECT_CLASS = (
    "block w-full rounded-lg border border-slate-300 bg-white px-3.5 py-2.5 pr-10 "
    "text-sm text-slate-900 shadow-sm appearance-none "
    "bg-[url('data:image/svg+xml;charset=utf-8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20fill%3D%22none%22%20viewBox%3D%220%200%2020%2020%22%20stroke%3D%22%2364748b%22%3E%3Cpath%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%20stroke-width%3D%221.5%22%20d%3D%22M6%208l4%204%204-4%22%2F%3E%3C%2Fsvg%3E')] "
    "bg-no-repeat bg-[right_0.75rem_center] bg-[length:1.25rem_1.25rem] "
    "focus:border-sky-500 focus:outline-none focus:ring-2 focus:ring-sky-500/30 "
    "transition"
)

TEXTAREA_CLASS = INPUT_CLASS + " min-h-[110px] resize-y leading-relaxed"

CHECKBOX_CLASS = (
    "h-4 w-4 rounded border-slate-300 text-sky-600 "
    "focus:ring-2 focus:ring-sky-500/40 focus:ring-offset-0 cursor-pointer"
)


class ApplicationForm(forms.ModelForm):
    """Diversity application form with validation and Tailwind-styled widgets."""

    interests = forms.MultipleChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        help_text="Select all areas that interest you",
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
            'additional_notes',
        ]
        widgets = {
            'country': forms.Select(attrs={'class': SELECT_CLASS}),
            'full_name': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Your full name',
                'autocomplete': 'name',
            }),
            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'your.email@example.com',
                'autocomplete': 'email',
            }),
            'phone': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': '+256 700 000 000',
                'autocomplete': 'tel',
            }),
            'city': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Your city',
                'autocomplete': 'address-level2',
            }),
            'dob': forms.DateInput(attrs={
                'class': INPUT_CLASS,
                'type': 'date',
            }),
            'is_18': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASS}),
            'status': forms.Select(attrs={'class': SELECT_CLASS}),
            'field': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'e.g., Computer Science, Software Development',
            }),
            'python_level': forms.Select(attrs={'class': SELECT_CLASS}),
            'python_duration': forms.Select(attrs={'class': SELECT_CLASS}),
            'why_attend': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 4,
                'placeholder': 'Tell us why you want to attend...',
            }),
            'hope_to_gain': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 4,
                'placeholder': 'What skills, knowledge, or connections are you looking for?',
            }),
            'community': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 3,
                'placeholder': 'Optional: describe your involvement in tech communities',
            }),
            'contributions': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 3,
                'placeholder': 'Optional: open source, mentoring, organizing events, etc.',
            }),
            'knowledge_sharing': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 3,
                'placeholder': 'Optional: blogging, teaching, talks, etc.',
            }),
            'attend_all': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASS}),
            'represent_professionally': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASS}),
            'share_publicly': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASS}),
            'represent_how': forms.TextInput(attrs={
                'class': INPUT_CLASS,
                'placeholder': 'Optional: social media, blog, presentations, etc.',
            }),
            'has_national_id': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASS}),
            'has_passport': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASS}),
            'can_travel': forms.CheckboxInput(attrs={'class': CHECKBOX_CLASS}),
            'financial_support': forms.Select(attrs={'class': SELECT_CLASS}),
            'additional_notes': forms.Textarea(attrs={
                'class': TEXTAREA_CLASS,
                'rows': 3,
                'placeholder': 'Optional: anything else you want us to know',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['interests'].widget.attrs.update({'class': CHECKBOX_CLASS})

    def clean(self):
        cleaned_data = super().clean()

        dob = cleaned_data.get('dob')
        is_18 = cleaned_data.get('is_18')

        if dob:
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 18:
                raise ValidationError("You must be 18 years or older to apply.")

        if not is_18:
            raise ValidationError("You must confirm that you are 18 years or older.")

        if not cleaned_data.get('attend_all'):
            raise ValidationError("You must confirm your ability to attend all days.")
        if not cleaned_data.get('represent_professionally'):
            raise ValidationError("You must agree to represent PyCon Uganda professionally.")
        if not cleaned_data.get('share_publicly'):
            raise ValidationError("You must agree to share your experience publicly.")

        if not cleaned_data.get('has_national_id') and not cleaned_data.get('has_passport'):
            raise ValidationError("You must have either a national ID or passport.")

        return cleaned_data

    def clean_interests(self):
        interests = self.cleaned_data.get('interests')
        if not interests:
            raise ValidationError("Please select at least one area of interest.")
        return ', '.join(interests)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
