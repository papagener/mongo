import pymongo
from pymongo import MongoClient
from passlib.hash import sha256_crypt

#check connection
try:
    conn = MongoClient()
    print("Connection Successful")
except:
    print("Connection Unsuccessful. Try again later.")

#MusicStore, not MovieStore
db = conn.MovieStore
custCollection = db.Customers
invColl = db.Inventory
cartColl = db.ShoppingCart


print("\nEnter 1 to Log in OR Enter 2 to Create an Account: ")

def createCustomer():
    db.custCollection.insert()
    

    
#print customers
doc = custCollection.find()
for data in doc:
    print(data['firstName'], data['lastName'], data['pw'])
    
