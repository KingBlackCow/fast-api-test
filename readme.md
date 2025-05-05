# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate

# 이제 pip 사용 가능
pip install uvicorn fastapi


# db 마이그레이션 (alembic)
```
pip install alembic
alembic init alembic
```

pip install 'dotenv'
pip install 'aiomysql'
pip install 'greenlet'
```
alembic revision --autogenerate -m "Add age column to user" # 마이그레이션 파일 생성
alembic upgrade head # db 반영
```