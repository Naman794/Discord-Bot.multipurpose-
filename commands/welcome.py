
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
import 


intents = discord.Intents.all()


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