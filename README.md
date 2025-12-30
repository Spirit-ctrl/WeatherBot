# 🌤 WeatherBot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success)
![GitHub repo size](https://img.shields.io/github/repo-size/Spirit-ctrl/WeatherBot)
![GitHub last commit](https://img.shields.io/github/last-commit/Spirit-ctrl/WeatherBot)

**WeatherBot** — это простой и удобный бот на Python для получения актуальной информации о погоде в любом городе мира.

---

## 🚀 Возможности

- 🌍 Получение текущей погоды по названию города  
- 🌡 Температура, влажность, скорость ветра  
- ☁️ Краткое описание погодных условий  
- ⚙️ Лёгкая настройка через `.env`  
- 🧩 Простая архитектура — легко расширять  

---

## 📂 Структура проекта

```
WeatherBot/
│
├── app/
│   └── main.py
│
├── .env.example
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠 Установка

```bash
git clone https://github.com/Spirit-ctrl/WeatherBot.git
cd WeatherBot
```

```bash
python -m venv venv
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

---

## ⚙️ Настройка

```env
TOKEN= 8575800527:***********************************
API_TOKEN=d0cd3c**************************


DB_HOST = localhost
DB_PORT = 5432
DB_NAME = postgres
DB_USER = postgres
DB_PASSWORD = 0102

```

---

## ▶️ Запуск

```bash
python app/main.py
```

---

## 📌 Пример вывода

```
🌤 Погода в городе: London
🌡 Температура: 18°C
💧 Влажность: 62%
💨 Ветер: 4.5 м/с
☁️ Описание: облачно
```

---

## 📄 Лицензия

Проект распространяется под лицензией MIT.
