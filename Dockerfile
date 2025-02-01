# Python rasmiy image dan foydalanamiz
FROM python:3.9-slim

# Ishchi direktoriyani yaratamiz
WORKDIR /app

# requirements.txt ni kopiya qilamiz va o'rnatamiz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Barcha loyiha fayllarini kopiya qilamiz
COPY . .

# Port ni ochib qo'yamiz
EXPOSE 8000

# Gunicorn ni ishga tushiramiz
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
