from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Job, Application
import os

class UserRegisterForm(UserCreationForm):
    is_employer = forms.BooleanField(
        required=False,
        label='Register as Employer',
        widget=forms.RadioSelect(choices=[(True, 'Employer'), (False, 'Applicant')])

        
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_employer']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company_name', 'location', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['resume', 'cover_letter']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5}),
        }
    
    def clean_resume(self):
        resume = self.cleaned_data.get('resume')
        if resume:
            # Validate file extension
            valid_extensions = ['.pdf', '.doc', '.docx']
            ext = os.path.splitext(resume.name)[1].lower()
            if ext not in valid_extensions:
                raise forms.ValidationError(
                    'Unsupported file format. Please upload PDF or Word documents only.'
                )
            
            # Validate file size (5MB limit)
            max_size = 5 * 1024 * 1024  # 5MB
            if resume.size > max_size:
                raise forms.ValidationError(
                    'File size exceeds the 5MB limit. Please upload a smaller file.'
                )
        else:
            raise forms.ValidationError('Resume is required.')
        return resume

    def clean_cover_letter(self):
        cover_letter = self.cleaned_data.get('cover_letter')
        if len(cover_letter) < 50:
            raise forms.ValidationError(
                'Cover letter should be at least 50 characters long.'
            )
        return cover_letter