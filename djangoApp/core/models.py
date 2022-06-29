from django.db import models

# Create your models here.


class Message(models.Model):
    user_id = models.CharField(max_length=10)
    question = models.CharField(max_length=250)

    def __str__(self):
        return self.user_id


class Answer(models.Model):
    vol_id = models.CharField(max_length=10)
    answer = models.CharField(max_length=250)

    def __str__(self):
        return self.answer


class ChatMessage(models.Model):
    chat_id = models.CharField(max_length=10)
    from_id = models.CharField(max_length=10)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text


class Question(models.Model):
    question = models.CharField(max_length=250)

    def __str__(self):
        return self.question


class QuestionChat(models.Model):
    question_text = models.CharField(max_length=250)
    chat_id = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    vol_id = models.CharField(max_length=10)

    def __str__(self):
        return (
            self.question_text
            + ": "
            + self.chat_id
            + ": "
            + self.user_id
            + "-> "
            + self.vol_id
        )