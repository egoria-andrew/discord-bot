# Discord Story Bot

A small interactive Discord bot built with Python and `discord.py`. It includes a few playful commands and a simple story game where users can begin a story and make choices like "left" or "right".

## Features

- Bot online status message
- `!hello` command for a quick check
- `!story` command to start a generated story
- `!choose <left|right>` command to continue the narrative
- `!chat <message>` command with simple keyword-based responses
- Lightweight, beginner-friendly Python code

## Requirements

- Python 3.9+
- A Discord bot token
- `discord.py`
- `python-dotenv`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/egoria-andrew/discord-bot.git
cd discord-bot
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a file named `token.env` in the project root with your Discord bot token:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```

Important: do not commit real secrets to GitHub. The repository already ignores `token.env` and `.env` files.

## Running the Bot

Start the bot with:

```bash
python bot.py
```

If the bot starts successfully, it will print a message showing the bot account it connected as.

## Bot Commands

```text
!hello
!story
!choose left
!choose right
!chat hello
!chat python
!chat discord
```

## Project Structure

```text
discord-bot/
├── bot.py
├── requirements.txt
├── .gitignore
├── token.env
└── README.md
```

## Notes

- This bot is meant for learning and experimentation.
- The story system and chat responses are intentionally simple and easy to expand.
- If you want to add more commands, story events, or better AI-like responses, this is a good base to build on.

## License

This project is provided as-is for educational and personal use.

## Troubleshooting

If the bot does not start:

- Make sure your Discord token is valid
- Make sure `discord.py` is installed
- Check that the `token.env` file is in the project root
- Ensure your bot has the required gateway permissions in the Discord Developer Portal

## Security Reminder

Never upload a real bot token to GitHub. Always keep tokens in local environment files and make sure they are listed in `.gitignore`.
