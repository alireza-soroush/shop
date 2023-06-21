from django.db import models




class Message(models.Model):
    email = models.EmailField(null=False,blank=False)
    title = models.CharField(max_length=30)
    message = models.TextField(max_length=200)