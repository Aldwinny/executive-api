#Password Encoder
import hashlib
import random

from regex import split

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_salt():
    chars = []

    for i in range(16):
        chars.append(random.choice(ALPHABET))

    return ''.join(chars)

def salt_from_hash(enc):
    return split(":", enc)[0]

def generate_sha256_hash(secret):
    return hashlib.sha256(secret.encode('utf-8'))

def generate_storable_hash(username, password, salt=None):
    salty = generate_salt() if salt is None else salt
    return salty + ":" + generate_sha256_hash(username + password + salty).hexdigest()