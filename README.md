# FastAPI Notification Logging Service

This is a FastAPI-based service that accepts JSON data via a RESTful POST endpoint (`/notification`) and logs the data to a file. The log file name and timezone can be configured via environment variables.

## Features
- Accepts JSON payload via REST POST `/notification`.
- Logs data to a file with rotation at midnight.
- Supports configurable log file names and timezones via environment variables.
- Can be run in a Docker container with external volume for log storage.

## Prerequisites
- Python 3.9+
- Docker (if running in a container)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-notification-service.git
cd fastapi-notification-service
```

### 2. Install Dependencies

#### Locally:
Create a virtual environment and install the required packages:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

#### Docker:
Build the Docker image:

```bash
docker build -t fastapi-notification-app .
```

### 3. Environment Variables

The application uses the following environment variables:

- **`LOG_FILENAME`**: (Optional) The name of the log file. Default is `notifications.log`.
- **`TIMEZONE`**: (Optional) The timezone for logging timestamps. Default is `Asia/Seoul`.

### 4. Running the Application

#### Locally:
To run the application locally:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

#### Docker:
To run the application in a Docker container:

```bash
docker run -d -p 8000:8000 -v /home/hennry/GitHub/logs:/logs -e LOG_FILENAME=noti.log -e TIMEZONE=Asia/Seoul fastapi-notification-app
```

When running the Docker container, you can use the --user option to set the container's user to the current user's UID and GID. This will ensure that any files created inside the container (including log files) are owned by the user who started the Docker container :

```bash
docker run -d -p 8000:8000 -v /home/hennry/GitHub/logs:/logs -e LOG_FILENAME=noti.log -e TIMEZONE=Asia/Seoul --user $(id -u):$(id -g) fastapi-notification-app
```

### 5. Example Usage

You can test the `/notification` endpoint using `curl`:

```bash
curl -X POST "http://localhost:8000/notification" -H "Content-Type: application/json" -d '{"message": "Test notification", "type": "info"}'
```

## Code Explanation

### FastAPI Application (`app.py`)

The service sets up a FastAPI application that listens for POST requests at `/notification`. The payload is expected to be in JSON format, and upon receiving the data, it writes it to a log file. The log file's name and the timezone used for timestamps are configurable via environment variables.

### Dockerfile

The Docker container is set up to:
1. Install necessary dependencies.
2. Use `/logs` as an external volume for log storage, allowing logs to be stored outside the container.
3. Allow configuration via environment variables passed during runtime.

### `requirements.txt`

The dependencies include:
- **`fastapi`**: For creating the RESTful API.
- **`uvicorn`**: For running the ASGI server.
- **`pytz`**: For handling timezones.

### Timezone Configuration

The default timezone is set to `Asia/Seoul`. To change the timezone, set the `TIMEZONE` environment variable. For example, you can use `America/New_York`, `Europe/London`, etc. The full list of supported timezones can be found in the [pytz documentation](https://pythonhosted.org/pytz/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


### 설명
- 이 `README.md` 파일은 프로젝트의 설치 방법, 설정 방법, 실행 방법, 그리고 주요 기능 설명을 포함하고 있습니다.
- `Docker`, `curl`, 환경 변수 사용법 등 필요한 모든 정보를 한눈에 볼 수 있게 정리했습니다.