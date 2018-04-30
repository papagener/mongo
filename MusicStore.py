import pymongo
from pymongo import MongoClient
from passlib.hash import sha256_crypt

#We need to have a connection, because right now we have conn.MovieStore
#with no host
#


#check connection
try:
    conn = MongoClient('localhost', 27017)
    print("Connection Successful")
except:
    print("Connection Unsuccessful. Try again later.")

#MusicStore, not MovieStore
db = conn.MusicStore
customers = db.Customers
inventory = db.Inventory
shoppingCart = db.ShoppingCart
testCust = db.TEST_Customer

#get customer info and match with db
#if match > login, else error
def loginCustomer():
    login = customers.find()
    print("You are logged in!")   

#create a new customer account
def createCustomer():
    db.Customers.insert({'customerID': "0112",
                            'firstName': firstName,
                            'lastName': lastName,
                            'email': email,
                            'pw': hashpw,
                        })
def list():
    doc = customers.find()
    for data in doc:
        print(data['firstName'], data['lastName'], data['pw'])

print("\nMain Menu")
print("Enter 1 to Login. Enter 2 to Create an Account: ")
choice = int(input())
if choice == 1:
    email = input("Enter your email: ")
    pw = input("enter your password: ")   
    loginCustomer()   
if choice == 2:
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    email = input("Enter your e-mail: ")
    password = input("Enter a password: ")   
    hashpw = sha256_crypt.encrypt(password)
    
    
    createCustomer()
    print("Welcome!")
if choice == 3:
    pw = input("Enter a password: ")
    password = sha256_crypt.encrypt(pw)
    print(password)
    


#def custLogin():
    
