from django.conf.urls import url
from login_auth import views
from django.conf import settings


urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),

]