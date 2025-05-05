# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate

# FastAPI 및 실행 서버(Uvicorn) 설치
```
pip install uvicorn fastapi
```

# db 마이그레이션 (alembic)
```
pip install alembic
alembic init alembic
alembic revision --autogenerate -m "Add age column to user" # 마이그레이션 파일 생성
alembic upgrade head # db 반영
```

# 각종 라이브러리 
```
pip install 'dotenv' # 환경구성
pip install 'aiomysql' # mysql 비동기 연결 
pip install 'greenlet' # 비동기 동작을 위한 가벼운 컨텍스트 전환 도구
```
