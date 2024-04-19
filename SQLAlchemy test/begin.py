from sqlalchemy import Column, Integer, String, Sequence, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, aliased

engine = create_engine('sqlite:///:memory:', echo=True)
# We bind the engine only if it exists if not then the command remains Session = sessionmaker()
Session = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)


# Hence User.__table Represents the table metadata as shown below
# Table('users', MetaData(bind=None),
#             Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
#             Column('name', String(), table=<users>),
#             Column('fullname', String(), table=<users>),
#             Column('nickname', String(), table=<users>), schema=None)

Base.metadata.create_all(engine)

# This queries the args instance and prints it out in the order stated

for instance in Session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)
# This takes the args name and fullname queries the arguments and prints it out in the order stated
for name, fullname in Session.query(User.fullname, User.name):
    print(name, fullname)
# This is a simple query that queries the User table and prints out the name and fullname
for row in Session.query(User, User.name).all():
    print(row.User, row.name)

user_alias = aliased(User, name='user_alias')

for row in Session.query(user_alias, user_alias.name).all():
    print(row.user_alias, row.name)
