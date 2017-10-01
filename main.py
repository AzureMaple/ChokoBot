# Import Libaries
import asyncio, discord, json
# Init Variables
version_data = "Alpha Build"
client = discord.Client()

# async def are parts of the program that are checked constantly. (Probably per tick.)

with open('common/login.json', 'r') as json_data_file:
    login_info = json.load(json_data_file)
    
@client.event #Add this before anything that should use discord.Client
async def on_ready(): # Alert that Choko is alive!
    if client.is_logged_in: # If Logged in...
        print("Surprise! ChokoBot is alive motherf*ckers! Fite me.")
        print("username: " + client.user.name)
        print("ID: " + client.user.id)
    else:
        print("Choko is ded. Press 'f' to pay your respects.")
        
client.run(login_info["token"]) # Run Client as Bot