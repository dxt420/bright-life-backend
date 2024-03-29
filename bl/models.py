from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from django.utils import timezone
import datetime


class MyGenericModel(models.Model):
    theFile = models.FileField(upload_to='media/files/',default='aa',blank=True)
    firebase_id_token = models.CharField(max_length=50)

class Applicant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50,blank=True)
    first_name = models.CharField(max_length=50,blank=True)
    middle_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50,blank=True)
    email = models.CharField(max_length=50,blank=True)
    dob = models.CharField(max_length=50,blank=True)
    phone = models.CharField(max_length=50,blank=True)
    other_phone = models.CharField(max_length=50,blank=True)
    status = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField(default=True)
    has_id = models.CharField(max_length=50,blank=True)
    has_cv = models.CharField(max_length=50,blank=True)
    has_rec = models.CharField(max_length=50,blank=True)
    has_lc = models.CharField(max_length=50,blank=True)
    has_academics = models.CharField(max_length=50,blank=True)
 

    def __str__(self):
        return self.first_name


class Identity(models.Model):
        # user = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    user_id = models.CharField(max_length=50,blank=True)
    nid_number = models.CharField(max_length=50,blank=True)
    passport_number = models.CharField(max_length=50,blank=True)
    nid_front = models.FileField(upload_to='media/files/',default='aa',blank=True)
    nid_back = models.FileField(upload_to='media/files/',default='aa',blank=True)
    passport_copy = models.FileField(upload_to='media/files/',default='aa',blank=True)






