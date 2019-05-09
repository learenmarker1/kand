from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    tags = TaggableManager()
    #is_active_question = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #is_active_choice = models.BooleanField(default=True)

    def __str__(self):
        return self.choice_text


class Poll(models.Model):
    date_from = models.DateTimeField('date from')
    date_to = models.DateTimeField('date to')
    questions = models.ManyToManyField(Question, editable=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            super().save(*args, **kwargs)
            # Randomly pick three questions and assign them to self.next_question_ids
            self.questions.set(Question.objects.order_by('?')[:3])
        else:
            super().save(*args, **kwargs)
