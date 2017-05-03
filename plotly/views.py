# This file contains the class-based generic views for the plotly app. Each view
# is linked to a model/object and a HTML Template

from django.views import generic
from .models import course

class IndexView(generic.ListView):
    template_name='plotly/index.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return course.objects.all()

class DetailView(generic.DetailView):
    model = course
    template_name = 'plotly/detail.html'






