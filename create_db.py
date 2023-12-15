import mysql.connector
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

# Create database
db_cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")

# use mydatabase;
db_cursor.execute("USE mydatabase")

# Create tokens table
db_cursor.execute("CREATE TABLE IF NOT EXISTS tokens (user_id VARCHAR(255), guild_id VARCHAR(255), token VARCHAR(255), PRIMARY KEY (user_id, guild_id))")

# check tokens table
db_cursor.execute("select * from tokens")