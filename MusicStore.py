#Title: MusicStore.py
#Description: The purpose of this program is to simulate a music store that sells physical copies
# of music (we'll say vinyl records since it's 2018).  Our clients want an online purchasing system that
# allows users to register.  Once registered (and with a payment method on file) clients may purchase
# physical copies which they may then pick up.
#

import pymongo
from pymongo import MongoClient
from passlib.hash import sha256_crypt


#check connection

#try MongoClient() first, which is PyMongo
#pass parameters String name, int portNo 
try:
    conn = MongoClient('localhost', 27017) #make sure the port number is correct
    print("Connection Successful")
except:
    print("Connection Unsuccessful. Try again later.")

#Connection to database made
#Select database
#MusicStore (CHANGE AS NEEDED)
db = conn.MusicStore

#all collections are occurring in MusicStore
#select (or create) collection Customers
customers = db.Customers
#select (or create) collection Inventory
inventory = db.Inventory
#select (or create) collection ShoppingCart
shoppingCart = db.ShoppingCart
#select (or create) collection TEST_Customer
testCust = db.TEST_Customer

#set different flags
outerLoopFlag = True;

innerLoopFlag2 = True;


#-------------------------------------------------------------------------------------------
#
#This section is for our different functions, creating them now and putting them together
#seems like a nice way to organize them.  If there are more in the future, we can add them
#here later as well.
#
#-------------------------------------------------------------------------------------------


#get customer info and match with db
#if match > login, else error
#figure out how to verify pw and email
def loginCustomer(email, pw):
    login = customers.find_one({"email" : email})       
    
    if login is None:
        print("Invalid/Inactive User")
    else:
        hash = {'pw'} 
        if sha256_crypt.verify(pw, hash):    
            print("You are logged in!")   

#create a new customer account
def createCustomer():
    customers.insert({'firstName': firstName,
                            'lastName': lastName,
                            'email': email,
                            'pw': hashpw,
                        })
def list():
    doc = customers.find()
    for data in doc:
        print(data['firstName'], data['lastName'], data['pw'])

#Set up a menu to go through
#Unlike Java, Python does not offer us a
#switch statement
#so we've just had to make a few different if statements here

while outerLoopFlag == True:
    print("\nMain Menu")
    print("Enter 1 to Login. Enter 2 to Create an Account: ")
    choice = int(input())
    
    #2nd level indent, inside of outer while loop
    if choice == 1:
        email = input("Enter your email: ")
        pw = input("enter your password: ")   
        loginCustomer(email, pw)   
        #once logged in enter a while loop for 



    #2nd level indent, inside of outer while loop        
    if choice == 2:
        innerLoopFlag = True;
        while innerLoopFlag == True:
            firstName = input("Enter your first name: ")
            lastName = input("Enter your last name: ")
            email = input("Enter your e-mail: ")
            password = input("Enter a password: ")   
            hashpw = sha256_crypt.encrypt(password)
            
            #will have to index e-mail since that is unique
            #if email is found, thus "is not None", give error message
            findUser = db.Customers.find_one({"email" : email})
            
            if findUser is None:
                createCustomer() 
                result = db.Customers.create_index([('email', pymongo.ASCENDING)], unique = True)
                print("Welcome!")
                break;
            else:
                #previously gave information that email was already registered, elected not to give
                #that information freely
                print("Invalid entry") 
                       
        
    
        



    #probably not sticking around --- developmental
    if choice == 3:
        pw = input("Enter a password: ")
        password = sha256_crypt.encrypt(pw)
        print(password)
        doc.list()
    


#def custLogin():
    
