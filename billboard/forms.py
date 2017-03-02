from django.contrib.auth.models import User
from django import forms

class form1(forms.ModelForm):
    class Meta:
        model = User
        fields =("username", "email", "password")

        # def save(self, commit=True):
        #     user = super(UserCreationForm, self).save(commit=False)
        #     user.email = self.cleaned_data["email"]
        #     if commit:
        #         user.save()
        #     return user