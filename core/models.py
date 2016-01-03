from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return '<Role: %s>' % self.name


class Room(models.Model):
    capacity = models.IntegerField()
    isInhabitable = models.BooleanField('Livable?', default=True)

    def __str__(self):
        return '<Room: %d>' % self.pk


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
        return '<Quarter: %s>' % self.handle()

    def handle(self):
        return '%s%d' % (self.season, self.year)


class User_Quarter(models.Model):
    userID = models.ForeignKey(User)
    quarterID =  models.ForeignKey(Quarter)
    roomID = models.ForeignKey(Room)

    points = models.IntegerField('House points')
    isAlumni = models.BooleanField(default=False)

    def __str__(self):
        return '<User_Quarter: %s, %s, %d>' % (self.userID.username, self.quarterID.handle(), self.roomID.pk)


class KitchenDuty(models.Model):
    date = models.DateField()
    quarterID =  models.ForeignKey(Quarter)
    workers = models.ManyToManyField(User)

    def __str__(self):
        return '<KitchenDuty: %r' % self.date


# class User_KitchenDuty(models.Model):
#     userID = models.ForeignKey(User)
#     kitchenDutyID = models.ForeignKey(KitchenDuty)

#     def  __str__(self):
#         return '<User_KitchenDuty: %d, %d>' % (self.userID.pk, self.kitchenDutyID.pk)


class Day(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return '<Day: %s>' % self.name


class Chore(models.Model):
    checker = models.ForeignKey(User, null=True, blank=True)
    daysDue = models.ManyToManyField(Day)

    name = models.CharField(max_length=100)
    description =  models.CharField(max_length=255)
    timeDue = models.TimeField()

    def __str__(self):
        return '<Chore: %s>' % self.name


# class Chore_Day(models.Model):
#     choreID = models.ForeignKey(Chore)
#     dayID = models.ForeignKey(Day)

#     def __str__(self):
#         return '<Chore_Day: %d>' % (self.choreID.pk, self.dayID.pk)


app_models = [
    Role,
    Room,
    Quarter,
    User_Quarter,
    KitchenDuty,
    #User_KitchenDuty,
    Day,
    Chore,
    #Chore_Day
]