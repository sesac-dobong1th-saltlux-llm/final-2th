import os
import sys
from datetime import datetime

import openai
from passlib.hash import bcrypt
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from db.database import SessionLocal, engine, Base
from db.models import User, Chatroom, Dialogue
import recommend_house

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "static")), name="static")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/login', response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})

@app.get('/sign_in', response_class=HTMLResponse)
def sign_in(request: Request):
    return templates.TemplateResponse('sign_in.html', {'request': request})

@app.post("/input_process", response_class=JSONResponse)
async def chat(request: Request, user_input: str = Form(...)):
    try:
        response = recommend_house.question_answering(user_input)
        return JSONResponse({"message": response})
    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse({"message": str(e)}, status_code=500)

@app.post("/process_signup", response_class=RedirectResponse)
async def process_signup(request: Request, email: str = Form(...), password: str = Form(...), name: str = Form(...), db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.user_id == email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")

        new_user = User(
            user_id=email,  # user_id 대신 email을 사용하거나 로직에 따라 조정
            password=bcrypt.hash(password),
            name=name
            # email=email,
            # registered_on=datetime.utcnow()
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # 회원가입 후 로그인 페이지로 리다이렉트
        return RedirectResponse(url='/login', status_code=303)
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemy Error: {str(e)}")
        return JSONResponse({"message": "회원가입에 실패했습니다.", "error": str(e)}, status_code=500)

@app.post('/process_login', response_class=RedirectResponse)
async def process_index(request: Request):
    return RedirectResponse(url='/', status_code=303)