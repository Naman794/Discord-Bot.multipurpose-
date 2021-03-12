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



# Client (our bot) 



          

client = commands.Bot(command_prefix = '$')
client.remove_command('help')
tracker = DiscordUtils.InviteTracker(bot)




@client.command(aliases=['r'])
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
@commands.has_role('Admin')
async def clear(ctx, amount=5, timestamp= datetime.utcnow()):

    await ctx.channel.purge(limit=amount)
    message = await ctx.channel.send("message deleted")
    await message.delete()
    embed =discord.Embed(
        title = f"**{ctx.author.mention}**",
        description = 'No one will know what you did, Idiot'
    )
    embed.set_thumbnail(url='https://cdn.discordapp.com/emojis/794993563003912243.gif?v=1')
    io = await ctx.channel.send(embed=embed)
    await asyncio.sleep(5)
    await io.delete()

@client.command(name='lol')
async def lol(ctx):
    await ctx.send("<a:narutorunpeepo:796039107670179860>")


        





@client.command(name='version')
async def version(context):

    myEmbed = discord.Embed(title=f"<:>", description=" Current verison of Rooter ", color=0x00ff00)
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

    embed = discord.Embed(
        title = f"User Asked: {question}",
        description = f'8Ball says: {random.choice(response)}',
        timestamp = datetime.utcnow()
    )          

    await context.message.channel.send(embed=embed)                



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
    
    




@client.command(name='ban', pass_context=True)
@commands.has_role('Admin')
async def ban(context, member: discord.Member, *, reason=None):

    await member.ban(reason=reason)
    await context.send('User ' + member.display_name + ' has been banned')





@client.command(name='kick', pass_context=True)
@commands.has_permissions(manage_channels=True)
async def kick(context, member: discord.Member, *, reason=None):

    await member.kick(reason=reason)
    await context.send('User ' + member.display_name + ' has been kicked')


@client.command()
@commands.has_role('Admin')
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

    myEmbed = discord.Embed(title="Commands", description="Basic Commands is available for everyone and Some commands can only be accessed by the specific Roles ", color=0x00ff00, timestamp= datetime.utcnow())
    myEmbed.add_field(name='Basic Commands', value="<a:arrow:801005342589714432> Ping : To check the message speed \n <a:arrow:801005342589714432> RPS : play rock,paper,scissor \n <a:arrow:801005342589714432> Rules : RPS rules  \n <a:arrow:801005342589714432> pubg : shows random images of the game \n <a:arrow:801005342589714432> freefire : shows random images of the game freefire \n <a:arrow:801005342589714432> 8ball : The fortune teller \n <a:arrow:801005342589714432> version : to check the curent version of the BOT ", inline=False)
    myEmbed.add_field(name='High Commands', value="<a:arrow:801005342589714432> Ban : Permanently bans the user, but need to have mods permission to the user \n <a:arrow:801005342589714432> Kick : Kick the out of server and gives a temperory bans for some time \n ", inline=False)
    myEmbed.add_field(name='Music Commands:', value="<a:arrow:801005342589714432> play : To play Songs \n <a:arrow:801005342589714432> Skip : To skip a song \n <a:arrow:801005342589714432> loop : To set the song on loop \n <a:arrow:801005342589714432> Join : To call him in voice channel \n <a:arrow:801005342589714432> leave : To disconnect the Bot ")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")

    myEmbed.set_thumbnail(url="https://i.pinimg.com/originals/79/ab/9f/79ab9f804b5ebbdd514af3329cad6e0c.gif")
    myEmbed.set_footer(text="by NAMAN#0002" ,icon_url='https://www.tailorbrands.com/wp-content/uploads/2018/10/article_pic_5-4.jpg')






   
    msg = await context.message.channel.send("Waiting in your DMs ")
    await context.author.send(embed=myEmbed)
    await msg.add_reaction("<a:7022:794993555496108032>")
    await msg.add_reaction("<a:hell1:796039111337181235>")


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



@client.command(name='inviteme')
async def inviteme(ctx):

    invitelinknew = await client.create_invite(description = ctx.message.channel, xkcd = True, max_uses = 100)

    embedMsg =discord.Embed(color = 0xf41af4)
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.set_footer(text="Discord Server Invited link.")
    await ctx.send_message(ctx.message.channel, embed = embedMsg)


    
    embedMsg.set_thumbnail(url='https://cdn.dribbble.com/users/467044/screenshots/2298806/open-uri20151018-3-17cz89q')


    await client.ctx.send(ctx.message.channel, embed=embedMsg)




@client.command(name='gts')
async def gts(self, ctx):
    number = random.randint(0, 100)
    for i in range(0, 5):
        await ctx.send('guess')
        response = await self.bot.wait_for('message')
        
        guess = int(response)

        if guess > number:
            await ctx.send('bigger')
        elif guess < number:
            await ctx.send('smaller')
        else:
            await ctx.send('true')




@client.command(name='nuke')
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, channel: discord.TextChannel = None, pass_ctx = True):

    if channel == None:
        await ctx.send("You did not mention a channel")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked")
        await nuke_channel.delete()
        msg = await new_channel.send("THIS CHANNEL IS HAS BEEN NUKED!")
        ctx.msg.delete()
        await ctx.send("Nuked the channel succesfully")
        await ctx.delete(3)
        await ctx.send(url='/home/deepank/Naman/Discord/OrneryUnluckyAngwantibo-max-1mb.gif')

    else:
        await ctx.send(f"No channel named {channel.name} was found!")


music = DiscordUtils.Music()


@client.command()
async def join(ctx):
    await ctx.author.voice.channel.connect() 


@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command(aliases = ['p','Play'])
async def play(ctx, *, name):

    player = music.get_player(guild_id=ctx.guild.id)
    if not player:
        player = music.create_player(ctx, ffmpeg_error_betterfix=True)
    if not ctx.voice_client.is_playing():
        await player.queue(name, search=True)
        song = await player.play()
        sngg = await ctx.send(f"Playing {song.name}")
        await sngg.add_reaction("🎧")
    else:
        song= await player.queue(name, search=True)
        await ctx.send(f"Queued {song.name}")


@client.command()
async def pause(ctx):
    player = music.get_player(guild_i=ctx.guild.id)
    song = await player.pause()
    sng = await ctx.send(f"Paused {song.name}")
    await sng.add_reaction("✋")

@client.command()
async def stop(ctx):
    player = music.get_player(guild_id =ctx.guild.id)
    await player.stop()
    stp = await ctx.send("Stopped")
    await stp.add_reaction("🖖")

@client.command()
async def loop(ctx):
    player = music.get_player(guild_id =ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
        await ctx.send(f"Enabled loop for {song.name}")
    else:
        await ctx.send(f"Disabled loop for {song.name}")


@client.command()
async def skip(ctx):
    player = music.get_player(guild_id=ctx.guild.id)
    data = await player.skip(force=True)
    if len(data) == 2:
        await ctx.send(f"Skipped from {data[0].name} to {data[1].name}")
    else:
        await ctx.send(f"Skipped {data[0].name}")

@client.command()
async def remove(ctx, index):
    player = music.get_player(guild_id=ctx.guild.id)
    song = await player.remove_from_queue(int(index))
    await ctx.send(f"Removed {song.name} from queue")


# as discord has animated emoji feature which is only accessible if you have their perks "Nitro"
#but the on message command will make it easy for anyone on the server to send emoji in webhook format, without giving any error
#but this command will only count emoji present in the server (excllude other servers)
@client.event
async def on_message(message):
    if ":" == message.content[0] and ":" == message.content[-1]:
        emoji_name = message.content[1:-1]

        for emoji in message.guild.emojis:
            if emoji_name == emoji.name:
                await message.channel.send(emoji)
                await message.delete()

    await client.process_commands(message)


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



# This command will count the total number joining the server in real time and will updated in the provided channel 
@client.command()
async def on_member_join(self, guild):
    inviter = await self.tracker.fetch_inviter(member)
    data = await self.bot.invites.find(inviter.id)
    if data in None:
        data = {"_id": inviter.id, "count": 0, "userInvited": []}

    data["count"] +=1
    data["userInvited"].append(member.id)
    await self.bot.invites.upsert(data)

    channel = discord.utils.get(member.guild.text_channels, name="gateway")
    embed = discord.Embed(
        title=f"Welcome {member.mention} to Rooter",
        description=f"Invited by : {inviter.mention}\nInvites : {data['count']}",
        timestamp=member.joined_at
    )
    await channel.send(embed=embed)
# this command is for message which will execute only if the user react on the emoji ;)
@client.command(aliases=['shop', 'store'])
async def paginate(ctx):
            # describing types of embeds do that the bot don't get exception while executing it
    embed1 = discord.Embed(color=ctx.author.color).add_field(name="Store 1", value="Will be updated soon!")
    embed2 = discord.Embed(color=ctx.author.color).add_field(name="Store 2", value=f"<a:cutie:800805913451692122>")
    embed3 = discord.Embed(color=ctx.author.color).add_field(name="Store 3", value=f"<a:indian:803542518754574336>")
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx, remove_reactions=True)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('🔐', "lock")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    embeds = [embed1, embed2, embed3]
    await paginator.run(embeds)
    await embed1.add_reaction("⏮️", "⏪", "🔐", "⏩", "⏭️")
    await embed2.add_reaction("⏮️", "⏪", "🔐", "⏩", "⏭️")
    await embed3.add_reaction("⏮️", "⏪", "🔐", "⏩", "⏭️")

 







# Run the client on the server
client.run('your bot token here')
 
