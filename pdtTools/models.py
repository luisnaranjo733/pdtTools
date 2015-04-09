from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Float, Boolean
from sqlalchemy.orm import relationship, backref
from werkzeug import generate_password_hash, check_password_hash
from pdtTools.database import Base, db_session


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    password_hash = Column(String(54))
    bond_number = Column(Integer, unique=True)
    house_points = Column(Float)
    is_live_in = Column(Boolean)
    is_admin = Column(Boolean)
    has_selected = Column(Boolean)
    room_id = Column(Integer, ForeignKey('rooms.number'))
    #chore = Column(Chore)

    room = relationship("Room", backref=backref('users', order_by=id))

    def __init__(self, **kwargs):
        self.is_admin = False  # can be overridden in kwargs
        for attr in kwargs:
            if attr == 'password_hash':
                self.setPassword(kwargs[attr])  # store password as a hash
            else:
                setattr(self, attr, kwargs[attr])  # normal attributes

    def __repr__(self):
        return '<User %r>' % (self.name)
    
    def setPassword(self, password):
        'Hash a given password and store it'
        self.password_hash = generate_password_hash(password)
        
    def checkPassword(self, password):
        'Check the given password (hash) against the stored hash'
        return check_password_hash(self.password_hash, password)
        
    @staticmethod
    def getSelectionQueue():
        '''Gets the queue of people who have not selected yet
        
        Ordered by descending house points'''
        pass
        
    @staticmethod
    def getLiveIns():
        '''Gets all live-ins
        
        Ordered by descending house points'''
        pass

    def canTakeRoom(self, room, mates=[]):
        ''' Tells if a list of room mates can take a particular room
            Positional Arguments:
            room -- The room to be potentially taken
            Keyword Arguments:
            mates --  a List of User objects that want to see if
                      they can take the room. If this argument is
                      omitted, this method assumes that this person is 
                      trying to take this room as a single.
            If the room is not occupied, this method returns True
            If there is more than one person trying to take a room,
            the sum housepoint value of the potential roommates is used.
        '''
        if self.is_live_in:
            pass

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

        if self.is_live_in:
            pass
            # Allows us to treat this process only as a list of mates, even if single.
            if len(mates) == 0:
                mates.append(self)

    def canClaimChore(self, chore):
        ''' Tells if Person can claim a particular chore
            Positional Arguments:
            chore -- The desired chore (Chore object)
            If the chore isn't full yet, return True
        '''
        if self.is_live_in:
            pass

    def claimChore(self, chore):
        ''' Takes a chore
            Positional Arguments:
            chore -- The desired chore (Chore object)
            Pre-condition: canTakeChore(chore) must be True
                           raises Exception if not
        '''
        if self.is_live_in:
            pass


class Room(Base):
    __tablename__ = 'rooms'
    number = Column(Integer, primary_key=True)
    # users is a field (list)

    def __init__(self, number):
        self.number = number

    def __repr__(self):
        # Room 2   --> '<Room 002>'
        # Room 311 --> '<Room 311>'
        return '<Room %r>' % (str(self.number).zfill(3))

    def getOccupants(self):
        'Return a list of users currently occupying this room.'
        return self.users

    def isOccupied(self):
        'Tells is the room is currently occupied'
        return len(self.users) > 0

    def evictOccupant(self, occupant):
        '''Evict an occupant from a room.

        Requires a User object. Returns True for success.'''
        try:
            self.users.remove(occupant)
        except ValueError:
            return False
        db_session.commit()
        return True
        

    

