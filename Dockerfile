# Base Image
FROM python:3.12.4-slim-bookworm

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 로그를 저장할 외부 경로는 /logs로 설정
VOLUME ["/logs"]

# uvicorn으로 FastAPI 애플리케이션 실행
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]