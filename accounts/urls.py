from django.conf.urls import url

from accounts.views import sign_out, sign_in, UserLoginView

urlpatterns = [
    url(r'^logout/$', sign_out, name='logout'),
    url(r'^login/$', sign_in, name='login'),
    url(r'^api/login/$', UserLoginView.as_view()),
]
