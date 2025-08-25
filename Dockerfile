# версия пайтон
FROM python:3.11-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем все файлы проекта внутрь контейнера
COPY . .

# Обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Команда запуска бота
CMD ["python", "eco_bot.py"]