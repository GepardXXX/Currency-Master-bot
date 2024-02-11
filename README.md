# Currency Master Bot

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/GepardXXX/Currency-Master-bot/aiogram3.x/logo.png" alt="Currency Rate Bot" style="margin-bottom: 10px;">
</div>



[![GitHub license](https://img.shields.io/github/license/GepardXXX/Currency-Master-bot.svg?style=plastic)](https://github.com/GepardXXX/Currency-Master-bot/blob/aiogram3.x/LICENSE)
[![GitHub release](https://img.shields.io/github/release/GepardXXX/Currency-Master-bot.svg?style=plastic)](https://github.com/GepardXXX/Currency-Master-bot/releases)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python)](https://www.python.org/downloads/release/python-3100/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram)](https://t.me/test32309518_bot)
![GitHub repo size](https://img.shields.io/github/repo-size/GepardXXX/Currency-Master-bot?style=plastic)

[![GitHub Stars](https://img.shields.io/github/stars/GepardXXX/Currency-Master-bot.svg?style=social&label=Stars)](https://github.com/GepardXXX/Currency-Master-bot/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/GepardXXX/Currency-Master-bot.svg?style=social&label=Watchers)](https://github.com/GepardXXX/Currency-Master-bot/watchers)

### О боте

***Currency Master*** - это удобный Telegram-бот, созданный для предоставления актуальных данных о курсах валют и простого выполнения конвертации между разными валютами. Бот разработан с целью обеспечить пользователей надежной информацией о финансовых рынках и упростить процесс валютных операций.

<details>

<summary><h2>Инструкция для пользователя</h2></summary>

Для начала работы с ботом, перейдите по ссылке [Currency Master в Telegram](https://t.me/test32309518_bot) или найдите его в Telegram, введя его имя в поиске.

### Команды

- `/start`: Начать общение с ботом. Бот приветствует вас и предоставляет доступ к основным функциям.
- `/help`: Получить справку о доступных командах.
- `/convert`: Начать процесс конвертации валют.
- `/course`: Получить текущий курс валют

</details>


<details> 

<summary><h2>Инструкция для разработчика</h2></summary>

Если вы разработчик и хотите запустить этого бота на своем компьютере, выполните следующие шаги:

1. **Клонируйте репозиторий**

   Сначала клонируйте репозиторий на свой компьютер с помощью Git. Откройте терминал или командную строку и выполните следующую команду:

   ```bash
   git clone https://github.com/yourusername/currency-rate-bot.git
   ```

2. **Установите зависимости**
   
   Перейдите в каталог проекта, затем установите необходимые зависимости, указанные в файле `requirements.txt`, выполнив следующую команду:

   ```bash
   pip install -r requirements.txt
   ```

3. **Создайте бота в Telegram**
   
   Прежде чем вы сможете запустить бота, вам нужно создать бота в Telegram и получить токен. Для этого выполните следующие шаги:

    - Откройте Telegram и найдите *`BotFather`* – официального бота для создания других ботов в Telegram.
  
    - Напишите ему сообщение `/newbot` и следуйте инструкциям.
  
    - Выберите имя для вашего бота и получите уникальный токен.

4. **Настройте конфигурацию**
   
   Создайте файл `.env` и вставьте ваш токен бота в поле **BOT_TOKEN**. В этом файле также можно настроить другие параметры, если необходимо.

   ```c++
   # .env

   BOT_TOKEN = 'YOUR_TOKEN_HERE'
   ```

5. **Запустите бота**
   
   В терминале или в командной строке выполните следующую команду:

   ```bash
   python main.py
   ```
   Ваш бот будет запущен и готов к работе.

</details> 

<details> 

<summary><h2>Лицензия</h2></summary>

Этот проект распространяется под Лицензией **MIT**, которая позволяет вам свободно использовать, модифицировать и распространять его как в коммерческих, так и в некоммерческих целях.

**Важно:** При использовании или распространении этого кода, обязательно указывать [GepardXXX](https://github.com/GepardXXX) в качестве контрибьютора и сохранять указание оригинальной лицензии в вашем проекте.

</details> 

