from django.db import models
from django.db.models import Max, Avg

'''
Room
----
Field: roomNumber
Field: isImproved
pointStrength()
    * pivot = occupant from getOccupants() with the highest house points
    * multiplier = 0. 6 if isImproved else 0.2
    * return pivot.points * multiplier + points
    * next quarter: return average of all occupants house points
getOccupants()
    * room.person_set.all()
takeImprovement()
    * isImproved = false
giveImprovement()
    * isImproved = true
evictOccupant()
    * takeImprovement()
    * occupant = None
    * isOccupied - false
'''

class Room(models.Model):
    roomNumberField = models.IntegerField(default=-1)
    isImprovedField = models.BooleanField(default=False)

    def getOccupants(self):
        '''Gets this room's current occupants.
        
        Returns a QuerySet of Person objects that have ForeignKeys
        that are mapped to this Room.
        '''
        return self.person_set.all()

    def isOccupied(self):
        '''Tells whether or not this room currently has any occupants.'''
        return len(self.getOccupants()) > 0

    def evictOccupants(self):
        '''Evicts all occupants of this room (if any)'''
        for occupant in self.getOccupants():
            occupant.setRoom(None)

    def strength(self):
        '''Calculates the overall "strength" of this room.
        
        This is a generalized method.
        Modify to return self.maxStrength() or self.avgStrength()
        depending on desired behaviour.
        '''
        return self.maxStrength()

    def maxStrength(self):
        '''Calculates strength by using the max occupant's house points'''
        occupants = self.getOccupants()
        if occupants:
            return occupants.aggregate(Max('pointsField'))['pointsField__max']
        else:
            return 0

    def avgStrength(self):
        '''Calculates strength by using the avg of all occupant's house points'''
        occupants = self.getOccupants()
        if occupants:
            return occupants.aggregate(Avg('pointsField'))['pointsField__avg']
        else:
            return 0

    def __unicode__(self):
        return "Room %d" % self.roomNumberField
        
    # Low level Setter/Getter methods below
        
    def getRoomNumber(self):
        return roomNumberField
        
    def setRoomNumber(self, roomNumber):
        self.roomNumberField = roomNumber
        self.save()
        
    def isImproved(self):
        return isImprovedField
        
    def setIsImproved(self, isImproved):
        self.isImprovedField = isImproved
        self.save()

class Chore(models.Model):
    titleField = models.CharField(max_length=80)
    descriptionField = models.TextField()
    workerQuotaField = models.IntegerField(default=0) # 2 for foyer
	
    def getWorkers(self):
        '''Returns all workers that currently have this chore.'''
        return self.person_set.all()

    def workersMissing(self):
        '''Returns the number of workers needed to make this chore "full"'''
        nWorkers = len(self.getWorkers())
        return abs(self.getNumWorkerQuota() - nWorkers)
        
    def __unicode__(self):
        return self.getTitle()
        
    # Low level Setter/Getter methods below
		
    def getTitle(self):
        return self.titleField
        
    def getDescription(self):
        return self.descriptionField
        
    def getNumWorkerQuota(self):
        return self.workerQuotaField

    def setTitle(self, title):
        self.titleField = title
        self.save()
        
    def setDescription(description):
        self.descriptionField = description
        self.save()
        
    def setWorkerQuota(self, quota):
        self.workerQuotaField = quota
        self.save()


class Person(models.Model):
    nameField = models.CharField(max_length=80)
    isLiveInField = models.BooleanField(default=True)
    roomField = models.ForeignKey(Room, blank=True, null=True)
    choreField = models.ForeignKey(Chore, blank=True, null=True)
    pointsField = models.IntegerField(default=0)

    def canTakeRoom(self, room, mates=[]):
        ''' Tells if a list of room mates can take a particular room

            Positional Arguments:
            room -- The room to be potentially taken

            Keyword Arguments:
            mates --  a List of Person objects that want to see if
                      they can take the room. If this argument is
                      omitted, this method assumes that this person is 
                      trying to take this room as a single.

            If the room is not occupied, this method returns True

            If there is more than one person trying to take a room,
            the max value of the potential roommates is used
        '''
        if len(mates) == 0:
            mates.append(self)
        if room.isOccupied():
            points = [mate.getPoints() for mate in mates]
            strength = sum(points) / len(mates) # Average of room mate points
            strength = max(points) # Highest room mate point value
            return strength > room.strength()
        else:
            return True

    def takeRoom(self, room, mates=[]):
        ''' Takes a room for a list of room mates

            Positional Arguments:
            room -- The room to be potentially taken (Room object)

            Keyword Arguments:
            mates --  a List of Person objects that want to take
                      the room. If this argument is omitted,
                      this method assumes that this person is
                      taking this room as a single.

            Pre-condition: canTakeRoom(room, mates) must be True
                           raises Exception if not
        '''
        if not self.canTakeRoom(room, mates): # precondition
            raise Exception("Not enough points to take this room!")
        if len(mates) == 0:
            mates.append(self)
        for mate in mates:
            mate.setRoom(room)

    def canClaimChore(chore):
        ''' Tells if Person can claim a particular chore

            Positional Arguments:
            chore -- The desired chore (Chore object)

            If the chore isn't full yet, return True
        '''
        pass

    def claimChore(chore):
        ''' Takes a chore

            Positional Arguments:
            chore -- The desired chore (Chore object)

            Pre-condition: canTakeChore(chore) must be True
                           raises Exception if not
        '''
        if not self.canTakeChore(chore):
            raise Exception("This chore can't be taken!")
        self.setChore(chore)

    def __unicode__(self):
        return self.getName()

    # Low level Setter/Getter methods below

    def setName(self, name):
        self.nameField = name
        self.save()

    def setLiveIn(self, livesIn):
        self.isLiveInField = livesIn
        self.save()

    def setRoom(self, room):
        self.roomField = room
        self.save()

    def setChore(self, chore):
        self.choreField = chore
        self.save()

    def setPoints(self, points):
        self.pointsField = points
        self.save()

    def getName(self):
        return self.nameField

    def isLiveIn(self):
        return self.isLiveInField

    def getRoom(self):
        return self.roomField

    def getChore(self):
        return self.choreField

    def getPoints(self):
        return float(self.pointsField)

'''
Person
------
Field: name
Field: isLiveIn
Field: room
Field: points
occupyRoom(room)
    * Throw exception if !canOccupyRoom(room)
canOccupyRoom(room)
    * if isLiveIn: Throw exception
    * return points > room.strength()
person.room_set.all()


'''

'''
Questions

If people are going to double/triple together, is their "point strength" the highest one of them, or their average?
Is this value the same when they are defending their room?
Are room improvements awarded to the room, or the individual(s) in the room?
    - If room mate A improves the room for fall quarter, and picks another room for winter quarter,
      does room mate B keep the defensive point strength boost from the improvement?
    - Best to ignore this case?



'''
