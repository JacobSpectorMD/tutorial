from django.conf.urls import url

import pathologists.views as views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^profiles/', views.profiles, name='profiles')
]