from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BaseModel = declarative_base()

engine = create_engine("mysql+pymysql://root:jacky@127.0.0.1/test", echo=False)

DBSession = sessionmaker(bind=engine)

'''
Create database
'''
#conn = engine.connect()
#conn.execute("commit")
#conn.execute("drop database mytestdb")
#conn.execute("create database mytestdb")
#conn.close()

'''
Create table
'''
class User(BaseModel):
    __tablename__ = "user1"  # table name
    user_name = Column(CHAR(30), primary_key=True)
    age = Column(SMALLINT(), server_default="10")

def init_db():
    BaseModel.metadata.create_all(engine)

def drop_db():
    BaseModel.metadata.drop_all(engine)

drop_db()
init_db()

'''
Insert data
'''
session = DBSession()
user1 = User(user_name="jacky", age=123)
session.add(user1)
user2 = User(user_name="tom", age=456)
session.add(user2)
user3 = User(user_name="jerry", age=789)
session.add(user3)
session.commit()

'''
Query
'''
res = session.query(User).all()
for user in res:
    print(user.user_name)
    print(user.age)

'''
Update
'''
query = session.query(User)
user = query.get("tom")
user.age = 11
session.commit()
print(user.user_name)
print(user.age)

'''
Delete
'''
query = session.query(User)
user = query.get("jerry")
session.delete(user)
session.commit()

'''
Execute SQL
'''
sql_cmd = "select * from user1"
res = session.execute(sql_cmd)
print("-----------------")
for user in res:
    print(user.user_name)
    print(user.age)


session.close()
