# Используем официальный Python 3.13 в минимальном варианте
FROM python:3.13-slim

# Рабочая директория внутри контейнера
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы (ваши скрипты)
COPY . .

# Запускаем основной скрипт
CMD ["python", "main.py"]