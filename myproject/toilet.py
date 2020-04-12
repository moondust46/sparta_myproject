import pymongo
import json # import json module

# with statement
with open('toilet.json') as json_file:
    json_data = json.load(json_file)


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient.dbsparta
mycol = mydb.toilet


x = mycol.insert_many(json_data['DATA'])

#print list of the _id values of the inserted documents:
print(x.inserted_ids)
