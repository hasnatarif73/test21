from django.db import models

class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_description = models.TextField()
class Jobs(models.Model):
    job_title = models.CharField(max_length=100)
    job_description = models.TextField()
    job_image=models.ImageField(upload_to='jobs/',max_length=250,null=True,default=None)

     # Automatically set the date when the job is created


