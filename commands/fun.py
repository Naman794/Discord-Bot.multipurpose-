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
import asyncio
import datetime



@client.command(aliases=['flip', 'toss'])
async def coinflip(ctx, timestamp= datetime.utcnow()):

    
    image = ["/home/deepank/Naman/Discord/EcSe (1).gif"]
    toss = random.choice(image)
    wow = await ctx.channel.send(file=discord.File(toss))
    await asyncio.sleep(4)
    await wow.delete()

    coinsides = ['Heads', 
                  'Tails']
    await ctx.channel.send(f"**{ctx.author.mention}** flipped a coin and got **{random.choice(coinsides)}**!")
    



@client.command(name='password')
async def password(context, nbytes: int =18):
    
    if nbytes not in range(3, 1401):
        return await context.send("I only accept number between 3-1400")
    
    if hasattr(context, 'guild') and context.guild is not None:
        await context.send(f"sending you a private message with your random generated password **{context.author.name}** ")
    await context.author.send(f"🎁 **here is your password:**\n{secrets.token_urlsafe(nbytes)}")


@client.command(name='noticeme')
async def noticeme(ctx):
    
   
    imag = ["/hom/home/deepank/Naman/Discord/OrneryUnluckyAngwantibo-max-1mb.gife/deepank/Videos/500ce4.gif"]

    full = random.choice(imag)


    await ctx.send(f"yo **{ctx.author.mention}**")
    await ctx.send(file=discord.File(full))


@client.command(aliases=['slot', 'bet'])
async def roll(ctx):
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a= random.choice(emojis)
    b= random.choice(emojis)
    c= random.choice(emojis)

    slotmachine = f"** {a} {b} {c}  \n{ctx.author.mention}**,"

    if (a == b == c):
        await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        await asyncio(6)

    elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
            await asyncio(6)
    else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")
            await asyncio(6)


@client.command(aliases=['8ball','test'])
async def _8ball(context,*, question):
    response = ['It is certain.',
                    'its decidedly so',
                    'without a doubt',
                    'yes - definitly',
                    'you may rely on it',
                    'as i see it, yes',
                    'most likely',
                    'outlook good',
                    'yes',
                    'signs point to yes',
                    'reply hazy, try again.',
                    'ask again later',
                    'better not tell you now',
                    'cannot predict now',
                    "don't count on it",
                    'my reply is no',
                    'my sources say no',
                    'outlook not so good',
                    'very doubtful',]

    embed = discord.Embed(
        title = f"User Asked: {question}",
        description = f'8Ball says: {random.choice(response)}',
        timestamp = datetime.utcnow()
    )          

    await context.message.channel.send(embed=embed) 