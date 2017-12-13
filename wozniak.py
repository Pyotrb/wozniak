import discord as d
from discord.ext import commands as c

import time as t

##########################################################################
Client = d.Client()
server = d.Server
prefix = '='
client = c.Bot(command_prefix = prefix)
voice = d.VoiceClient

##########################################################################
@client.event

async def on_ready():
    print('Jamboree time')
    print('http://discordpy.readthedocs.io/en/latest/api.html')
    print(d.__version__)

##########################################################################
@client.event
async def on_message(message):
    msg = message.content.lower()
    user = message.author.name + '#' + message.author.discriminator

    # BLING EARNING

    if message.server.id == '389483103250284555':
        try:
            f = open('users/' + user + '.musx', 'r')
            f.close()
            newfile = 0
        except:
            f = open('users/' + user + '.musx', 'w')
            f.close()
            newfile = 1

        if newfile:
            f = open('users/' + user + '.musx', 'w')
            f.write('1\n')
            f.write(str(int(t.time())) + '\n')
            f.close()
        else:
            f = open('users/' + user + '.musx', 'r')
            lines = f.readlines()
            if int(t.time()) - int(lines[1]) > 30:
                lines[0] = str(int(lines[0].replace('\n',''))+ 1) + '\n'
                lines[1] = str(int(t.time())) + '\n'
            f.close
            f = open('users/' + user + '.musx', 'w')
            for i in lines:
                f.write(i)
            f.close()

    # BALANCE CHECK
    
    if msg.startswith('check balance '):
        try:
            f = open('users/' + msg.replace('check balance ','') + '.musx', 'r')
            lines = f.readlines()
            await client.send_message(message.channel, '`' + message.content.replace('check balance ','') + '` has **' + lines[0].replace('\n','') + '** Bling Dollars')
        except:
            await client.send_message(message.channel, 'User with name ` ' + message.content.replace('check balance ','') + ' ` does not exist or does not have any Bling Dollars.')

        
            
            
                
                


##########################################################################
client.run('Mzg5NDkwMzM3NDA1NzMwODE2.DQ8eZQ.yfqly2SMHapnRnkZG6H88T-Te5c')


