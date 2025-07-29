# 🌈Discord Role Color Changer Bot

This bot automatically changes the color of a specified role in your Discord server every second, cycling through a preset list of colors. It also includes a `/say` slash command to make the bot repeat any message you want🥰.

---

## Setup Instructions 📝

1. **Clone the repository or download the `bot.py` file🤖.**

2. **Install dependencies👾**

Make sure you have Python 3.8 or newer installed⚠.

`pip install -U discord.py`

3. **Configure your bot🧰**

Open bot.py

Replace the placeholders with your own information:

GUILD_ID = YOUR_GUILD_ID_HERE       # Your Discord server ID (integer)
ROLE_ID = YOUR_ROLE_ID_HERE         # The role ID to change colors (integer)
TOKEN = 'YOUR_BOT_TOKEN_HERE'       # Your Discord bot token (string)

You can get these IDs by enabling Developer Mode in Discord (Settings > Advanced > Developer Mode), right-clicking your server or role, and selecting "Copy ID".

4. **Run the bot🏃‍♂️**

`python bot.py`

**Invite your bot to your server 📩**

**Make sure your bot has the following permissions⚠:**

Manage Roles (to change role colors)

Read Messages/View Channels

Send Messages

Use Slash Commands

Use this OAuth2 URL Generator to create an invite link:

Scopes: bot, applications.commands

Bot Permissions: Manage Roles, Send Messages
