from django.db import models




class Message(models.Model):
    email = models.EmailField('ایمیل',null=False,blank=False)
    title = models.CharField('موضوع',max_length=30)
    message = models.TextField('پیام',max_length=200)

    class Meta :
        verbose_name = 'پیام'
        verbose_name_plural = "پیام ها"