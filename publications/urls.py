"""Urls of publications in project "first_project"
"""
from django.conf.urls import url
from publications.views import publications

urlpatterns = [

    url(r'^$', publications, name='publications'),
]

