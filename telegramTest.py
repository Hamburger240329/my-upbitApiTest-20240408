# pip tnstall python-telegram-bot

import telegram
import asyncio

bot = telegram.Bot(token="7145450371:AAHk1TnNGgnEJuGbZQr_gq-IGMa_P3M0zKY")
chat_id = "5373442259"

asyncio.run(bot.sendMessage(chat_id=chat_id, text="안녕하세요!! 파이썬 텔레그램 테스트!!!"))




