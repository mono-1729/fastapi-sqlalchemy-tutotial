from fastapi import FastAPI, Depends, HTTPException  # new
from fastapi.security import HTTPBasic, HTTPBasicCredentials  # new
 
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED  # new
 
import db  # new
from models import User, Task  # new
 
import hashlib  # new

app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
    version='0.9 beta'
)

templates = Jinja2Templates(directory='templates')

jinja_env = templates.env

def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request':request})

def admin(request:Request):
    # ユーザとタスクを取得
    # とりあえず今はadminユーザのみ取得
    user = db.session.query(User).filter(User.username == 'admin').first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
    db.session.close()
    return templates.TemplateResponse('admin.html',
                                      {'request':request,
                                       'user':user,
                                       'task':task
                                       })