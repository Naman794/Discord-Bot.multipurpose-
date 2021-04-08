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
from urllib import response
from urllib3.util import url



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