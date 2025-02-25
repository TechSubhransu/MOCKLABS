from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import os
# Create your models here.

class StudentProfile(models.Model):
    def get_upload_path(self,filename):
        ext = filename.split('.')[:-1]
        filename = f"{self.username.first_name}_{self.username}_resume.{ext}"
        return os.path.join("student_resumes",filename)
    cources = [
        ('Python FullStack Developement','Python FullStack Developement'),
        ('Java FullStack Developement','Java FullStack Developement'),
        ('MERN FullStack Developement','MERN FullStack Developement'),
        ('FullStack Testing','FullStack Testing')
    ]
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pno = models.CharField(max_length=50)
    add = models.CharField(max_length=50)
    cource = models.CharField(max_length=50,choices=cources,default='Python FullStack Developement')
    profile_pic = models.ImageField(upload_to='student_profiles/')
    resume = models.FileField(upload_to='student_resumes/',validators=[FileExtensionValidator(['pdf','docx'])]) #it will accept a list of argument
    
    def __str__(self):
        return self.username.username
    
    