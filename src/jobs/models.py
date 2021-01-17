from django.db import models

# Create your models here.
class job(models.Model):

    JOB_TYP = [('Full Time', 'Full Time'),
               ('part Time', 'Part Time')]

    title = models.CharField(max_length=200)

    job_type = models.CharField(max_length=15,choices= JOB_TYP)
    descripctions = models.TextField(max_length=1000)
    publish = models.DateTimeField(auto_now=True)
    vancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    expernce = models.IntegerField(default=1)


    def __str__(self):
        return self.title