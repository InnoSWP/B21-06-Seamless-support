from rest_framework import serializers
from .models import Message
from .models import Answer
from .models import ChatMessage


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('user_id', 'question')


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('vol_id', 'answer')


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ('chat_id', 'from_id', 'text')
