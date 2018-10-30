from pymongo import MongoClient
from bson.objectid import ObjectId
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

# Querying the database collection for id and street
# Find_one will only find the first one that matches the parameters
print(coll.find_one({'_id': ObjectId('5baf855731b49517cd8e5407')}))

print(coll.find_one({'street': '6001 MCMAHON DR'}))

# Finds all for the specific parameter
i = 0
for docs in coll.find():
    if int(docs['price']) > 500000:
        print(docs)
        i += 1

print('Documents retreived with price > 500000', i)

sum = 0
for docs in coll.find():
    sum = sum + int(doc['price'])

print('Total Sales Price ${:,}'.format(sum))

# Bulk writing
from pymongo import InsertOne, DeleteOne, ReplaceOne

db = client.new_dump_db
coll = db.num_coll

# upsert will input the new object even if it does not find the one it is
# replacing
requests = [
    InsertOne({'Binel':100}),
    DeleteOne({'Binel':100}),
    ReplaceOne({'Binel':100}, {'Ben':1000}, upsert=True)
]

results = coll.bulk_write(requests)

print('Final writes are: ', results.inserted_count)


# Deletions based on criteria
# Need to re-assign the origional db though for this to work

db = client.new_db

coll = db.db_collection

coll.delete_many({
    'city':{
        '$eq':'Sacramento'.upper()
    }
})

print('Docs in collection: ', coll.estimated_document_count())

#This will remove all items in the collection
coll.delete_many({})

print('Docs in collection: ', coll.estimated_document_count())
