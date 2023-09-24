import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/neuronlabDB")

dataBase = client("neuronlabDB")

collection = dataBase["Products"]

d = {
    "companyName" : "iNeuron",
    "product" : "Affordable AI",
    "courseOffered" : "Machine Learning with Deployment"
}

rec = collection.insert_one(d)

all_record = collection.fine()

for ids, record in enumerate(all_record):
    print(f"{idx} : {record}")