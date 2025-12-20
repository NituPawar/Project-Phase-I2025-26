#!/usr/bin/env python3
"""
create_admin_mongo.py

Utility to create or promote a user to admin in the MongoDB used by the app.
Usage:
  python create_admin_mongo.py --email admin@example.com --password MySecret123 --name "Admin Name"
If password is not provided, you'll be prompted to enter one interactively.

This script uses the same MongoDB Atlas URI configured in `app.py`.
"""
import argparse
import getpass
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import sys

MONGO_URI = "mongodb+srv://suhaninaidu2003_db_user:suhani%40123@jamasya.mzm5dyx.mongodb.net/jamasya_db?retryWrites=true&w=majority"


def create_admin(name: str, email: str, password: str):
    try:
        client = MongoClient(MONGO_URI)
        db = client.jamasya_db
        users = db.users

        existing = users.find_one({'email': email})
        hashed = generate_password_hash(password)

        if existing:
            update_doc = {'$set': {'is_admin': True}}
            # update name/password if provided
            if name:
                update_doc['$set']['name'] = name
            if password:
                update_doc['$set']['password'] = hashed
            users.update_one({'email': email}, update_doc)
            print(f"Updated existing user '{email}' as admin.")
        else:
            user_doc = {
                'name': name or '',
                'email': email,
                'password': hashed,
                'is_admin': True
            }
            users.insert_one(user_doc)
            print(f"Created admin user '{email}'.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create or promote a MongoDB user to admin for the grievance app')
    parser.add_argument('--name', '-n', help='Full name of the admin user', default='Admin')
    parser.add_argument('--email', '-e', help='Email address for admin user', required=True)
    parser.add_argument('--password', '-p', help='Password for admin user (if omitted, prompted)', required=False)

    args = parser.parse_args()

    pwd = args.password
    if not pwd:
        try:
            pwd = getpass.getpass(prompt='Enter password for admin user: ')
            pwd_confirm = getpass.getpass(prompt='Confirm password: ')
            if pwd != pwd_confirm:
                print('Passwords do not match. Aborting.')
                sys.exit(1)
        except Exception:
            print('Failed to read password interactively. Provide --password to the command.')
            sys.exit(1)

    create_admin(args.name, args.email, pwd)
