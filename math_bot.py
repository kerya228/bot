math_bot.py
pip install python-telegram-bot sympy
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import sympy as sp

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот, который решает математические задачи. Просто напиши мне пример, и я постараюсь его решить.')

# Функция для обработки текстовых сообщений
def solve_math(update: Update, context: CallbackContext) -> None:
    try:
        # Получаем текст сообщения от пользователя
        user_input = update.message.text
        
        # Пытаемся решить математическое выражение
        result = sp.sympify(user_input)
        
        # Отправляем результат пользователю
        update.message.reply_text(f'Результат: {result}')
    except Exception as e:
        # Если что-то пошло не так, отправляем сообщение об ошибке
        update.message.reply_text(f'Ошибка: {e}')

def main() -> None:
    # Вставьте сюда ваш токен
    updater = Updater("7603215514:AAHanVMz4teSp1pQq4tgG1P_3OyHteCn1HQ")

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))
    
    # Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, solve_math))

    # Запускаем бота
    updater.start_polling()

    # Работаем до тех пор, пока не будет нажата комбинация Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
    
