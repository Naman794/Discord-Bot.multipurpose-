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


@client.listen()
''' as discord has animated emoji feature which is only accessible if you have their perks "Nitro"
    but the on message command will make it easy for anyone on the server to send emoji in webhook format, without giving any error
    but this command will only count emoji present in the server (exclude other servers) '''
async def on_message(message):
    if ":" == message.content[0] and ":" == message.content[-1]:
        emoji_name = message.content[1:-1]

        for emoji in message.guild.emojis:
            if emoji_name == emoji.name:
                pfp = requests.get(message.author.avatar_url_as(format='png', size=256)).content #defining the body of the webhook
                hook = await message.channel.create_webhook(name=message.author.display_name, avatar=pfp)
                await hook.send(emoji)
                await hook.delete()  #this will delete the webhook for integrations as per the discord limit of 10 webhooks per channel
                await message.delete() 

    
