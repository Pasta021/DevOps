# pip install pymongo
from pymongo import MongoClient

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://root:9xgCOMv6ZbMtpPKH@cluster0.kaq1p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.shop_db  # Replace "app" with your database name
products_collection = db.products  # Replace products with your collection name

# Example product objects
products = [
    {
        "name": "Product 1",
        "image": "/static/images/product1.jpg",
        "price": 29.99,
        "tag": "New"
    },
    {
        "name": "Product 2",
        "image": "/static/images/product2.jpg",
        "price": 49.99,
        "tag": "Discounted"
    },
    {
        "name": "Product 3",
        "image": "/static/images/product3.jpg",
        "price": 19.99,
        "tag": "Best Seller"
    }
]

black_friday_deals = {
        "name": "Product 4",
        "image": "/static/images/product4.jpg",
        "price": 9.99,
        "tag": "Black Friday Deals"
    }

products_collection.insert_many(products)  # allows you to add a list of dictionaries into the database
products_collection.insert_one(black_friday_deals)  # allows you to add a single dictionary into the database