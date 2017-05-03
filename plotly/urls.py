# This file contains all the URLs for the Plotly App
from django.conf.urls import url

from . import views

app_name = 'plotly'

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    # /plotly
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /plotly/1
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
