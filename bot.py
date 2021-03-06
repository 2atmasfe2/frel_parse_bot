import gmail_analysis
from telegram import Bot
from time import sleep
from telegram.utils.request import Request
from telegram.ext import Updater
import threading

hat_id = 0000000000  # chat_id для line 17

# функция, опрашивающая функцию gmail_analysis
def gmail_checking():
    while True:
        mails = gmail_analysis.analize()
        if mails:
            for mail in mails:
                Bot.send_message(chat_id=hat_id, text=mail)
        sleep(0.1)


t = threading.Thread(target=gmail_checking, args=())  # Запуск функции в отдельном потоке
t.start()

# Скелет бота
def main():
    req = Request(
        connect_timeout=0.5,
    )

    bot = Bot(
        request=req,
        token='###',  # Токен для бота
        base_url='###',  # Проксирующий URL
    )

    updater = Updater(
        bot=bot,
        use_context=True,
    )

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()



