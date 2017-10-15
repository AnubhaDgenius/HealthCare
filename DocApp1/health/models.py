from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
def validate_img(upload): 
      import os
      ext = os.path.splitext(upload.name)[1]
      if not ext in ['.jpg', ".png"]:
        raise ValidationError(u'File type not supported!')    
      if upload.size > 1024*500:
        raise ValidationError(u'File too big!')

class Disease(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Notice(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    cr_date = models.DateField(auto_now=True)
    notice_details=models.FileField(upload_to = "doc\\", null=True, blank=True)
    
    def __str__(self):
        return self.subject

class Patient(models.Model):
    p_name = models.CharField(max_length=200, null=True)
    p_age=models.CharField(max_length=2,null=True)
    p_addr = models.TextField()
    phone_number = PhoneNumberField()
    p_email = models.EmailField()
    p_img = models.ImageField(upload_to = "images\\", validators=[validate_img], null=True)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.p_name
    
class Ques(models.Model):
    question = models.TextField(null=True) 
    answer = models.TextField(null=True) 
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    notice=models.ForeignKey(Notice, on_delete=models.CASCADE)
    def __str__(self):
        return self.question 
       
class Book(models.Model):
     date=models.DateField()
     time=models.TimeField()
     description=models.TextField(null=True)
     def __str__(self):
        return self.date
       
