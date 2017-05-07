from django.contrib import admin
from django import forms

from publications.models import Publication, PublicationLike, PublicationComment
from redactor.widgets import RedactorEditor


class PublicationAdminForm(forms.ModelForm):
    class Meta:
        model = Publication
        widgets = {
           'body': RedactorEditor(),
        }
        fields = ("title", "body", "image", "author")

class PublicationAdmin(admin.ModelAdmin):
    form = PublicationAdminForm

# Register your models here.
admin.site.register(PublicationLike)
admin.site.register(PublicationComment)
admin.site.register(Publication, PublicationAdmin)
