from django.db import models

import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def get_result_dict(self):
        res = []
        for choice in self.choice_set.all():
            d = {}
            d['text'] = choice.choice_text
            d['num_votes'] = choice.votes
            if not self.votes:
                d['percentage'] = 0
            else:
                d['percentage'] = choice.votes / self.votes * 100
                res.append(d)
        return res

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

    def __str__(self):
        return self.choice_text
