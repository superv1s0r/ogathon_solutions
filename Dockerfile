FROM python:3.11-slim

WORKDIR /app

# Copiamos solo requirements primero para aprovechar cacheo de Docker
COPY src/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Luego copiamos todo el código
COPY . .

# Exponemos el puerto 8080
EXPOSE 8080

# Lanzamos el servidor en el puerto 8080
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]

