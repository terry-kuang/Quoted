# Quoted
Quoted is a Discord bot that allows users to quote their favorite messages and view them is a repository
Quotes are organized in an internal dictionary system where the names are keys and the quotes are stored 
as lists in the value pair.

Currently, the list of available commands include:
.ping - Checks the latency of the Quote Bot
.guide - Provides a list of all commands
.add name - Adds a new quotable person
.delete name - Deletes a quotable person
.q message ~ name - Adds a quote to the person's list of quotes   (alias for .quote)
.d name - Displays all of the person's quotes                     (alias for .display)
.r index ~ name - Removes a specific quote from a person's list   (alias for .remove)
.a name - Displays the total number of quotes a person has        (alias for .amount)
.c name - Clears all quotes from the person's list                (alias for .clear)


Will be working on making the repository an external file as to save the quotes. Currently, if the bot goes
offline, the dictionary is wiped clean and all progress is reset. 
Will be working on making the code more readable
Will be adding new elements such as the ability to customize the prefix, ranking system?, etc

