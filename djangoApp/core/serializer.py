from rest_framework import serializers

from .models import Answer, ChatMessage, Message, Question, QuestionChat


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("user_id", "question")


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("vol_id", "answer")


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ("chat_id", "from_id", "text")


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "question"


class QuestionChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionChat
        fields = ("question_text", "chat_id", "user_id", "vol_id")
