from flask import Flask, request, jsonify
from pymongo import MongoClient

# Flask uygulamasını başlat
app = Flask(__name__)

# MongoDB'ye bağlan
client = MongoClient('<mongodb_connection_string>')
db = client['<database_name>']
collection = db['Users']

# Endpoint 1: Kullanıcı ekleme
@app.route('/adduser', methods=['POST'])
def add_user():
    user_data = request.json

    # Kullanıcıyı Users koleksiyonuna ekle
    collection.insert_one(user_data)

    return jsonify({'message': 'Kullanıcı başarıyla eklendi'})

# Endpoint 2: Yaşı 25'ten büyük olanları döndürme
@app.route('/25', methods=['GET'])
def get_users_above_25():
    filtered_users = collection.find({"Age": {"$gt": 25}})
    users = []

    for user in filtered_users:
        users.append(user)

    return jsonify(users)

# Endpoint 3: Tüm kullanıcıları döndürme
@app.route('/', methods=['GET'])
def get_all_users():
    all_users = collection.find()
    users = []

    for user in all_users:
        users.append(user)

    return jsonify(users)

# Endpoint 4: Verilen id'ye sahip kullanıcıyı silme
@app.route('/deleteuser', methods=['POST', 'DELETE'])
def delete_user():
    user_id = request.json['id']

    # Kullanıcıyı id'ye göre sil
    collection.delete_one({"_id": user_id})

    return jsonify({'message': 'Kullanıcı başarıyla silindi'})

# Flask uygulamasını çalıştırma
if __name__ == '__main__':
    app.run()
