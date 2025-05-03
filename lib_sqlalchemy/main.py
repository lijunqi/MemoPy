import time

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from models import Base, User, Task

ENGINE = create_engine("mysql+pymysql://root:jacky@127.0.0.1/test", echo=False)
DBSession = sessionmaker(bind=ENGINE)
SESS = DBSession()

def init_db():
    Base.metadata.create_all(ENGINE)

    try:
        # ~ Add user
        u1 = User(name="Tom", email="tom@gmail.com")
        SESS.add(u1)
        u2 = User(name="Jerry", email="jerry@gmail.com")
        SESS.add(u2)
        u3 = User(name="Mike", email="mike@gmail.com")
        SESS.add(u3)

        # ~ Add task
        SESS.add(Task(title="task 1", description="this is task one", user=u1))
        SESS.add(Task(title="task 2", description="this is task two", user=u1))
        SESS.add(Task(title="task 3", description="this is task three", user=u2))
        SESS.add(Task(title="task 4", description="this is task four", user=u3))

        SESS.commit()
    except IntegrityError as exc:
        SESS.rollback()
        print("Error: add user. ", str(exc))



def drop_db():
    Base.metadata.drop_all(ENGINE)


def get_user_by_email(user_email):
    return SESS.query(User).filter_by(email=user_email)


if __name__ == "__main__":
    st = time.time()
    drop_db()
    init_db()

    user = SESS.query(User).filter_by(name="Tom").first()
    if user:
        print(f"[Success]Query Tom: {user.name}, id={user.id}")
        for t in user.tasks:
            print(f"{'User\'s task':^15}: {t.title}, {t.description}")
            print('='*15)

    print(f"Well done. Time = {time.time() - st:.2f}")
