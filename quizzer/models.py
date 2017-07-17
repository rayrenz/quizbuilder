from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from picklefield.fields import PickledObjectField


STATUS = [
    ('draft', 'Draft'),
    ('published', 'Published'),
]


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Quiz(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    expiration = models.DateField(blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=10, default='draft')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'quizzes'


class Question(models.Model):
    text = models.CharField(max_length=500, unique=True)
    quiz = models.ForeignKey(Quiz, null=True)

    def __str__(self):
        return self.text


class Choice(models.Model):
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question)

    def __str__(self):
        return self.text


class QuizSession(models.Model):
    date_taken = models.DateTimeField()
    quiz = models.ForeignKey(Quiz)
    score = models.IntegerField()
    answers = PickledObjectField()
    user = models.ForeignKey(User)

    def __str__(self):
        return 'Quiz ' + self.quiz.title + ' answered by ' + self.user.username

    def get_absolute_url(self):
        return reverse('quizzer:session_results', args=[self.quiz.id, self.id])