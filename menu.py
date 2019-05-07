import os
import pymongo
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

# mongodb information
app = Flask(__name__)
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "Project0"
COLLECTION_NAME = "Cluster0"

# testing database connection
def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
#menu screen        
def show_menu():
    print("")
    print("1. Add a recipe")
    print("2. Find a recipe")
    print("3. Update an existing recipe")
    print("4. Delete a recipe")
    print("5. Exit")
    
    option = input("Enter option")
    return option
#once option is selected, return the correct value    
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            print("You have selected option 1")
        elif option == "2":
            print("You have selected option 2")
        elif option == "3":
            print("You have selected option 3")
        elif option == "4":
            print("You have selected option 4")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")    
        
#conn/coll definitions        
conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]   

main_loop()
        
        
        