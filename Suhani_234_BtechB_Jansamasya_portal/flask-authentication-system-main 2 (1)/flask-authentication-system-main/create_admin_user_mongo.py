from pymongo import MongoClient
from werkzeug.security import generate_password_hash

def create_admin_user(name, email, password):
    client = MongoClient("mongodb://localhost:27017/")
    db = client['mydatabase']
    users_collection = db['users']

    existing_user = users_collection.find_one({'email': email})
    if existing_user:
        print(f"User with email {email} already exists.")
        # Update is_admin to True
        users_collection.update_one({'email': email}, {'$set': {'is_admin': True}})
        print(f"Updated user {email} to admin.")
        return

    hashed_password = generate_password_hash(password)
    admin_user = {
        'name': name,
        'email': email,
        'password': hashed_password,
        'is_admin': True
    }
    users_collection.insert_one(admin_user)
    print(f"Admin user {name} created successfully.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python3 create_admin_user_mongo.py <name> <email> <password>")
    else:
        name = sys.argv[1]
        email = sys.argv[2]
        password = sys.argv[3]
        create_admin_user(name, email, password)
