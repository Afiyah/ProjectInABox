# Model for the Plotly App courses, detailing the level,
# subject, course title, course image for each course

from django.db import models

class course(models.Model):

    level = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    course_title = models.CharField(max_length=250)
    course_image = models.CharField(max_length=250)

    def __str__(self):
        return self.level + ' - ' + self.subject



