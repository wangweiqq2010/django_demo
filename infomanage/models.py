# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Human(models.Model):
    name = models.CharField(max_length=50)
    GENDER_CHOICE = ((u'M', u'Male'), (u'F', u'Female'),)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICE, null=True)

    class Meta:
        abstract = True


class Teacher(Human):
    course = models.CharField(max_length=100)
    age = models.IntegerField()
    join_date = models.DateField(null=True)
    email = models.EmailField(null=True)
    introduction = models.TextField(null=True)

    class Meta:
        db_table = 'teacher'
        get_latest_by = 'join_date'


class Student(Human):
    grade = models.IntegerField()
    s_class = models.CharField(max_length=50)
    math = models.IntegerField(default=90)

    class Meta:
        db_table = 'student'

    # def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
    #     return self.name


class Math(models.Model):
    student = models.CharField(max_length=50)
    score = models.IntegerField()
    teacher = models.CharField(max_length=50)
    date = models.DateField(null=True)

    class Meta:
        db_table = 'math'
        ordering = ['-score']
