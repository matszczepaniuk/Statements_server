import hashlib
import random
import string

def hash_password(password, salt=None):
    if salt is None:
        salt = generate_salt()

    if len(salt) < 16:
        salt += ("a" * (16 - len(salt)))

    if len(salt) > 16:
        salt = salt[:16]

    t_sha = hashlib.sha256()

    t_sha.update(salt.encode('utf-8') + password.encode('utf-8'))

    return salt + t_sha.hexdigest()

def check_password(pass_to_check, hashed):
    salt = hashed[:16]
    hash_to_check = hashed[16:]
    new_hash = hash_password(pass_to_check, salt)
    return new_hash[16:] == hash_to_check

def generate_salt():
    salt = ""
    for i in range(0, 16):
        salt += random.choice(string.ascii_letters)
    return salt
