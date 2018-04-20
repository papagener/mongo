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
customers = db.Customers
inventory = db.Inventory
shoppingCart = db.ShoppingCart
testCust = db.TEST_Customer

def createCustomer():
    db.Customers.insert({'customerID': "0112",
                            'firstName': firstName,
                            'lastName': lastName,
                            'email': email,
                            'pw': password,
                        })

print("\nEnter 1 to Login OR Enter 2 to Create an Account: ")
choice = int(input())
if choice == 1:
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    email = input("Enter your e-mail: ")
    password = input("Enter a password: ")
    
    createCustomer()
else:
    custLogin()


#def custLogin():

doc = customers.find()
for data in doc:
    print(data['firstName'], data['lastName'], data['pw'])
    
