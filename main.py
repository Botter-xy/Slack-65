import nextcord
from nextcord.ext import commands
import config

intents = nextcord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

bot.load_extension('commands')
bot.run(config.DISCORD_TOKEN)

# -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -     -
