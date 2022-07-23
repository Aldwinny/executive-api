import sqlite3
import logging as log

from sqlite3 import Error

from ..utils import passenc
from ..model.user import User


__DB_LOCATION = "././db/users.db"

# Features
# 1. Request users count (/)
# 2. password hashing
# 3. create, read, update, delete userdata

def __connect():
    conn = None
    try:
        conn = sqlite3.connect(__DB_LOCATION)
    except Error as e:
        log.critical(e)
        return conn
    finally:
        return conn

# def init():
#     query = """CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY,
#         name TEXT UNIQUE NOT NULL,
#         directory TEXT NOT NULL,
#         admin INTEGER NOT NULL DEFAULT 0,
#         password TEXT NOT NULL
#     );"""
#     conn = __connect()
#     try:
#         conn.execute("DROP TABLE IF EXISTS users")
#         conn.execute(query)

#         guest = User.get_guest_account().db_format()
#         register_user(guest[0], guest[1], guest[2], guest[3])
#         conn.commit()

#     except Error as e:
#         print(e)
        

def count_users():
    conn = __connect()
    count = 0
    try:
        c = conn.cursor()
        c.execute("SELECT count(*) FROM users")
        count = c.fetchall()[0][0]
    except Error as e:
        log.critical(e)
    finally:
        conn.close()
        return count

def get_users():
    conn = __connect()
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        return users
    except Error as e:
        log.critical(e)
        return 0

# Returns first instance
def get_user(name, close = False):
    conn = __connect()
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE `name`='{}'".format(name))
        user = c.fetchall()
        return user
    except Error as e:
        print(e)
        return 0

def register_user(name, dir, isAdmin, password, obtain = True, close = False):
    conn = __connect()
    try:
        c = conn.cursor()

        # Confirm existence of user, then reject registration attempt if user exists.
        if record_exists(name):
            print("Name already registered. Please use a different name.")
            return 0

        c.execute("INSERT INTO users(`name`, `directory`, `admin`, `password`) VALUES ('{}', '{}', '{}', '{}')".format(name, dir, 1 if isAdmin else 0, passenc.generate_storable_hash(name, password)))
        res = c.fetchall
        return res
    except Error as e:
        print(e)
        return 0

# TODO: optimizeable: kwargs** can be used except im too lazy to do it..
def edit_user(user, target, new, password):
    conn = __connect()
    try:
        c = conn.cursor()
        if record_exists(user.name):
            salt = passenc.salt_from_hash(c.execute("SELECT password FROM users WHERE `name`='{}'".format(user.name)).fetchall()[0][0])
        else:
            print("User does not exist")
            return 0
        conn.execute("UPDATE users SET `{}`='{}' WHERE `password`='{}';".format(target, new, passenc.generate_storable_hash(user.name, password, salt)))
    except Error as e:
        print(e)
        return 0
    finally:
        commit(conn)

def record_exists(name):
    conn = __connect()
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE `name`='{}'".format(name))
        res = len(c.fetchall()) > 0
        return res
    except Error as e:
        print(e)
        return False
    finally:
        conn.close()

def commit(conn = __connect(), close = False):
    try:
        conn.commit()
    except Error as e:
        log.critical(e)
    finally:
        if close:
            conn.close()