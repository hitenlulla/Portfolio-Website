from django.db import models

# Create your models here.
class ProjectModel(models.Model):
    img = models.FileField(upload_to ='project_images/', blank = False)
    title = models.CharField(max_length = 50)
    info = models.CharField(max_length = 200)
    day = models.CharField(max_length = 3)
    month = models.CharField(max_length = 10)
    year = models.CharField(max_length = 5)
    # Technologies
    html = models.BooleanField(default= False)
    css = models.BooleanField(default= False)
    javascript = models.BooleanField(default= False)
    python = models.BooleanField(default= False)
    database = models.BooleanField(default= False)
    django = models.BooleanField(default= False)
    tensorflow = models.BooleanField(default= False)
    react = models.BooleanField(default= False)
    github_link = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

class ContactModel(models.Model):
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 40)
    idea = models.CharField(max_length= 200)

    def __str__(self):
        return self.email + " --> " + self.idea