from pdtTools.database import init_db, db_session
from pdtTools.models import User, Room

init_db()

def delete_all():
    User.query.delete()
'''
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    password_hash = Column(String(54))
    bond_number = Column(String(4), unique=True)
    house_points = Column(Float)
    is_live_in = Column(Boolean)
    #room = Column(Room)
    #chore = Column(Chore)
'''

rooms = [Room(102), Room(212), Room(306), Room(002)]
if len(Room.query.all()) < 1:
    for room in rooms:
        db_session.add(room)
        print 'Adding %s' % room
    db_session.commit()

test_user_dicts = [
    {
        'email': 'luis@gmail.com', 'password_hash': 'test', 'name': 'Luis', 'is_admin': True,
    },

    {
        'email': 'michael@gmail.com', 'password_hash': 'test', 'name': 'Michael'
    },

    {
        'email': 'dan@gmail.com', 'password_hash': 'test', 'name': 'Dan'
    },

    {
        'email': 'bo@gmail.com', 'password_hash': 'test', 'name': 'Bo'
    },

    {
        'email': 'frank@gmail.com', 'password_hash': 'test', 'name': 'Frank'
    },
]

test_users = []

for user_dict in test_user_dicts:
    user = User(**user_dict)
    test_users.append(user)


if len(User.query.all()) < 2:
    for user in test_users:
        db_session.add(user)
        print 'Adding %s' % user
    db_session.commit()


def getUser(): return User.query.filter(User.name == 'Luis').first()
def getRoom(): return Room.query.filter(Room.number == 102).first()

user = getUser()
room = getRoom()

