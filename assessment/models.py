# Model for the Assessment App courses.
# Consists of three models: Course, Test and StudentAnswer

from django.db import models
from django.core.urlresolvers import reverse

class Course(models.Model):
    level = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    course_title = models.CharField(max_length=50)
    course_image = models.CharField(max_length=250)

    def __str__(self):
        return self.level + '-' + self.subject

class Test(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    test_title = models.CharField(max_length=50)
    test_image = models.CharField(max_length=250)
    question_1= models.CharField(max_length=1000)
    question_2= models.CharField(max_length=1000)

    def get_absolute_url(self):
      return reverse('assessment:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.test_title

class StudentAnswer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    answer_1= models.CharField(max_length=1000)
    answer_2= models.CharField(max_length=1000)
    student_name=models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('assessment:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.student_name
