import jwt
import datetime
from app.config import Config
from app.models.user import User

def generate_jwt_token(username):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    payload = {'username': username, 'exp': expiration_time}
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

def verify_jwt_token(token):
    try:
        return jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
