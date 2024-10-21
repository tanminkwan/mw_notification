from fastapi import FastAPI, Request
import logging
import os
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
import pytz

app = FastAPI()

# 환경 변수로부터 타임존과 로그 파일 이름 가져오기
timezone_env = os.getenv("TIMEZONE", "Asia/Seoul")  # 기본값: Asia/Seoul
log_filename_env = os.getenv("LOG_FILENAME", "notifications.log")

# 타임존 설정
seoul_tz = pytz.timezone(timezone_env)

# 로그 파일 설정
#log_dir = "/home/hennry/GitHub/logs"
log_dir = "/logs"  # Docker 컨테이너 외부 파일 시스템과 연결될 경로
os.makedirs(log_dir, exist_ok=True)

def get_log_filename():
    return os.path.join(log_dir, log_filename_env)

# TimedRotatingFileHandler 사용
log_handler = TimedRotatingFileHandler(get_log_filename(), when="midnight", interval=1, backupCount=0)
log_handler.suffix = "%Y%m%d"
log_handler.extMatch = r"^\d{8}$"

# 로그 포맷 지정
formatter = logging.Formatter('%(asctime)s - %(message)s')
formatter.converter = lambda *args: datetime.now(seoul_tz).timetuple()  # 타임존 적용
log_handler.setFormatter(formatter)

logger = logging.getLogger("notification_logger")
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

@app.post("/notification")
async def log_notification(request: Request):
    try:
        # JSON 데이터 받기
        data = await request.json()
        # 로그 파일에 기록
        logger.info(f"Received data: {data}")
        return {"status": "success", "message": "Data logged successfully."}
    except Exception as e:
        logger.error(f"Error logging data: {e}")
        return {"status": "error", "message": "Failed to log data."}

# 서버 실행
# uvicorn 파일명:app --reload
