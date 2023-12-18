import pymongo
from datetime import datetime, timedelta

# Подключение к MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['mycollection']

# Создание TTL индекса на поле 'expiration_time' с временем жизни в 24 часа
collection.create_index("expiration_time", expireAfterSeconds=24*60*60)

# Добавление документа с полем 'expiration_time' равным текущему времени плюс 24 часа
document = {
    "data": "some data",
    "expiration_time": datetime.now() + timedelta(days=1)
}
collection.insert_one(document)
