
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
import paginator
from discord.ext.commands import buttons




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
