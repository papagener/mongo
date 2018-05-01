import pymongo
from pymongo import MongoClient
from passlib.hash import sha256_crypt

#We need to have a connection, because right now we have conn.MovieStore
#with no host


#check connection
try:
    conn = MongoClient('localhost', 27017) #make sure the port number is correct
    print("Connection Successful")
except:
    print("Connection Unsuccessful. Try again later.")

#MusicStore/MovieStore CHANGE AS NEEDED
db = conn.MovieStore
customers = db.Customers
inventory = db.Inventory
shoppingCart = db.ShoppingCart
testCust = db.TEST_Customer

#clear shopping cart after checking out or logging out
def clearCart():
    db.shoppingCart.drop()

#create a new temporary shopping cart that will be removed at end of purchase.
def newShoppingCart(selection):
    db.shoppingCart.insert({'title': selection })
    cart = shoppingCart.find()
    for data in cart:
        print(data)

#Once logged in, customer can choose music titles to add to cart.
def loggedIn():
    flag = 1
    while flag == 1:
        print("What would you like to do? ")
        print("1. Add music to cart: " + "\n2. Check out: " + "\n3. Log Out: ")
        choice = int(input())
        
        #add music to cart option
        #inventory is printed for viewing purposes and title is entered to make a selection
        #
        if choice == 1:
            all = inventory.find()
            for data in all:
                print("Title: " + data['title'] + " Price: "+ data['price'] + " Quantity: " + data['quantity'])
            selection = input("Enter title to add to cart: ")
            newShoppingCart(selection)
        
        if choice == 2:
            clearCart()
            print("You have successfully checked out! ")
            break
            
            
        if choice == 3:
            clearCart()
            print("You have logged out. ")
            break
    
#get customer info and match with db
#if match > login, else error
#figure out how to verify pw and email
def loginCustomer(email, pw):
    login = customers.find({'email': email, 'pw': pw})
    for data in login:
        print("Welcome " + data['firstName'] + " " + data['lastName'])
        loggedIn()
     
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
print("1. Login \n2. Create an Account ")
choice = int(input())
if choice == 1:
    email = input("Enter your email: ")
    pw = input("Enter your password: ")   
    loginCustomer(email, pw)
    #print(sha256_crypt.verify(pw, pw))
    #once logged in enter a while loop for 


if choice == 2:
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    email = input("Enter your e-mail: ")
    password = input("Enter a password: ")   
    #hashpw = sha256_crypt.encrypt(password)
    #hashing verifcation not working. Keeping password unhashed.
    
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
    test = input("Enter pw: ")
    print(sha256_crypt.verify(test, password))
    #list()
    


#def custLogin():
    
