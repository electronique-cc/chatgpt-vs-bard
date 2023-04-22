Sure, here's an example of a Discord bot written in Python using the Pycord library with a basic economy system that uses an SQLite database:

```python
`import discord
from discord.ext import commands
import sqlite3

bot = commands.Bot(command_prefix='!')

# connect to the SQLite database
conn = sqlite3.connect('economy.db')
cursor = conn.cursor()

# create the table to store user balances if it doesn't exist already
cursor.execute('''CREATE TABLE IF NOT EXISTS balances
                  (user_id INTEGER PRIMARY KEY, balance INTEGER)''')
conn.commit()

@bot.event
async def on_ready():
    print('Bot is online and connected to Discord!')

@bot.command()
async def balance(ctx):
    # get the user's balance from the database
    cursor.execute('SELECT balance FROM balances WHERE user_id=?', (ctx.author.id,))
    result = cursor.fetchone()
    if result is None:
        # if the user doesn't have a balance yet, create a new record for them
        cursor.execute('INSERT INTO balances (user_id, balance) VALUES (?, ?)', (ctx.author.id, 0))
        conn.commit()
        await ctx.send(f'{ctx.author.mention}, you have 0 coins.')
    else:
        await ctx.send(f'{ctx.author.mention}, you have {result[0]} coins.')

@bot.command()
async def earn(ctx, amount: int):
    # add the specified amount to the user's balance in the database
    cursor.execute('SELECT balance FROM balances WHERE user_id=?', (ctx.author.id,))
    result = cursor.fetchone()
    if result is None:
        cursor.execute('INSERT INTO balances (user_id, balance) VALUES (?, ?)', (ctx.author.id, amount))
    else:
        new_balance = result[0] + amount
        cursor.execute('UPDATE balances SET balance=? WHERE user_id=?', (new_balance, ctx.author.id))
    conn.commit()
    await ctx.send(f'{ctx.author.mention}, you earned {amount} coins!')

@bot.command()
async def spend(ctx, amount: int):
    # subtract the specified amount from the user's balance in the database
    cursor.execute('SELECT balance FROM balances WHERE user_id=?', (ctx.author.id,))
    result = cursor.fetchone()
    if result is None or result[0] < amount:
        await ctx.send(f'{ctx.author.mention}, you don\'t have enough coins to spend {amount}!')
    else:
        new_balance = result[0] - amount
        cursor.execute('UPDATE balances SET balance=? WHERE user_id=?', (new_balance, ctx.author.id))
        conn.commit()
        await ctx.send(f'{ctx.author.mention}, you spent {amount} coins!')
        
# replace 'TOKEN' with your own Discord bot token
bot.run('TOKEN')` 
```
This bot uses the `balance`, `earn`, and `spend` commands to interact with the user's balance in the database. When a user types `!balance`, the bot fetches the user's balance from the database and sends it back in a message. When a user types `!earn <amount>`, the bot adds the specified amount to the user's balance in the database and sends a confirmation message. When a user types `!spend <amount>`, the bot subtracts the specified amount from the user's balance in the database and sends a confirmation message, or an error message if the user doesn't have enough coins.