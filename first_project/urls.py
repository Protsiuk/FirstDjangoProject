"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import home_page
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^redactor/', include('redactor.urls')),
    # url(r'^docs/', include('rest_framework_docs.urls')),
    url(r'^docs/', include_docs_urls(title='My API title')),


    url(r'^$', home_page, name='home'),

    url(r'accounts/', include('accounts.urls')),
    url(r'publications/', include('publications.urls')),

    # url(r'^logout/$', sign_out, name='logout'),
    # url(r'^login/$', sign_in, name='login'),

    # url(r'^publications/$', publications, name='publications'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

