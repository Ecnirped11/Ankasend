import os
from dotenv import load_dotenv
from bot.bot import SMSSenderBot
from telegram.error import TimedOut, BadRequest

load_dotenv()

def main() -> None:

    ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
    
    try:
        sms_sender_bot =  SMSSenderBot(ACCESS_TOKEN)
        sms_sender_bot.run_bot()
    except TimedOut:
        pass

if __name__ == '__main__':
    main()