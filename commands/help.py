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


@client.command(name='help')
async def help(context):
    ''' Customize as you want it to be , this code is just an example ! '''

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

    