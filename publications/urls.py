"""Urls of publications in project "first_project"
"""
from django.conf.urls import url
from publications.views import publications, single_publication, like_single_publication, publications_as_json

urlpatterns = [

    url(r'^$', publications, name='publications'),
    url(r'^(?P<publication_id>[\d]+)$', single_publication, name='single_publication'),
    url(r'^(?P<publication_id>[\d]+)/like$', like_single_publication, name='like_single_publication'),
    url(r'^api/(?P<publication_id>[\d]+)$', publications_as_json, name='publications_as_json'),
]

