from app.bot import AndHisNameIs
from settings import BOT_TOKEN


def main():
    bot = AndHisNameIs()
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
