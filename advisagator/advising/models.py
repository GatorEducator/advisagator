""" This file is used to create all the models for Django """
from django.db import models


class Question(models.Model):
    """Define a model for questions"""

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    """Define a model for choices"""

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
