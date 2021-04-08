# Import Discord Package
import discord
from discord.ext import commands, tasks
import random, math, asyncio, json, string, urllib, secrets, aiohttp, os, re, time, DiscordUtils
from itertools import cycle
from discord import client, errors, guild, member, message, permissions, user
from dateutil.relativedelta import relativedelta
from datetime import timezone, datetime
from discord.ext.commands import bot
import DiscordUtils
from urllib import response
from urllib3.util import url
from discord.ext.buttons import Paginator
from commands import rps


# Client (our bot) 



          

client = commands.Bot(command_prefix = '$')
client.remove_command('help')
tracker = DiscordUtils.InviteTracker(bot)









@client.command(name='rules')
async def rules(ctx):
    await ctx.send("To play Rock Paper Scissors type in the following commands: \n Rock = -rock \n Paper = -paper \n Scissors = -scissors \n you can't beat ME")


@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title=f"<:>", description=" Current verison of Rooter ", color=0x00ff00)
    myEmbed.add_field(name='Version Code:', value="v5.9.7.2", inline=False)
    myEmbed.add_field(name='Date Updated:', value="Nov 5th, 2020", inline=False)
    myEmbed.set_footer(text=" ")
    myEmbed.set_author(name="Rooter Sports Technologies Private Limited")

    await context.message.channel.send(embed=myEmbed)
    
               



@client.command(name='ping')
async def ping(context):
    msg = await context.send("`Pinging bot latency...`")
    times = []
    counter = 0
    embed = discord.Embed(title="More information:", description="Pinged 4 times and calculated the average.", colour=discord.Colour(value=0x36393e))
    for _ in range(3):
            counter += 1
            start = time.perf_counter()
            aa = await msg.edit(content=f"Pinging... {counter}/3")
            end = time.perf_counter()
            speed = round((end - start) * 1000)
            times.append(speed)
            embed.add_field(name=f"Ping {counter}:", value=f"{speed}ms", inline=True)

    myEmbed = discord.Embed(
        title="?Ping?", 
        color = 0xfffff,
        description=f'Pong!! \n That will send us  in Nebula lets go <a:run:796039107670179860> \n The message took {round(client.latency *  1000)}ms to respond')
    
    myEmbed.set_footer(text=f" by {context.author.name} ", icon_url='https://cdn.discordapp.com/emojis/804354768495050762.png?v=1')


    pp = await context.message.channel.send(embed=myEmbed)
    await asyncio.sleep(5)
    await pp.delete()
    
    





   
    



@client.event
async def on_ready():
    # DO STUFF....
    general_channel = client.get_channel(793061802023714819)

    print ("bot is ready")



@client.command(aliases=[' '])
async def ctx(context):

        myEmbed = discord.Embed(title=" ", description=" ", color=0x00ff00, timestamp = datetime.utcnow())
        myEmbed.add_field(name=':', value="", inline=False)
        myEmbed.add_field(name='', value="", inline=False)
        myEmbed.set_footer(text=f" Requested by {context.author.name} ")
        myEmbed.set_author(name="")
         # embed.set_thumbnail(url=f"{ctx.guild.icon}")
        
        myEmbed.set_thumbnail(url="")
        
        
        
        await context.message.channel.send(embed=myEmbed)
    
   






@client.event
async def on_connect():

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=''))
    
    # Settings 'Listening' status

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" "))
    


    


@client.command(name="freefire")
async def freefire(context, timestamp= datetime.utcnow()):

    images = ["/home/deepank/Naman/Discord/garena-free-fire-pc.jpg", "/home/deepank/Naman/Discord/source.gif"]

    free_fire = random.choice(images)





@client.command(name="pubg")
async def pubg(context, timestamp= datetime.utcnow()):

    images = ["/home/deepank/Naman/Discord/av8jeOO_460s.jpg", "/home/deepank/Naman/Discord/download (1).jpeg", "/home/deepank/Naman/Discord/download (2).jpeg", "/home/deepank/Naman/Discord/Serious-Sam-4-Planet-Badass-4K-Ultra-HD-Mobile-Wallpaper-scaled.jpg", "/home/deepank/Naman/Discord/725bc30a562e98d4ea56c39e2a422993.jpg"]

    pubg = random.choice(images)

    await context.send(file=discord.File(pubg))


@client.command(name="")
async def (context, timestamp= datetime.utcnow()):

    images = [""]

    profile = random.choice(images)

    await context.send(file=discord.File(profile))


@client.command(name='invites')
async def invites(context, member: discord.member = None):
    totalInvites = 0
    for i in await context.guild.invites():
        if i.inviter == context.author:
            totalInvites += i.uses
        embed = discord.Embed(
            title = f"You have invited {totalInvites} member{'' if totalInvites == 1 else 's'} to the server! ",
            timestamp = datetime.utcnow(),
            color = 0xFFFF00
        )
    await context.send(embed=embed)





@client.command(name='inviteme')
async def inviteme(ctx):

    invitelinknew = await client.create_invite(description = ctx.message.channel, xkcd = True, max_uses = 100)

    embedMsg =discord.Embed(color = 0xf41af4)
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.set_footer(text="Discord Server Invited link.")
    await ctx.send_message(ctx.message.channel, embed = embedMsg)


    
    embedMsg.set_thumbnail(url='https://cdn.dribbble.com/users/467044/screenshots/2298806/open-uri20151018-3-17cz89q')


    await client.ctx.send(ctx.message.channel, embed=embedMsg)











# this comman will show the data of the server, like when it was created and how many members, user are present or joined as well as roles and perms too!              
@client.command(aliases=['info', 'serverinfo'])
async def server(ctx):
        guild = ctx.message.guild
        online = len([m.status for m in guild.members
                      if m.status == discord.Status.online or
                      m.status == discord.Status.idle])
        total_users = len(guild.members)
        total_bots = len([member for member in guild.members if member.bot == True])
        total_humans = len([member for member in guild.members if member.bot == False])
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        passed = (ctx.message.created_at - guild.created_at).days
        created_at = ("Since {}. Over {} days ago."
                      "".format(guild.created_at.strftime("%d %b %Y %H:%M"),
                                passed))

        embed = discord.Embed(description=created_at, colour=discord.Colour(value=0xFFD700))
        embed.add_field(name="Region", value=str(guild.region))
        embed.add_field(name="Users", value="{}/{}".format(online, total_users))
        embed.add_field(name="Humans", value=total_humans)
        embed.add_field(name="Bots", value=total_bots)
        embed.add_field(name="Text Channels", value=text_channels)
        embed.add_field(name="Voice Channels", value=voice_channels)
        embed.add_field(name="Roles", value=len(guild.roles))
        embed.add_field(name="Owner", value=str(guild.owner))
        embed.set_footer(text=f"Guild ID:{str(guild.id)}")
        embed.set_footer(text=f"by {ctx.author}", icon_url='https://www.tailorbrands.com/wp-content/uploads/2018/10/article_pic_5-4.jpg')

        if guild.icon_url:
            embed.set_author(name=guild.name, url=guild.icon_url)
            embed.set_thumbnail(url=guild.icon_url)
        else:
            embed.set_author(name=guild.name)

        await ctx.send(embed=embed)










# Run the client on the server
client.run('your bot token here')
 
