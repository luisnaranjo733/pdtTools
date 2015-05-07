import platform
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dist = platform.dist()[0]

path = 'sqlite:///'

if dist == 'centos':
    temp = os.path.expanduser('~')
    temp = os.path.join(temp, 'webapps')
    temp = os.path.join(temp, 'phidelttools')
    temp = os.path.join(temp, 'pdtTools')
    temp = os.path.join(temp, 'test.db')
    path += temp
else:
    path += '/home/luis/Dropbox/pdtTools/test.db'
engine = create_engine(path, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import pdtTools.models
    Base.metadata.create_all(bind=engine)
