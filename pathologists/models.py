from django.db import models


class Message(models.Model):
    user = models.ForeignKey('pathologists.Pathologist', null=True, related_name='messages', on_delete=models.SET_NULL)
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(default='', max_length=1000)


class Pathologist(models.Model):
    name = models.CharField(default='', max_length=100)
    specialty = models.CharField(default='', max_length=200)
    location = models.CharField(default='', max_length=50)