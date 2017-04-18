from django.conf.urls import url

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home_page, sign_out, sign_in
from publications.views import publications

urlpatterns = [
                  url(r'^logout/$', sign_out, name='logout'),
                  url(r'^login/$', sign_in, name='login'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

