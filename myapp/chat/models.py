from django.db import models

# Create your models here.


class Conversation(models.Model):

    conv_name = models.CharField(max_length=200)

    # pub_date = models.DateTimeField('date published')


class Message(models.Model):

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)
