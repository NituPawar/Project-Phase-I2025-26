from app import db, User, app
import bcrypt

def create_admin_user(name, email, password):
    with app.app_context():
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            print(f"User with email {email} already exists.")
            return
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        admin_user = User(name=name, email=email, password=hashed_password, is_admin=True)
        db.session.add(admin_user)
        db.session.commit()
        print(f"Admin user {name} created successfully.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python3 create_admin_user.py <name> <email> <password>")
    else:
        name = sys.argv[1]
        email = sys.argv[2]
        password = sys.argv[3]
        create_admin_user(name, email, password)
