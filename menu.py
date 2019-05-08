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
    
#find recipe function
def find_recipe():
    print("")
    recipe_name = input("Enter recipe name >")
    author = input("Enter an authors name > ")
    Ingredients = input("Enter an Ingredient here > ")
    
    #search function options
    try:
        doc = coll.find_one({'recipe_name': recipe_name.lower(), 'author': author.lower(),
            'Ingredients': Ingredients()
        })
    #failed search result    
    except:
        print("Error accessing the database")
    
    #no document found result    
    if not doc:
        print("")
        print("Error! No results found.")
        
    return doc    
# add recipe function    
def add_recipe():
    print("")
    recipe_name = input("Enter the name of your recipe > ")
    author = input("Enter the author of the recipe > ")
    description = input("Enter a description of the dish > ")
    Ingredients = input("Enter all Ingredients required > ")
    method = input("Enter a step by step method to making the dish > ")
    
#dictionary for add recipe function
    new_doc = { 'recipe name': recipe_name.lower(), 'author': author.lower(), 
    'description': description(), 'Ingredients': Ingredients(), 'method': method()}
    #document successfully added 
    
    try: 
        coll.insert(add_recipe)
        print("")
        print("Document Inserted")
        
    #document failed to be added 
    except:
        print("Error accessing the database")
        
    
#once option is selected, print the selected option to screen    
def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_recipe()
        elif option == "2":
            find_recipe()
        elif option == "3":
            update_recipe()
        elif option == "4":
            delete_recipe()
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
        
        
        
        
        