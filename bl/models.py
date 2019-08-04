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
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    bank_number =  models.CharField(max_length=50)
    bank_name =  models.CharField(max_length=50)
    national_id = models.FileField(upload_to='media/files/',default='aa',blank=True)
    uace_uce_slip = models.FileField(upload_to='media/files/',default='aa',blank=True)
    cv = models.FileField(upload_to='media/files/',default='aa',blank=True)
    recommendation = models.FileField(upload_to='media/files/',default='aa',blank=True)
    lc = models.FileField(upload_to='media/files/',default='aa',blank=True)
    status = models.CharField(max_length=50,blank=True)
    applied_at = models.CharField(max_length=50,blank=True)
    applied_from = models.CharField(max_length=50,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    bank_number =  models.CharField(max_length=50)
    bank_name =  models.CharField(max_length=50)
    national_id = models.FileField(upload_to='media/files/',default='aa',blank=True)
    uace_uce_slip = models.FileField(upload_to='media/files/',default='aa',blank=True)
    cv = models.FileField(upload_to='media/files/',default='aa',blank=True)
    recommendation = models.FileField(upload_to='media/files/',default='aa',blank=True)
    lc = models.FileField(upload_to='media/files/',default='aa',blank=True)
    status = models.CharField(max_length=50,blank=True)
    applied_at = models.CharField(max_length=50,blank=True)
    applied_from = models.CharField(max_length=50,blank=True)
    valid = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name



