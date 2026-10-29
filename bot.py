import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
load_dotenv("token.env")

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set.")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix = "!",
    intents = intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm online.")


story_location = [
    "an abandoned library",
    "a mysterious island",
    "a futuristic city",
    "a hidden underground laboratory",
    "a forest that never appears on any map",
    "an empty, endless desert",
    "a haunted Victorian mansion"
]

story_items = [
    "a glowing key",
    "an ancient notebook",
    "a strange campass",
    "a locked metal box",
    "a mysterious photograph",
    "a broken locket",
    "a single silver earring",
    "a worn leather diary"
]

story_events = [
    "You hear footsteps behind you.",
    "The lights suddenly turn off.",
    "A hidden door opens nearby.",
    "Your phone starts displaying a message from an unknown sender.",
    "You notice that the room has changed.",
    "A cold breeze blows from an unknown source.",
    "You find a hidden passage.",
    "The object you are holding vibrates softly."
]
user_stories = {}

@bot.command()
async def story(ctx):

    user_id = ctx.author.id

    location  = random.choice(story_location)
    item = random.choice(story_items)
    event = random.choice(story_events)

    user_stories[user_id] = {
        "location":location,
        "items": item,
        "event":event
    }

    story_text = (
        f"You wake up in {location}.\n\n"
        f"Next to you is {item}.\n\n"
        f"{event}.\n\n"
        "What do you do?"
    )

    await ctx.send(story_text)


@bot.command()
async def choose(ctx, choice: str):
    user_id = ctx.author.id

    if user_id not in user_stories:
        await ctx.send("You dont have an active story. Try '!story' first.")
        return

    choice = choice.lower()

    if choice == "left":
        response = (
            "You head left and discover a room filled with old maps."
            "One of them your name written on it"
        )
    elif choice == "right":
        response = (
            "You head right and a staircase leading toward"
            "a strange blue light."
        )

    else:
        response = "Try choosing 'Left' or 'Right'."

    await ctx.send(response)

chat_responses = {
    "hello": [
        "Hey! What's up?",
        "Hello! How is your day going?",
        "Hi! What are you working on?"
    ],

    "python": [
        "Python is a great language for beginners because its syntax is pretty readable.",
        "If you're learning Python, try building something instead of only watching tutorials."
    ],

    "discord": [
        "Discord bots are a fun way to practice Python because you get instant feedback.",
        "Once you understand commands and events, you can build some surprisingly complex bots."
    ]
}

@bot.command()
async def chat(ctx, *, message: str):
    text = message.lower()

    for keyword, responses in chat_responses.items():
        if keyword in text:
            await ctx.send(random.choice(responses))
            return

    await ctx.send(
        "I'm still learning how to respond to that. "
        "Try talking to me about python or discord."
    )

support_responses = {
    "stress":[
        "That sounds like alot to handle. Try to breaking the situation into one small task at a time.",
        "When everything feels overwhelming, it can help to pause and focus on what needs attention right now." 
    ],
    "school": [
        "School can pile up quickly. Consider choosing an assignment to work on first instead of trying to finish everything at once.",
        "If school stress is getting deficult to manage, talking with a trusted person can make things less like something you have to handle alone."
    ],
    "sad":[
        "Am sorry you are having a dificult moment. "
    ]
    
}

bot.run(TOKEN)