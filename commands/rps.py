MIT License

Copyright (c) 2017 HB Zatan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


import discord
import random 



@commmands.command(aliases=['r'])
async def rock(ctx):
    number = random.randint(1,3)
    if number == 1:
        embed = discord.Embed(
            title = "Result",
            description = 'Its a tie, shit!', color = 0xFFFFFF
        )
        await ctx.send(embed=embed)
    elif number == 2:
        eembed = discord.Embed(
            title = "Results",
            description = 'You lost now go drink milk idioto!', color = 0xFFFFFF
        )
        await ctx.send(embed=eembed)
    elif number == 3:
        eymbed = discord.Embed(
            title = "Result",
            description = 'You win but i am not gonna lose to you again!', color = 0xFFFFFF
        )
        await ctx.send(embed=eymbed)



@commands.command(name='paper')
async def paper(ctx):
    number = random.randint(1,3)
    if number == 1:
        await ctx.send('YOU WIN!')
    elif number == 2:
        await ctx.send("IT'S A TIE!")
    elif number == 3:
        await ctx.send('YOU LOST!')



@commands.command(name='scissors')
async def scissors(ctx):
    number = random.randint(1,3)
    if number == 1:
        await ctx.send('YOU LOST!')
    elif number == 2:
        await ctx.send("YOU WIN!")
    elif number == 3:
        await ctx.send("IT'S A TIE!")