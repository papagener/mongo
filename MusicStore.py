import pymongo
from pymongo import MongoClient

#check connection
try:
    conn = MongoClient()
    print("Connection Successful")
except:
    print("Connection Unsuccessful. Try again later.")
    
db = conn.MusicStore
custCollection = db.customer
invColl = db.inventory
cartColl = db.shoppingCart

#print customers
doc = custCollection.find()
for data in doc:
    print(data)