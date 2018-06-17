import pymongo
from pymongo import MongoClient

myClient=MongoClient()
db=myClient.mydb

users=db.users

user1={'userName':"Prakhar",'Password':"prakahar",'Age':25,"hobbies":["Python","Game","Pizza"]}

user_id=users.insert_one(user1).inserted_id

print(user_id)