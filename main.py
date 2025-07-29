import discord
from discord.ext import tasks
from discord import app_commands
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# Replace these with your own IDs and token before running
GUILD_ID = YOUR_GUILD_ID_HERE       # int: Your Discord server (guild) ID
ROLE_ID = YOUR_ROLE_ID_HERE         # int: Role ID whose color you want to change
TOKEN = 'YOUR_BOT_TOKEN_HERE'       # str: Your bot token

colors = ['#ff0000', '#ff4000', '#ff8000', '#ffbf00', '#ffff00', '#bfff00', '#80ff00', '#40ff00', '#00ff00', '#00ff40', '#00ff80', '#00ffbf', '#00ffff', '#00bfff', '#0080ff', '#0040ff', '#0000ff', '#4000ff', '#8000ff', '#bf00ff', '#ff00ff', '#ff00bf', '#ff0080', '#ff0040', '#ffc0cb', '#ff69b4', '#db7093', '#7600bc']

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # Sync slash commands globally
        await self.tree.sync()
        print("✅ Slash commands synced globally.")

client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'👋 Hello {client.user} from canny2505! Thanks for using my code, consider leaving a star on my github page.')

    # Set bot activity
    activity = discord.Game(name="Changing role colors!")
    await client.change_presence(status=discord.Status.online, activity=activity)

    # Start the role color changing task
    change_color.start()
    print("🔥 Role color changing task started.")

@tasks.loop(seconds=1)
async def change_color():
    await client.wait_until_ready()
    guild = client.get_guild(GUILD_ID)
    if guild is None:
        print("⚠️ Guild not found.")
        return

    role = guild.get_role(ROLE_ID)
    if role is None:
        print("⚠️ Role not found.")
        return

    index = change_color.current_loop % len(colors)
    color = colors[index]

    try:
        if color.startswith('#'):
            await role.edit(color=discord.Color(int(color[1:], 16)))
        else:
            await role.edit(color=getattr(discord.Color, color.lower()))
        print(f"🎨 {datetime.now().strftime('%H:%M:%S')} - Changed role {role.name} color to {color}")
    except Exception as e:
        print(f"❌ Error changing color: {e}")

# Slash command /say
@client.tree.command(name="say", description="Make the bot say any message you want")
@app_commands.describe(message="The message you want the bot to say")
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(message)

try:
    client.run(TOKEN)
except discord.LoginFailure:
    print("❌ Invalid bot token.")
# from canny2505  on discord ;)