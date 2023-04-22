Sure, here is an example of a Discord bot in Python with Pycord that has a basic economy system with an SQLite database:
```python
import os
import sqlite3

from discord.ext import commands

# Create the database connection
conn = sqlite3.connect("economy.db")

# Create the tables
c = conn.cursor()
c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, balance INTEGER)")
c.execute("CREATE TABLE transactions (id INTEGER PRIMARY KEY, user_id INTEGER, amount INTEGER, type TEXT, timestamp TEXT)")

# Create the bot
bot = commands.Bot(command_prefix="!")

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
```
    
This bot has the following commands:

* `deposit`: Deposits money into the user's account.
* `withdraw`: Withdraws money from the user's account.
* `balance`: Shows the user's balance.

The bot uses an SQLite database to store the users' balances and transactions. The database is created when the bot is first run. The bot also logs all transactions to the database.

This is just a simple example of a Discord bot with an economy system. You can add more features to the bot, such as buying and selling items, or having user-to-user transactions.