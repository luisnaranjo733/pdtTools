from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '<Role: %s>' % self.name


class UserStatus(models.Model):
    userID = models.ForeignKey(User)
    isAlumni = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    def __str__(self):
        return '<UserStatus: %d>' % (self.userID.first_name)


class Quarter(models.Model):
    SEASONS = (
        ('Aut', 'Autumn'),
        ('Win', 'Winter'),
        ('Spr', 'Spring'),
        ('Sum', 'Summer')
    )

    season = models.CharField(max_length=10, choices=SEASONS)
    year = models.IntegerField()

    def __str__(self):
        return '<Season: %s %d>' % (self.season, self.year)


class Quarter_UserStatus(models.Model):
    quarterID =  models.ForeignKey(Quarter)
    userStatusID = models.ForeignKey(UserStatus)

    def __str__(self):
        return '<Quarter_UserStatus: %d, %d>' % (self.quarterID.pk, self.userStatusID.pk)


class Room(models.Model):
    capacity = models.IntegerField()
    isInhabitable = models.BooleanField('Livable?')

    def __str__(self):
        return '<Room: %d>' % self.pk


class KitchenDuty(models.Model):
    date = models.DateField()

    def __str__(self):
        return '<KitchenDuty: %r' % self.date


class User_KitchenDuty(models.Model):
    userID = models.ForeignKey(User)
    kitchenDutyID = models.ForeignKey(KitchenDuty)

    def  __str__(self):
        return '<User_KitchenDuty: %d, %d>' % (self.userID.pk, self.kitchenDutyID.pk)


class Day(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return '<Day: %s' % self.name


class Chore(models.Model):
    checker = models.ForeignKey(User, null=True)

    name = models.CharField(max_length=20)
    description =  models.CharField(max_length=255)
    timeDue = models.TimeField()

    def __str__(self):
        return '<Chore: %s>' % self.name


class Chore_Day(models.Model):
    choreID = models.ForeignKey(Chore)
    dayID = models.ForeignKey(Day)

    def __str__(self):
        return '<Chore_Day: %d>' % (self.choreID.pk, self.dayID.pk)


app_models = [
    Role,
    UserStatus,
    Quarter,
    Quarter_UserStatus,
    Room,
    KitchenDuty,
    User_KitchenDuty,
    Day,
    Chore,
    Chore_Day
]