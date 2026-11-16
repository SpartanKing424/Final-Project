from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: str
'''
user login database, may have to figure out a different storage plan
    - Drafter might not be able to permanently alter this file
    - Having this file open to the public on Github is not very secure...
'''
user_database = [
    User("user1", "1")
]