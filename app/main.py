from fastapi import FastAPI, HTTPException,status, Depends
from sqlalchemy.orm import Session
from database import engine, Base ,get_db
import models,schemas
from fastapi.security import OAuth2PasswordRequestForm
from auth import hash_password, verify_password
from jwt import create_access_token
from deps import get_current_user
from chatbot import model
from routers import chat
from fastapi.middleware.cors import CORSMiddleware


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(chat.router)



# User registration endpoint

@app.post("/register",response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()

    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    
    hashed_pwd = hash_password(user.password)
    new_user = models.User(username=user.username, password=hashed_pwd) 
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#login endpoint

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user= db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Get current user endpoint

@app.get("/me", response_model=schemas.UserResponse)
def read_current_user(current_user: models.User = Depends(get_current_user)):
    return{"id": current_user.id, "username": current_user.username}


# Generate text using the chatbot model

@app.post("/test")
def generate_text(prompt: str):
    output = model.text_generator(
        prompt,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.7
    )

    return {"response": output[0]["generated_text"]}