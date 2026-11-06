FROM node:22-alpine AS frontend-build

WORKDIR /frontend

COPY frontend/package*.json ./
RUN npm ci

COPY frontend/ ./
RUN npm run build


FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=8000

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpcap-dev \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY backend/requirements.txt ./backend/requirements.txt

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r ./backend/requirements.txt

COPY backend/ ./backend/

COPY --from=frontend-build /frontend/dist/ ./frontend/dist/

COPY data/ ./data/
COPY scripts/ ./scripts/
COPY docs/ ./docs/
COPY start.py ./start.py

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/api/health || exit 1

CMD ["python", "start.py"]
