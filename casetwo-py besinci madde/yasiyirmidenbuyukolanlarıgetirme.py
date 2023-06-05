from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient('<mongodb_connection_string>')
db = client['<database_name>']
collection = db['Users']

# Yaşı 20'den büyük olan kullanıcıları getir
age_threshold = 20
filtered_users = collection.find({"Age": {"$gt": age_threshold}})

for user in filtered_users:
    print(user)
