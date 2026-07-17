FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .
COPY uv.lock .

RUN pip install --no-cache-dir uv

RUN uv sync --frozen --no-dev

COPY . .

CMD ["uv", "run", "python", "main.py"]