from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient('<mongodb_connection_string>')
db = client['<database_name>']
collection = db['Users']

# Tüm verileri getir
all_users = collection.find()

for user in all_users:
    print(user)
