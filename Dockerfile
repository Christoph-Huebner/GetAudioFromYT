# Use a lightweight Python image
FROM python:3.10-slim

WORKDIR /app

COPY pip-packages.txt /app/

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r pip-packages.txt \
    && apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY  *.py /app/

RUN useradd --create-home appuser \
    && chown -R appuser:appuser /app
USER appuser

ENTRYPOINT ["python", "main.py"]
