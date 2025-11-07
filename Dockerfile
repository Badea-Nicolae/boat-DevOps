# Imagine de bază mică, cu Python
FROM python:3.10-slim

# Creează directorul de lucru în container
WORKDIR /app

# Copiem requirements întâi (cache mai bun la build)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Apoi copiem codul aplicației
COPY app/ /app/app

# Portul pe care rulează Uvicorn
EXPOSE 8000

# Comanda de start a API-ului FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
