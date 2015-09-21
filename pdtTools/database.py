import platform
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dist = platform.dist()[0]

path = 'sqlite:///'
DB_FILE_NAME = 'data.db'

if dist == 'centos':
    path += '/home/jnaranj0/webapps/phidelttools/pdtTools/%s' % DB_FILE_NAME
else:
    #path += '/home/luis/Dropbox/pdtTools/test.db'
    db_path = os.path.split(os.path.abspath(__file__))[0]
    db_path = os.path.split(db_path)[0]
    path += os.path.join(db_path, DB_FILE_NAME)
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


init_db()