from envparse import env


env.read_envfile()
BOT_TOKEN = env('BOT_TOKEN', cast=str, default='')
