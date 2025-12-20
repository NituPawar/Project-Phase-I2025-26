from app import db, User, app
import bcrypt

def verify_login(email, password):
    with app.app_context():
        user = User.query.filter_by(email=email).first()
        if not user:
            print("User not found.")
            return False
        if user.check_password(password):
            print(f"Login successful for user: {user.name}, Admin: {user.is_admin}")
            return True
        else:
            print("Invalid password.")
            return False

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 verify_login.py <email> <password>")
    else:
        email = sys.argv[1]
        password = sys.argv[2]
        verify_login(email, password)
