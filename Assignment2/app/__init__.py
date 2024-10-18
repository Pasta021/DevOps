# To install flask, first run the following line in the terminal:
# pip install flask

# To import the flask into the project use the following line:
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
flask_app = Flask(__name__)

db_username = os.environ["MONGODB_USERNAME"]
db_password = os.environ["MONGODB_PASSWORD"]

print(db_username)
print(db_password)

# MongoDB Atlas Connection
client = MongoClient(f"mongodb+srv://{db_username}:{db_password}@cluster0.kaq1p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db  # Replace "app" with your database name
products_collection = db.products  # Replace products with your collection name

from app import routes