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