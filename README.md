# Currency Master Bot

<div style="display: flex; justify-content: center;">
  <img src="https://github.com/GepardXXX/Currency-Master-bot/blob/main/logo.png)" alt="Currency Rate Bot" style="margin-bottom: 10px;">
</div>



[![GitHub license](https://img.shields.io/github/license/GepardXXX/Currency-Master-bot.svg?style=plastic)](https://github.com/GepardXXX/Currency-Master-bot/blob/main/LICENSE)
[![GitHub release](https://img.shields.io/github/release/GepardXXX/Currency-Master-bot.svg?style=plastic)](https://github.com/GepardXXX/Currency-Master-bot/releases)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python)](https://www.python.org/downloads/release/python-3100/)
[![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue.svg?logo=telegram)](https://t.me/test32309518_bot)
![GitHub repo size](https://img.shields.io/github/repo-size/GepardXXX/Currency-Master-bot?style=plastic)

[![GitHub Stars](https://img.shields.io/github/stars/GepardXXX/Currency-Master-bot.svg?style=social&label=Stars)](https://github.com/GepardXXX/Currency-Master-bot/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/GepardXXX/Currency-Master-bot.svg?style=social&label=Watchers)](https://github.com/GepardXXX/Currency-Master-bot/watchers)

### О боте

***Currency Master*** - это удобный Telegram-бот, созданный для предоставления актуальных данных о курсах валют и простого выполнения конвертации между разными валютами. Бот разработан с целью обеспечить пользователей надежной информацией о финансовых рынках и упростить процесс валютных операций.

<details>
<summary><h2>Описание файлов</h2></summary>

- `bot/` - Пакет с ботом.
  - `bot.py` - Основной файл бота.
  - `handlers/` - Обработчики команд и callback-запросов.
    - `commands/` - Обработчики команд.
      - `start.py` - Обработчик команды /start.
      - `help.py` - Обработчик команды /help.
      - `convert.py` - Обработчик команды /convert.
      - `course.py` - Обработчик команды /course.
    - `callbacks/` - Обработчики callback-запросов.
      - `amount_selection_handler.py` - Обработчик ввода суммы во время конвертации.
      - `back_button_handlers.py` - Обработчики кнопки "Назад" в разных состояниях.
      - `conversion_handler.py` - Обработчик выбора конверсии валют.
      - `currency_handler.py` - Обработчик запросов на отображение текущего курса выбранной валюты.
  - `keyboards/` - Клавиатуры для бота.
    - `back_button.py` - Кнопка "Назад" для использования в инлайн-клавиатуре.
    - `conversion_keyboards.py` - Клавиатуры для выбора конверсии валют.
    - `currency_selection_buttons.py` - Клавиатуры для выбора валюты.
    - `amount_keyboard.py` - Клавиатура для ввода суммы во время конвертации.
  - `states/` - Состояния для управления процессом конвертации.
  - `texts/` - Текстовые сообщения, используемые в боте.
- `config/` - Конфигурационные файлы.
  - `settings.py` - Настройки бота.
- `utils/` - Утилиты для работы с ботом.
  - `currency_course.py` - Утилита для получения и обработки данных о курсах валют.
- `README.md` - Описание проекта и инструкции по его использованию.
- `LICENSE` - Лицензия проекта.
- `main.py` - Основной файл для запуска бота.
- `requirements.txt` - Зависимости проекта.

</details>


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
   
   Откройте файл `config/settings.py` и вставьте ваш токен бота в поле **TOKEN**. В этом файле также можно настроить другие параметры, если необходимо.

   ```c++
   # config/settings.py

   TOKEN = 'YOUR_TOKEN_HERE'
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

