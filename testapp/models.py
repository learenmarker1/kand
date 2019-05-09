from django.db import models

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #is_active_question = models.BooleanField(default=False)

    def get_result_dict(self):
        res = []
        for choice in self.choice_set.all():
            d = {}
            d['text'] = choice.choice_text
            d['num_votes'] = choice.votes
            if not choice.votes:
                d['percentage'] = 0
            else:
                d['percentage'] = choice.votes / self.num_votes * 100
                res.append(d)
        return res

    @property
    def num_votes(self):
        votes_total = 0
        for choice in self.choice_set.all():
            votes_total += choice.votes
        return votes_total

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
    questions = models.ManyToManyField(Question, editable=False)

    def save(self, *args, **kwargs):
        if self.id is None:
            super().save(*args, **kwargs)
            # Randomly pick three questions and assign them to self.next_question_ids
            self.questions.set(Question.objects.order_by('?')[:3])
        else:
            super().save(*args, **kwargs)
