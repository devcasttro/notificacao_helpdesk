import asyncio
from telegram import Bot
from telegram.error import TelegramError

async def send_html_message(token, chat_id, message):
    bot = Bot(token=token)

    try:
        # Envia a mensagem formatada
        await bot.send_message(chat_id=chat_id, text=message, parse_mode='HTML')
        print("Mensagem enviada com sucesso!")
    except TelegramError as e:
        # Trate o erro e exiba uma mensagem informando o problema
        print(f"Ocorreu um erro ao enviar a mensagem: {e}")

# Função de conveniência para chamar a função assíncrona de forma síncrona
def send_notification(token, chat_id, message):
    asyncio.run(send_html_message(token, chat_id, message))
