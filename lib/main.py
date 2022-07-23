import sys
import logging as log

from regex import split

from .model.user import User
from .shared import constants as const
from .db import user_db as db
from .utils import passenc as ps

def main():
    # args = sys.argv[1:]

    guest = User.get_guest_account()

    me = User("Aldwin", "c:/", True)

    db.register_user("Aldwin", "c:/", True, "Secret")
    db.edit_user(me, "name", "Alds", "Secret")


    item = db.get_users()
    count = db.count_users()
    print(item)
    print(count)





    # query = """CREATE TABLE IF NOT EXISTS users (
    #     id INTEGER PRIMARY KEY,
    #     name TEXT NOT NULL,
    #     directory TEXT NOT NULL,
    #     admin INTEGER NOT NULL DEFAULT 0
    # );"""

    # query_in = """INSERT INTO users(name, directory, admin) VALUES(?,?,?);"""
    
    # query_s = """SELECT * FROM users;"""

    # c = db.insert(users_db, query_in, guest.db_format())
    # c = db.execute(users_db, query_s, True)

    # rows = c.fetchall()

    # for row in rows:
    #     print(row)

    # users_db.commit()
    # users_db.close()


if __name__ == "__main__":
    main()
else:
    print(__name__)