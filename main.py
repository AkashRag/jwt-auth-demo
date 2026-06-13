import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends , HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta

app= FastAPI()

load_dotenv()

#__________Configuration__________
Secret_Key = "my secret_key123"
Algorithm = "HS256"
Access_Token_Expire_Minutes = 30

#________Setup__________

app= FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

#_______fake database_________

fake_users_db = {}



#__________Models__________
class User(BaseModel):
    Username: str
    password: str

# ─── JWT Token Function ───────────────
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=Access_Token_Expire_Minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, Secret_Key, algorithm=Algorithm)
    return encoded_jwt

#__________Register EndPoint__________
@app.post("/register")
def register(user: User):
    if user.Username in fake_users_db:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    hashed_password = pwd_context.hash(user.password)
    fake_users_db[user.Username] = hashed_password

    return {"message": "User registered successfully"}


# ─── Login Endpoint ───────────────────
@app.post("/login")
def login(user: User):
    if user.Username not in fake_users_db:
        raise HTTPException(status_code=401, detail="Invalid username")
    
    hashed_password = fake_users_db[user.Username]
    
    if not pwd_context.verify(user.password, hashed_password):
        raise HTTPException(status_code=401, detail="Invalid password")
    
    access_token = create_access_token(data={"sub": user.Username})
    
    return {"access_token": access_token, "token_type": "bearer"}

# ─── Verify Token Function ────────────
def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, Secret_Key, algorithms=[Algorithm])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


# ─── Protected Route ──────────────────
@app.get("/profile")
def profile(current_user: str = Depends(get_current_user)):
    return {"message": f"Welcome {current_user}! This is a protected route."}








    