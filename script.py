import discord
from discord.ext import commands
import mysql.connector
import secrets
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_DATABASE = os.environ.get('DB_DATABASE')

BOT_TOKEN = os.environ.get('BOT_TOKEN')

db_connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_DATABASE
)

db_cursor = db_connection.cursor()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    print("Message Content:", message.content)
    
    if message.author == bot.user:
        return

    if message.content.startswith('!bot'):
        if message.guild:
            server_name = message.guild.name
            print("Message Guild:", message.guild)

            user_id = str(message.author.id)
            guild_id = str(message.guild.id)

            if await is_valid_token(user_id, guild_id):
                await message.channel.send(f'Hello world, {server_name}!')
            else:
                token = generate_token()
                store_token(user_id, guild_id, token)
                await message.channel.send('Token generated and stored. Please try messaging again.')

async def is_valid_token(user_id, guild_id):
    db_cursor.execute("SELECT token FROM tokens WHERE user_id = %s AND guild_id = %s", (user_id, guild_id))
    result = db_cursor.fetchone()
    return result is not None


def generate_token():
    return secrets.token_urlsafe(16)

def store_token(user_id, guild_id, token):
    db_cursor.execute("INSERT INTO tokens (user_id, guild_id, token) VALUES (%s, %s, %s)", (user_id, guild_id, token))
    db_connection.commit()

bot.run(BOT_TOKEN)