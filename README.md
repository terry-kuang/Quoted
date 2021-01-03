# Quoted

## Description
Quoted is a Discord bot that allows users to quote their favorite messages and view them is a repository
Quotes are organized in an internal dictionary system where the names are keys and the quotes are stored 
as lists in the value pair.

## Dependencies
* Python >= 3.6.0
* discord.py >= 1.5.1
* Mac/Window OS

## Commands
Currently, the list of available commands include:
* .ping - Checks the latency of the Quote Bot
* .guide - Provides a list of all commands
* .add name - Adds a new quotable person
* .delete name - Deletes a quotable person
* .q message ~ name - Adds a quote to the person's list of quotes   (alias for .quote)
* .d name - Displays all of the person's quotes                     (alias for .display)
* .r index ~ name - Removes a specific quote from a person's list   (alias for .remove)
* .a name - Displays the total number of quotes a person has        (alias for .amount)
* .c name - Clears all quotes from the person's list                (alias for .clear)

## Future Changes
Will be working on making the repository an external file as to save the quotes. Currently, if the bot goes
offline, the dictionary is wiped clean and all progress is reset. 
Will be working on making the code more readable
Will be adding new elements such as the ability to customize the prefix, ranking system?, etc

## Author
Terry Kuang
January 3rd 2021

Project created for a discord server to streamline the quoting process instead of using a spreadsheet manually

## License
The MIT License

Copyright (c) 2020 Terry Kuang

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
