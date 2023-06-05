import random
from pymongo import MongoClient

# MongoDB'ye bağlan
client = MongoClient('<mongodb_connection_string>')
db = client['<database_name>']
collection = db['Users']

# Kullanıcı verilerini oluştur ve ekle
for _ in range(50):
    name = random.choice(['John', 'Jane', 'Mike', 'Emily'])
    age = random.randint(0, 50)
    job = random.choice(['Engineer', 'Teacher', 'Doctor', 'Artist'])
    description = "1"
    
    user_data = {
        'Name': name,
        'Age': age,
        'Job': job,
        'Description': description
    }
    
    collection.insert_one(user_data)

print("Veri ekleme tamamlandı.")
