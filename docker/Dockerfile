FROM python:3.11-slim

WORKDIR /app

COPY . /app

ENV PYTHONUNBUFFERED=1 \
    AIRS_CONFIG=/app/config/airs.yaml \
    AIRS_WORKSPACE_DIR=/app/workspace-data \
    AIRS_CACHE_DIR=/app/.cache/airs

EXPOSE 8765 8080

CMD ["python3", "api/server.py", "--host", "0.0.0.0", "--port", "8765"]

