from flask_bcrypt import Bcrypt
from app import app

bcrypt = Bcrypt(app)

def password_hashing(password):
    pas = bcrypt.generate_password_hash(password).decode('UTF-8')
    return pas

def hash_checking(hash, password):
    return bcrypt.check_password_hash(pw_hash=hash, password=password)