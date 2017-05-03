# This file contains the class-based generic and function-based views for the
# Assessment app. Each view
# is linked to a model/object and a HTML Template

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Course, Test, StudentAnswer
from .forms import TestForm, UserForm


class IndexView(generic.ListView):
    template_name='assessment/index.html'
    context_object_name = 'all_courses'

    def get_queryset(self):
        return Course.objects.all()

class DetailView(generic.DetailView):
    model = Course
    template_name = 'assessment/detail.html'


def CourseTestDetailsView(request, *args, **kwargs):
    test = Test.objects.get(id=kwargs['pk'])
    form = TestForm(request.POST or None)
    context = {"Test": test, "Form": form}
    if form.is_valid():
        obj_test = test
        obj_student_name = form.cleaned_data.get("student_name")
        obj_answer_1 = form.cleaned_data.get("answer_1")
        obj_answer_2 = form.cleaned_data.get("answer_2")
        new_studentanswer, created = StudentAnswer.objects.get_or_create(
            test = obj_test,
            student_name = obj_student_name,
            answer_1 = obj_answer_1,
            answer_2 = obj_answer_2
        )
        if created:
            return redirect('assessment:index')
    print(form)
    return render(request, 'assessment/test_form.html', context)


def CourseTestIndexView(request, *args, **kwargs):
    course = Course.objects.get(id=kwargs['pk'])
    context = {"Course": course}
    return render(request,'assessment/Testindex.html', context)

class UserFormView(View):
    form_class = UserForm
    template_name = 'assessment/registration_form.html'

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #Cleaned (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns Users objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('assessment:index')

        return render(request, self.template_name, {'form': form})



