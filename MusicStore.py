import pymongo
from pymongo import MongoClient
from passlib.hash import sha256_crypt

#We need to have a connection, because right now we have conn.MovieStore
#with no host
#


#check connection
try:
    conn = MongoClient('localhost', 27017) #make sure the port number is correct
    print("Connection Successful")
except:
    print("Connection Unsuccessful. Try again later.")

#MusicStore/MovieStore CHANGE AS NEEDED
db = conn.MusicStore
customers = db.Customers
inventory = db.Inventory
shoppingCart = db.ShoppingCart
testCust = db.TEST_Customer

#get customer info and match with db
#if match > login, else error
#figure out how to verify pw and email
def loginCustomer():
    login = customers.find()
    print("You are logged in!")   

#create a new customer account
def createCustomer():
    db.Customers.insert({'firstName': firstName,
                            'lastName': lastName,
                            'email': email,
                            'pw': hashpw,
                        })
def list():
    doc = customers.find()
    for data in doc:
        print(data['firstName'], data['lastName'], data['pw'])

#Setup a menu to go through
#Unlike Java, Python does not offer us a
#switch statement
#so we've just had to make a few different if statements here
print("\nMain Menu")
print("Enter 1 to Login. Enter 2 to Create an Account: ")
choice = int(input())
if choice == 1:
    email = input("Enter your email: ")
    pw = input("enter your password: ")   
    loginCustomer()   
    #once logged in enter a while loop for 


if choice == 2:
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    email = input("Enter your e-mail: ")
    password = input("Enter a password: ")   
    hashpw = sha256_crypt.encrypt(password)
    #will have to index e-mail since that is unique
    findUser = db.Customers.find({"email" : email})
    if findUser is not None:
        print("E-mail address already exists in database! Please register a different e-mail address!")

    else:
        createCustomer()        
    
        
    result = db.Customers.create_index([('email', pymongo.ASCENDING)], unique = True)
    sorted(list(db.Customers.index_information()))
    
    
    
    print("Welcome!")
if choice == 3:
    pw = input("Enter a password: ")
    password = sha256_crypt.encrypt(pw)
    print(password)
    doc.list()
    


#def custLogin():
    
