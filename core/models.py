from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    userID = models.OneToOneField(User, on_delete=models.CASCADE)
    bondNumber = models.IntegerField(null=True, blank=True)
    isAlumni = models.BooleanField(default=False)
    
    def __str__(self):
        name = self.userID.get_full_name()
        if self.isAlumni:
            name += ' (ALUMNI)'
        return name
  

class Quarter(models.Model):
    SEASONS = (
        ('Fall', 'Fall'),
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer')
    )

    season = models.CharField(max_length=10, choices=SEASONS)
    year = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return self.getHandle() 
        
    def getHandle(self):
        'A string representation of the season and year of the quarter'
        return '%s %d' % (self.season, self.startDate.year) 


class Member_Quarter(models.Model):
    memberID = models.ForeignKey(Member)
    quarterID =  models.ForeignKey(Quarter)

    isLiveIn = models.BooleanField(default=True)
    points = models.IntegerField('House points', default=0, blank=True)
    
    def __str__(self):
        return '%s, %s' % (self.memberID.userID.username, self.quarterID.getHandle())


class Role(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    spots = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return self.name

class Quarter_Role(models.Model):
    memberQuarterID = models.ForeignKey(Member_Quarter)
    roleID = models.ForeignKey(Role)
    
    def __str__(self):
        return "%s : %s" % (self.roleID, self.memberQuarterID)

class Member_Quarter_Role(models.Model):
    userQuarterID = models.ForeignKey(Member_Quarter)
    roleID = models.ForeignKey(Role)
    
    def __str__(self):
        return '%s, %s, %s' % (self.roleID, self.userQuarterID, self.userQuarterID.memberID)

# class Room(models.Model):
#     capacity = models.IntegerField()
#     isInhabitable = models.BooleanField('Livable?', default=True)

#     def __str__(self):
#         return '<Room: %d>' % self.pk

# class KitchenDuty(models.Model):
#     date = models.DateField()
#     quarterID =  models.ForeignKey(Quarter)
#     workers = models.ManyToManyField(User)

#     def __str__(self):
#         return '<KitchenDuty: %r' % self.date


# class User_KitchenDuty(models.Model):
#     userID = models.ForeignKey(User)
#     kitchenDutyID = models.ForeignKey(KitchenDuty)

#     def  __str__(self):
#         return '<User_KitchenDuty: %d, %d>' % (self.userID.pk, self.kitchenDutyID.pk)


# class Day(models.Model):
#     name = models.CharField(max_length=10)

#     def __str__(self):
#         return '<Day: %s>' % self.name


# class Chore(models.Model):
#     checker = models.ForeignKey(User, null=True, blank=True)
#     daysDue = models.ManyToManyField(Day)

#     name = models.CharField(max_length=100)
#     description =  models.CharField(max_length=255)
#     timeDue = models.TimeField()

#     def __str__(self):
#         return '<Chore: %s>' % self.name


# class Chore_Day(models.Model):
#     choreID = models.ForeignKey(Chore)
#     dayID = models.ForeignKey(Day)

#     def __str__(self):
#         return '<Chore_Day: %d>' % (self.choreID.pk, self.dayID.pk)


app_models = [
    Member,
    Role,
    Quarter,
    Member_Quarter,
    Member_Quarter_Role
]