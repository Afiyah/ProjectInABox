# This file contains all the URLs for the Assessment App

from django.conf.urls import url
from . import views

app_name = 'assessment'

urlpatterns = [
    # /assessment/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /assessment/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /assessment/course_id
    url(r'^(?P<pk>[0-9]+)/$', views.CourseTestIndexView, name='detail'),

    # /assessment/test/test_id/complete
    url(r'test/(?P<pk>[0-9]+)/complete/$', views.CourseTestDetailsView, name='test-complete'),

]
