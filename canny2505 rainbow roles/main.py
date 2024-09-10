import discord
import asyncio
from datetime import datetime
# from canny2505 with love <3
# Create an intent object and enable message content
intents = discord.Intents.default()
intents.message_content = True
# from canny2505 with love <3
# Create a single client instance
client = discord.Client(intents=intents)
# from canny2505 with love <3
# Define the role and guild IDs (replace with your actual values)
role_id = replace role id  # Replace with the actual role ID
guild_id = replace guild id  # Replace with the actual guild ID
# from canny2505 with love <3
# List of colors (including hex codes)
colors = ['#ff0000', '#ffa500', '#ffff00', '#00ff00', '#0000ff', '#ffc0cb', '#7600bc']
# from canny2505 with love <3
async def change_color():
    await client.wait_until_ready()
# from canny2505 with love <3
    # Get the guild using client.get_guild(guild_id)
    guild = client.get_guild(guild_id)
# from canny2505 with love <3
    # Get the role object
    role = guild.get_role(role_id)
# from canny2505 with love <3
    index = 0
    while not client.is_closed():
        color = colors[index % len(colors)]
# from canny2505 with love <3
        # Use discord.Color for color names or hex codes
        if color.startswith('#'):  # Check if it's a hex code
            await role.edit(color=discord.Color(value=int(color[1:], 16)))
        else:
            try:
                # Get the color object from the known color name
                await role.edit(color=getattr(discord.Color, color.lower()))
            except AttributeError:  # Handle invalid color names
                print(f"Invalid color name: {color}")
                pass  # Skip to the next color
# from canny2505 with love <3
        index += 1
        await asyncio.sleep(1) # You can change any speed that you want, i reccomend 60s to avoid rate limits
        print(f"At {datetime.now().strftime('%H:%M:%S')}, canny2505 has changed {role.name} to {color}")
# from canny2505 with love <3
@client.event
async def on_ready():
    print(f'canny2505 say hi to {client.user} and thank you for using my code <3')
    client.loop.create_task(change_color())
# from canny2505 with love <3
# Replace with your actual bot token
client.run('replace your token here')
# from canny2505 with love <3