from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Quiz, Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['text', 'is_correct', 'id']


class QuestionSerializer(serializers.ModelSerializer):
    choice_set = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['text', 'quiz', 'choice_set', 'id']


class QuizSerializer(serializers.ModelSerializer):
    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Quiz
        fields = ['title', 'created', 'expiration', 'status', 'question_set', 'id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
