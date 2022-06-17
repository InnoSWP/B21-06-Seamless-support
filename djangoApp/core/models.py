from django.db import models

# Create your models here.


class Message (models.Model):
    user_id = models.CharField(max_length=10)
    question = models.CharField(max_length=250)

    def __str__(self):
        return self.user_id


class Answer (models.Model):
    vol_id = models.CharField(max_length=10)
    answer = models.CharField(max_length=250)

    def __str__(self):
        return self.answer
