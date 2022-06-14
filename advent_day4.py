import hashlib


key = "yzbqklnj"


def hash_input():
    hexidemical_hash = hashlib.md5(key.encode())
    return (hexidemical_hash.hexdigest())


print(hash_input())