# 가상환경 생성
python3 -m venv venv

# 가상환경 활성화
source venv/bin/activate

# 이제 pip 사용 가능
pip install uvicorn fastapi

pip install greenlet