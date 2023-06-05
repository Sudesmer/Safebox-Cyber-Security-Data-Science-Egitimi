from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient('<mongodb_connection_string>')
db = client['<database_name>']
collection = db['Users']

# İsmi Ahmet olan kullanıcıları getir
name = "Ahmet"
filtered_users = collection.find({"Name": name})

for user in filtered_users:
    print(user)
