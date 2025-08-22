from django import forms
from .models import Profile
LANG_CHOICES = [
    ('', 'English (Default)'),
    ('hindi', 'Hindi'),
    ('tamil', 'Tamil'),
    ('bengali', 'Bengali'),
    ('gujarati', 'Gujarati'),
    ('telugu', 'Telugu'),
    ('punjabi', 'Punjabi'),
    ('kannada', 'Kannada'),
    ('malayalam', 'Malayalam'),
    ('marathi', 'Marathi'),
    ('urdu', 'Urdu'),
]

class DocumentForm(forms.Form):
    document = forms.FileField()
    language = forms.ChoiceField(choices=LANG_CHOICES, required=False)


class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']
