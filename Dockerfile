# Obraz bazowy
FROM python:3.11-slim

# Ustawienie folderu roboczego
WORKDIR /app

# Instalacja zależności systemowych (potrzebne do bazy danych)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Kopiowanie listy bibliotek i ich instalacja
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiowanie reszty plików projektu
COPY . .

CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT"