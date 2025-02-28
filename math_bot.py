python math_bot.py
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

# Функция для обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Привет! Я бот, который решает математические задачи и уравнения. '
        'Просто напиши мне уравнение, например: "x**2 - 4 = 0", и я решу его.'
    )

# Функция для решения уравнений
def solve_equation(equation: str) -> str:
    try:
        # Разделяем уравнение на левую и правую части
        left, right = equation.split('=')
        left = left.strip()
        right = right.strip()

        # Преобразуем строки в символьные выражения
        x = sp.symbols('x')
        expr = sp.sympify(left) - sp.sympify(right)

        # Решаем уравнение
        solution = sp.solve(expr, x)

        # Форматируем ответ
        if not solution:
            return "Уравнение не имеет решений."
        elif len(solution) == 1:
            return f"Решение: x = {solution[0]}"
        else:
            return f"Решения: {', '.join([f'x = {sol}' for sol in solution])}"
    except Exception as e:
        return f"Ошибка: {e}"

# Функция для обработки текстовых сообщений
def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text

    # Если пользователь ввёл уравнение
    if '=' in user_input:
        result = solve_equation(user_input)
        update.message.reply_text(result)
    else:
        # Если это просто математическое выражение
        try:
            result = sp.sympify(user_input)
            update.message.reply_text(f"Результат: {result}")
        except Exception as e:
            update.message.reply_text(f"Ошибка: {e}")

def main() -> None:
    # Вставьте сюда ваш токен
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчики команд
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Запускаем бота
    updater.start_polling()

    # Работаем до тех пор, пока не будет нажата комбинация Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
    
