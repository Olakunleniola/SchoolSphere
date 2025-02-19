from django import forms
from .models import School
from django.contrib.auth import get_user_model

User = get_user_model()

class SchoolSignupForm(forms.ModelForm):
    admin_email = forms.EmailField(required=True, label="Admin Email")
    admin_password = forms.CharField(widget=forms.PasswordInput, required=True, label="Admin Password")

    class Meta:
        model = School
        fields = ['name', 'about', 'admin_email', 'admin_password']

    def clean_admin_email(self):
        admin_email = self.cleaned_data.get('admin_email')
        if User.objects.filter(email=admin_email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return admin_email