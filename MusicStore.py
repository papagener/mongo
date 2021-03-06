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

#all collections are occurring in MusicStore
#select (or create) collection Customers
#MusicStore/MovieStore CHANGE AS NEEDED
db = conn.MovieStore

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

#remove shopping cart after checking out or logging out
def removeCart():
    db.shoppingCart.drop()

#In progress, but need to get newShoppingcart() working first.
def viewCart():
    cart = db.shoppingCart.find()
    for data in cart:
        print(data['title'], data['price'])
    
#create a new temporary shopping cart that will be removed at end of purchase.
#find the current music title selection and add to the new cart.
def newShoppingCart(selection):
    find = inventory.find({'title': selection})
    for data in find:
        print(data['title'], data['price'], "has been added to cart.")
        db.shoppingCart.insert({'title': data['title'], 'price': data['price']})
    #db.shoppingCart.insert({ find })
    #cart = shoppingCart.find()
    #for data in cart:
        #print(data['title'])

#Once logged in, customer can choose music titles to add to cart.
def loggedIn():
    flag = 1
    while flag == 1:
        print("\nWhat would you like to do? ")
        print("1. Add music to cart " + "\n2. View cart" +"\n3. Check out " + "\n4. Log Out ")
        choice = int(input())
        
        #add music to cart option
        #inventory is printed for viewing purposes and title is entered to make a selection
        #
        if choice == 1:
            print("\nMusic List:")
            all = inventory.find()
            for data in all:
                print("Title: " + data['title'], data['price'])
            selection = input("Enter title to add to cart: ")
            newShoppingCart(selection)
        
        if choice == 2:
            print("\nYour cart: ")
            viewCart()

        if choice == 3:
            #cart validation to be inserted here
            removeCart()
            print("\nYou have successfully checked out! ")
            
        if choice == 4:
            #destroy cart if logged out
            removeCart()
            print("\nYou have logged out. ")
            break
    
#get customer info and match with db
#if match > login, else error
#figure out how to verify pw and email
def loginCustomer(email, pw):
    login = customers.find({'email': email})
    if login is None:
        return "Invalid entry!"
    else:
        for data in login:
            password = data['pw']
            if pw == password:
                #return "Valid user"
            
                #return "You are logged in!"
                print("\nWelcome " + data['firstName'] + " " + data['lastName']+"!")
                innerLoopFlag3 = True;
                loggedIn()
            else:
                return "The Email and Password did not match. Try again."     
#create a new customer account
def createCustomer():
    db.Customers.insert({'firstName': firstName,
                         'lastName': lastName,
                         'email': email,
                         'pw': password,
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
    print("1. Login \n2. Create an Account ")
    choice = int(input())

    #2nd level indent, inside of outer while loop        
    if choice == 1:
        email = input("Enter your email: ")
        pw = input("Enter your password: ")   
        clientLogin = loginCustomer(email, pw)
        print(clientLogin)
        outerLoopFlag = False

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
                break
            else:
                #previously gave information that email was already registered, elected not to give
                #that information freely
                print("Invalid entry") 
                       
    
