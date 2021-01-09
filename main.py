import discord
from itertools import cycle
from discord.ext import tasks, commands
from datetime import date
from flask import Flask
from threading import Thread


app = Flask('')
today = date.today()

# Quote Library
quote_library = {}


@app.route('/')
def main():
    return "Your Bot Is Ready"


def run():
    app.run(host="0.0.0.0", port=8000)


def keep_alive():
    server = Thread(target=run)
    server.start()


client = commands.Bot(command_prefix='.')
status = cycle(['Status 1', 'Status 2', 'Status 3'])


@client.event
async def on_ready():
    change_status.start()
    print("Quote Bot is Ready!")


@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# List of Quotable People
def getlist(dictionary):
    return list(dictionary.keys())


# Ping Command to check bot latency
@client.command(aliases=["PING", "Ping", "p", "P"])
async def ping(ctx):
    await ctx.send(f"Ping: {round(client.latency * 1000)}ms")


# Help Command to get list of Commands
@client.command(aliases=["Guide", "GUIDE", "G", "g"])
async def guide(ctx):
    await ctx.send(f"Here are all the available commands:\n"
                   f".ping - Checks the latency of the Quote Bot\n"
                   f".guide - Provides a list of all commands\n"
                   f".add name - Adds a new quotable person\n"
                   f".delete name - Deletes a quotable person\n"
                   f".q message ~ name - Adds a quote to the person's list of quotes\n"
                   f".d name - Displays all of the person's quotes\n"
                   f".r index ~ name - Removes a specific quote from a person's list\n"
                   f".a name - Displays the total number of quotes a person has\n"
                   f".c name - Clears all quotes from the person's list")


# Add Command to Add a New Quotable Person
@client.command(aliases=["Add", "ADD"])
async def add(ctx, *, name):
    if quote_library.get(name) is None:
        temp = {name: list()}
        quote_library.update(temp)
        await ctx.send(f"{name} has been added as a quotable person!")
    else:
        await ctx.send("The person you are trying to add already exists")


# Del Command to Delete a Quotable Person
@client.command(aliases=["Delete", "DELETE"])
async def delete(ctx, *, name):
    if quote_library.get(name) is None:
        await ctx.send("The person you are trying to remove doesn't exist")
    else:
        del quote_library[name]
        await ctx.send(f"{name} has been removed from the list of quotable people")


# Quote Command to add a Quote to a Quotable Person
@client.command(aliases=["Quote", "QUOTE", "q", "Q"])
async def quote(ctx, *, message):
    messagelist = [x.strip() for x in message.split('~')]
    if quote_library.get(messagelist[-1]) is None:
        await ctx.send("The person you are trying to quote is not yet a quotable person")
    else:
        quote_library.get(messagelist[-1]).append(f"{today} - {messagelist[0]}")
        await ctx.send("Quoted!")


# Display Command to displau all quotes of a particular person
@client.command(aliases=["Display", "DISPLAY", "d", "D"])
async def display(ctx, *, name):
    if quote_library.get(name) is None:
        await ctx.send("The person you have searched for is not a quotable person\n"
                       "Please check the spelling of the name and ensure it matches with one of the following:\n"
                       + (str(getlist(quote_library))) +
                       f"\nOtherwise, please add this person to the list of quotable people using .add")
    elif len(quote_library.get(name)) == 0:
        await ctx.send(f"{name} does not have any quotes yet! You can change that by using "
                       f".quote")
    else:
        for elem in quote_library.get(name):
            await ctx.send(f"{(1 + (quote_library.get(name).index(elem)))}. {elem}")


# Amount Command that displays the number of times a person has been quoted
@client.command(aliases=["Amount", "AMOUNT", "a", "A"])
async def amount(ctx, *, name):
    if quote_library.get(name) is None:
        await ctx.send("The person you have searched for is not a quotable person\n"
                       "Please check the spelling of the name and ensure it matches with one of the following:\n"
                       + (str(getlist(quote_library))) +
                       f"\nOtherwise, please add this person to the list of quotable people using .add")
    else:
        await ctx.send(f"{name} has been quoted {len(quote_library.get(name))} times")


# Remove Command that removes a specific quote using the number assigned to the quote
@client.command(aliases=["Remove", "REMOVE", "r", "R"])
async def remove(ctx, *, info):
    infolist = [x.strip() for x in info.split('~')]
    if quote_library.get(infolist[-1]) is None:
        await ctx.send("The person you have searched for is not a quotable person\n"
                       "Please check the spelling of the name and ensure it matches with one of the following:\n"
                       + (str(getlist(quote_library))) +
                       f"\nOtherwise, please add this person to the list of quotable people using .add")
    else:
        del quote_library.get(infolist[-1])[(int(infolist[0])-1)]
        await ctx.send("The quote has been removed")


# Clear Command that removes all quotes from a person's list
@client.command(aliases=["Clear", "CLEAR", "c", "C"])
async def clear(ctx, *, name):
    quote_library.get(name).clear()
    await ctx.send(f"{name}'s quotes have been cleared")


client.run('token')
