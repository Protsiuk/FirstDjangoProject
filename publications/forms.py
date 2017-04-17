from django import forms


class PublicationForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)
    image = forms.FileField()
