import os
import sqlite3
import logging
import discord

from datetime import datetime
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Create the database connection
conn = sqlite3.connect("economy.db")

# Create the tables
c = conn.cursor() #create table if not exists users (id integer primary key, balance integer)
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, balance INTEGER)")
c.execute("CREATE TABLE IF NOT EXISTS transactions (id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER, type TEXT, timestamp TEXT)")

# Create the bot
bot = discord.Bot()

# Add a command to deposit money
@bot.command()
async def deposit(ctx, amount: int):
    # Get the user's ID
    user_id = ctx.author.id

    # Get the user's current balance
    c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    balance = c.fetchone()[0]

    # Update the user's balance
    c.execute("UPDATE users SET balance = ? WHERE id = ?", (balance + amount, user_id))
    conn.commit()

    # Log the transaction
    c.execute("INSERT INTO transactions (user_id, amount, type, timestamp) VALUES (?, ?, ?, ?)", (user_id, amount, "deposit", str(datetime.now())))
    conn.commit()

    # Send a message to the user
    await ctx.send(f"You have deposited {amount} coins. Your balance is now {balance} coins.")

# Add a command to withdraw money
@bot.command()
async def withdraw(ctx, amount: int):
    # Get the user's ID
    user_id = ctx.author.id

    # Get the user's current balance
    c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    balance = c.fetchone()[0]

    # Check if the user has enough money
    if balance < amount:
        await ctx.send("You do not have enough coins.")
        return

    # Update the user's balance
    c.execute("UPDATE users SET balance = ? WHERE id = ?", (balance - amount, user_id))
    conn.commit()

    # Log the transaction
    c.execute("INSERT INTO transactions (user_id, amount, type, timestamp) VALUES (?, ?, ?, ?)", (user_id, amount, "withdraw", str(datetime.now())))
    conn.commit()

    # Send a message to the user
    await ctx.send(f"You have withdrawn {amount} coins. Your balance is now {balance} coins.")

# Add a command to see the user's balance
@bot.command()
async def balance(ctx):
    # Get the user's ID
    user_id = ctx.author.id

    # Get the user's balance
    c.execute("SELECT balance FROM users WHERE id = ?", (user_id,))
    balance = c.fetchone()[0]

    # Send a message to the user
    await ctx.send(f"Your balance is {balance} coins.")

# Run the bot
bot.run(os.getenv("TOKEN"))