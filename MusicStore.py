import pymongo
from pymongo import MongoClient

#check connection
try:
    conn = MongoClient()
    print("Connection Successful")
except:
    print("Connection Unsuccessful. Try again later.")
    
db = conn.MovieStore
custCollection = db.Customers
invColl = db.Inventory
cartColl = db.ShoppingCart

#print customers
doc = custCollection.find()
for data in doc:
    print(data)