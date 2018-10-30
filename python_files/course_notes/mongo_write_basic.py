from pymongo import MongoClient
import csv

# Connects to a mongo client after .net/ you can specify an existing or
# create new database
client = MongoClient(
    'mongodb+srv://chrislockard:Enveydis_1@cluster0-rkwsl.mongodb.net/new_db?'
    'retryWrites=true'
)

# you can create a new cluster simply by specifying it as an attribute of client
db = client.new_db

coll = db.db_collection

with open('Sacramentorealestatetransactions.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        coll.insert_one(row).inserted_id

print('Initial Documents in collection:', coll.estimated_document_count())

with open('Sacramentorealestatetransactions.csv', newline='') as file:
    reader = csv.DictReader(file)
    coll.insert_many(reader)

coll_no = db.NumberCollection

coll_no.insert_many({'number': i, 'earnings': i*10} for i in range(100)).inserted_ids
