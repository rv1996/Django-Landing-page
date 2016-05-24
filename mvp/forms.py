from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['email', 'full_name']
        # or we can even exclude a single field if we want to keep all except one
        # exclude =['full_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, email_provider = email.split("@")
        print (email_base, email_provider)
        extension = email_provider.split('.')
        print(extension[1])
        if len(extension)>2:
            raise forms.ValidationError("Enter the global extension like '.com' not '.co.in'")

        if extension[1] != 'com':
            raise forms.ValidationError('Please enter a email with .com domain')
        print("Testing the overiding function")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        full_name = full_name.title()
        return full_name



