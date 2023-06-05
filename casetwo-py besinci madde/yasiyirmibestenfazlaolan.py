from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient('<mongodb_connection_string>')
db = client['<database_name>']
collection = db['Users']

# Yaşı 25'ten büyük olan kullanıcıların description'ını 0 yap
age_threshold = 25
collection.update_many({"Age": {"$gt": age_threshold}}, {"$set": {"Description": "0"}})

print("Güncelleme tamamlandı.")
