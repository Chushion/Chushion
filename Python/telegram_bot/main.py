import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

telegram_api_token = os.getenv("7462803038:AAE-gyEDeC2TTJFD_bCPfj6PX-xD80jp2u0")

class TelegramBotHandler:
    @classmethod
    async def help(cls, update: Update, context: ContextTypes.DEFAULT_TYPE):
        msg = "안녕하세요. 반갑습니다!!! 저는 사용자분의 '/help' 명령에 의해 답변드립니다."
        await update.message.reply_text(msg)

def main():
    try:
        application = ApplicationBuilder().token(telegram_api_token).build()
        application.add_handler(CommandHandler('help', TelegramBotHandler.help))
        application.run_polling()
    except KeyboardInterrupt:
        return True

if __name__ == '__main__':
    main()