from datetime import datetime, timedelta, timezone
from typing import Any, Union
import jwt
import bcrypt
import hashlib
from app.core.config import settings

def _hash_password_bytes(password: str) -> bytes:
    # Use sha256 to produce a 64-character hex digest, safely under bcrypt's 72-byte limit
    return hashlib.sha256(password.encode("utf-8")).hexdigest().encode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        pw_bytes = _hash_password_bytes(plain_password)
        hashed_bytes = hashed_password.encode("utf-8")
        return bcrypt.checkpw(pw_bytes, hashed_bytes)
    except Exception:
        return plain_password == hashed_password

def get_password_hash(password: str) -> str:
    pw_bytes = _hash_password_bytes(password)
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pw_bytes, salt).decode("utf-8")

def create_access_token(subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None
