from django import forms
# from accounts import


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=4, max_length=10, widget=forms.TextInput(attrs={"type": "password"}))

    # def clean(self):
    #     email = self.cleaned_data.get("email")
    #     # password = self.cleaned_data.get('password')
    #     if len(email) < 14:
    #         raise forms.ValidationError("Sorry. Please try again.")
    # # password = forms.CharField(min_length=10, max_length=20, widget=forms.TextInput(atr={"class": "password"}))
    #


