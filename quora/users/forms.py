from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    

    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
