FROM python:3.11-slim

WORKDIR /app

ARG APP_VERSION
ARG GIT_COMMIT
ARG REPOSITORY
ARG BUILD_DATE

LABEL org.opencontainers.image.version=$APP_VERSION
LABEL org.opencontainers.image.revision=$GIT_COMMIT
LABEL org.opencontainers.image.source=$REPOSITORY
LABEL org.opencontainers.image.created=$BUILD_DATE

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]