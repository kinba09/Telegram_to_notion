from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import notion_back
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


def handle_response(text: str) -> str:
    processed: str = text.lower()
    return processed


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    print(f'User ({update.message.chat.id}): "{text}"')
    response: str = handle_response(text)
    print('Bot:', response)
    notion_back.note(text)
    await update.message.reply_text(response)


# Start the bot
if __name__ == '__main__':
    bot = Application.builder().token(TELEGRAM_TOKEN).build()
    bot.add_handler(CommandHandler('start', start_command))
    bot.add_handler(MessageHandler(filters.TEXT, handle_message))
    bot.run_polling(poll_interval=5)

#os child, aws landa 
