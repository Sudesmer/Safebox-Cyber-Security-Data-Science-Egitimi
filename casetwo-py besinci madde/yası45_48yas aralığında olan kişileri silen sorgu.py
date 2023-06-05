from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient('<mongodb_connection_string>')
db = client['<database_name>']
collection = db['Users']

# Yaşı 45-48 arasında olan kullanıcıları sil
age_min = 45
age_max = 48
collection.delete_many({"Age": {"$gte": age_min, "$lte": age_max}})

print("Silme işlemi tamamlandı.")
