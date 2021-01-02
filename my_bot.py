# Import Discord Package
import discord
from discord.ext import commands, tasks
import random
from itertools import cycle
import math
import asyncio









# Client (our bot) 
client = commands.Bot(command_prefix='-')
client.remove_command('help')



            







@client.command(name='rock' or 'r')
async def rock(ctx):
    number = random.randint(1,3)
    if number == 1:
        await ctx.send("IT'S A TIE!")
    elif number == 2:
        await ctx.send('YOU LOST!')
    elif number == 3:
        await ctx.send('YOU WIN!')



@client.command(name='paper')
async def paper(ctx):
    number = random.randint(1,3)
    if number == 1:
        await ctx.send('YOU WIN!')
    elif number == 2:
        await ctx.send("IT'S A TIE!")
    elif number == 3:
        await ctx.send('YOU LOST!')



@client.command(name='scissors')
async def scissors(ctx):
    number = random.randint(1,3)
    if number == 1:
        await ctx.send('YOU LOST!')
    elif number == 2:
        await ctx.send("YOU WIN!")
    elif number == 3:
        await ctx.send("IT'S A TIE!")




@client.command(name='rules')
async def rules(ctx):
    await ctx.send("To play Rock Paper Scissors type in the following commands: \n Rock = -rock \n Paper = -paper \n Scissors = -scissors \n you can't beat ZATAN")


@client.command()
async def clear(ctx, amount=5):

    await ctx.channel.purge(limit=amount)









@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title="About Rooter Version", description=" Current verison of Rooter ", color=0x00ff00)
    myEmbed.add_field(name='Version Code:', value="v5.9.7.2", inline=False)
    myEmbed.add_field(name='Date Updated:', value="Nov 5th, 2020", inline=False)
    myEmbed.set_footer(text=" ")
    myEmbed.set_author(name="Rooter Sports Technologies Private Limited")

    await context.message.channel.send(embed=myEmbed)
    
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

    await context.message.channel.send(f'question: {question} \nAnswer: {random.choice(response)}')                



@client.command(name='ping')
async def ping(context):
   
    await context.send(f"Pong! {round(client.latency * 1000)}ms")



@client.event
async def on_ready():
    # DO STUFF....
    general_channel = client.get_channel(793061802023714819)

    await general_channel.send(' ! ')



@client.command(name='Rooter')
async def Rooter(context):

        myEmbed = discord.Embed(title="About Rooter", description="Rooter is Gaming and Sports App.Join Daily Contest & GIveaway and Win up to ₹5 Lakhs now. ", color=0x00ff00)
        myEmbed.add_field(name='Founders & CEO :', value="Piyush & Dipesh Agarwal", inline=False)
        myEmbed.add_field(name='Established', value="Since Year 2015", inline=False)
        myEmbed.set_footer(text="        ")
        myEmbed.set_author(name="ROOTER")
         # embed.set_thumbnail(url=f"{ctx.guild.icon}")
        
        myEmbed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0ZkT2dGynxvQikVTQ4lBZMLxNTmyCqPvZEA&usqp=CAU")
        
        
        
        await context.message.channel.send(embed=myEmbed)
    
   






@client.event
async def on_connect():

    await client.change_presence(status=discord.Status.online, activity=discord.Game('type -help'))



@client.command(name='ban', pass_context=True)
async def ban(context, member: discord.Member, *, reason=None):

    await member.ban(reason=reason)
    await context.send('User ' + member.display_name + ' has been banned')





@client.command(name='kick', pass_context=True)
async def kick(context, member: discord.Member, *, reason=None):

    await member.kick(reason=reason)
    await context.send('User ' + member.display_name + ' has been kicked')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):

            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return







@client.command(name='help')
async def help(context):

    myEmbed = discord.Embed(title="Commands", description="Basic Commands is available for everyone and Some commands can only be accessed by the specific Roles ", color=0x00ff00)
    myEmbed.add_field(name='Basic Commands :', value="Ping \n RPS \n Rules \n pubg \n freefire \n 8ball \n version ", inline=False)
    myEmbed.add_field(name='High Commands', value="Ban \n Kick \n ", inline=False)
    myEmbed.set_footer(text="        ")
    myEmbed.set_author(name="ＨELP")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    myEmbed.set_thumbnail(url="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5ecd5fab-be8d-4409-bd84-4a3d205b9ec8/daehq7e-48b7f14a-14ff-4082-9e7c-aee710c9bbfd.gif?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNWVjZDVmYWItYmU4ZC00NDA5LWJkODQtNGEzZDIwNWI5ZWM4XC9kYWVocTdlLTQ4YjdmMTRhLTE0ZmYtNDA4Mi05ZTdjLWFlZTcxMGM5YmJmZC5naWYifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.4Y6BPM1ZrKtT-0FAscnrscGSJyKt5XxagdsRU5A6XL0")







   
    await context.message.channel.send(embed=myEmbed)



@client.command(name="freefire")
async def freefire(context):

    images = ["/home/deepank/Naman/Discord/garena-free-fire-pc.jpg", "/home/deepank/Naman/Discord/source.gif"]

    free_fire = random.choice(images)

    await context.send(file=discord.File(free_fire))



@client.command(name="pubg")
async def pubg(context):

    images = ["/home/deepank/Naman/Discord/av8jeOO_460s.jpg", "/home/deepank/Naman/Discord/download (1).jpeg", "/home/deepank/Naman/Discord/download (2).jpeg", "/home/deepank/Naman/Discord/Serious-Sam-4-Planet-Badass-4K-Ultra-HD-Mobile-Wallpaper-scaled.jpg", "/home/deepank/Naman/Discord/725bc30a562e98d4ea56c39e2a422993.jpg"]

    pubg = random.choice(images)

    await context.send(file=discord.File(pubg))


@client.command(name="zatanprofile")
async def zatanprofile(context):

    images = ["/home/deepank/Naman/Discord/WhatsApp Image 2020-11-29 at 8.40.31 PM.jpeg"]

    zatanprofile = random.choice(images)

    await context.send(file=discord.File(zatanprofile))






# Run the client on the server
client.run('Bot Token')
 
