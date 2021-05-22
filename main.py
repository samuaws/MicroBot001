import discord
import random
from keep_alive import keep_alive
keep_alive()
playing=False
guessing=False
replay=False
t1=""
t2=""
l=""
arr=list()
wrong=list()
from discord.ext import commands
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

async def start_game(message):
  print("starting")
  print(message.author.name)
  global author
  global playing
  playing=True
  author = message.author.id 
  await message.channel.send("Let's start ! Give 2 truths and than 1 lie")


@client.event
async def on_message(message):
  global t1
  global t2
  global l
  global arr
  global wrong
  global playing
  global guessing
  global replay
  if message.content == ".play" : 
    arr.clear()
    wrong.clear()
    t1=""
    t2=""
    l=""
    guessing = False
    replay=True 
    await start_game(message)
  
   
  if message.author.id!=client.user.id :
    if  playing or replay:
      if author == message.author.id :
        
        if t1 == "" :
          
          if message.content==".play" : 
            pass
          else :
            t1 = message.content
            arr.append(t1)
            await message.delete()
            await message.channel.send("I have your first truth")
        elif t2 == "":
          t2 = message.content
          arr.append(t2)
          await message.delete()
          await message.channel.send("I have your second truth")
        elif l == "" :
          l= message.content
          arr.append(l)
          await message.delete()
          await message.channel.send("I have your lie")
          random.shuffle(arr)
          print(arr)
          await message.channel.send('1- ' + arr[0] +'\n' +'2- ' + arr[1] + '\n' + '3- ' + arr[2])
          guessing=True
      if guessing :
        print("i'm here")
        if author != message.author.id :
          print("I'm there")
          if l != "" :
            if (message.content == str(arr.index(l)+1)) & ((str(message.author.name) in wrong) == False) : 
              await message.channel.send(str(message.author.name)+" is the winner!")
              playing = False 
              arr.clear()
              wrong.clear()
              t1=""
              t2=""
              l=""
            else : 
              if (str(message.author.name) in wrong) == False :  
                 await message.channel.send(str(message.author.name)+" you're WRONG!")
                 wrong.append(str(message.author.name))

  if message.content == ".help" :
    await message.channel.send("```Anglais:\n Do you know your friends well?\n To start the mini-game type \".play\" to call MicroBot!\n You and your friends, turn by turn, each of you will write to the MicroBot 2 truths then a lie about you (one after the other ), then your friends will try to guess which lie among your 3 statements by typing the number of the sentence, but choose well because you will only have one chance.\n You can restart at any point of your game if no one found the right answer by retyping \".play\".\n\nFrançais:\n Connaissez-vous bien vos amis ? \n Pour commencer le mini-jeu tappez \".play\" afin d'appeller MicroBot! \n Vous et vos amis, tour par tour, chaqu'un de vous allez ecrir au  MicroBot 2 vérités puis un mensonge sur vous (une apres l'autre)  puis vos amis vont tenter de deviner la quelle  d'entre vos 3 déclarationsest fausse en tappant le numero de la phrase, mais choisissez bien car vous n'aurez qu'une seule chance.\n Vous pouvez recommencer de votre jeu à tout moment si personne n'a trouvé la bonne réponse en retapant \".play\".```")
        
        

 

client.run("ODQ1MjU3OTEyNzkxMzM0OTMy.YKeVxg.RlGPHbJTdVuKf_ynCAGQZhBX7Wo")
