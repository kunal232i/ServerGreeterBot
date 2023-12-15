# ServerGreeterBot

ServerGreeterBot is a Discord bot written in Python that greets users with a "Hello World" message when called. The bot authenticates into a Discord server and prints a greeting message along with the server name when invoked.

## Installation

1. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Set up a MySQL database with the provided script (`create_db.py`).

3. Create a `.env` file in the project root and fill in the following information:
   ```env
   DB_HOST=your_mysql_host
   DB_USER=your_mysql_user
   DB_PASSWORD=your_mysql_password
   DB_DATABASE=your_mysql_database
   BOT_TOKEN=your_discord_bot_token
   ```

## Database Setup

Run the `create_db.py` script to create the necessary MySQL database and tables for storing authentication tokens.

```bash
python create_db.py
```

## Usage

Run the `script.py` to start the ServerGreeterBot:

```bash
python script.py
```

The bot will log in, and you will see "Logged in as {bot_username}" in the console.

## Commands

- `!bot`: Call this command in a Discord server to trigger the bot. The bot will check if it has a valid authentication token for the user and the server. If a valid token is found, it greets the server with "Hello World." If not, it generates a new token and stores it for future use.
