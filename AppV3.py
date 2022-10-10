import random
import time
import GameV3
from GameV3 import *
import Mario
from Mario import *
import Luigi
from Luigi import *
"""This is the gane. This is where everything is printed and the user input comes in."""
#Oh by the way I dont know if the code is in Github so i hope it is
print(GameV3.titleText)
GameV3.textTimer(0,GameV3.introLength,GameV3.introTexter,6)
GameV3.textTimer(0,GameV3.dialogueLength,GameV3.dialogueTexter,6)
#strength is used to challenge Donkey Kong
#skill is used to travel the world to get to Bowser's lair
#reason is used to think rationally when fighting Bowser and when dealing with the ending
print("\n\nMario stats: Strength: +1, Reason: -1, Skill: +2\n")
print("Luigi stats: Strength: +2, Reason: +1, Skill: -1")
characterChoose = str(input("\nWho should go slay Bowser and save Princess Peach? Mario or Luigi? ")).lower() # cboose the role you want

if (characterChoose == "mario"):
    print(GameV3.mario+"Brother, I will go. Do not deny me this.")
    time.sleep(GameV3.timingText)
    print(GameV3.luigi+"Hmph. As you wish.")
    time.sleep(GameV3.timingText)
    print(GameV3.luigi+"Then, take this.")
    time.sleep(GameV3.timingText)
    print("Mario receives a pair of magical die.")
    print(GameV3.luigi+"It's a pair of magic die. Roll it and it's numbers will rewrite the future in your favor or disfavor.")
    time.sleep(GameV3.timingText)
    print(GameV3.mario+"Why would I want that? I could easily take the world by force.")
    time.sleep(GameV3.timingText)
    print(GameV3.luigi+"Sure, but just keep it anyway. You never know what'll happen.")
    time.sleep(GameV3.timingText)
    print(GameV3.mario+"Alright fine. I'll be going now. Cya later, Luigi.")
    time.sleep(GameV3.timingText)
    print(GameV3.luigi+"Bye bye!!")
    strength = Mario.strengthMario
    skill = Mario.skillMario
    reason = Mario.reasonMario
    character = Mario.nameMario
    character2 = Luigi.nameLuigi
elif (characterChoose == "luigi"):
    print(GameV3.luigi+"Get some rest, Mario. You've done this too much.")
    time.sleep(GameV3.timingText)
    print(GameV3.mario+"Fine. I guess I am a bit exhausted.")
    time.sleep(GameV3.timingText)
    print(GameV3.luigi+"Mmmm. Good. I guess I'll head out then.")
    time.sleep(GameV3.timingText)
    print(GameV3.mario+"Ah, Luigi, wait. Take this with you.")
    time.sleep(GameV3.timingText)
    print("Luigi receives a pair of magical die")
    print(GameV3.luigi+"What's this?")
    time.sleep(GameV3.timingText)
    print(GameV3.mario+"It's a pair of magical die I found while saving Peach.")
    time.sleep(GameV3.timingText)
    print(GameV3.mario+"If you ever have your back against the wall, then roll it and your problem will go away. Or get worse.")
    time.sleep(GameV3.timingText)
    print(GameV3.luigi+"So, gambling?")
    time.sleep(GameV3.timingText)
    print(GameV3.mario+"Yes, but it's better than being defeated, yes?")
    time.sleep(GameV3.timingText)
    print(GameV3.luigi+"I suppose. Well then, I'll go now. Thank you Mario. Rest well.")
    time.sleep(GameV3.timingText)
    print(GameV3.mario+"Thank you Luigi. I'll see you later")
    strength = Luigi.strengthLuigi
    skill = Luigi.skillLuigi
    reason = Luigi.reasonLuigi
    character = Luigi.nameLuigi
    character2 = Mario.nameMario
else:
    while (characterChoose != "mario" or characterChoose != "luigi"):
     characterChoose = str(input("\nThat isn't an option. Who should go on this final adventure? Mario or Luigi? ")).lower()

     if (characterChoose == "mario"):
         print(GameV3.mario+"Brother, I will go. Do not deny me this.")
         time.sleep(GameV3.timingText)
         print(GameV3.luigi+"Hmph. As you wish.")
         time.sleep(GameV3.timingText)
         print(GameV3.luigi+"Then, take this.")
         time.sleep(GameV3.timingText)
         print("Mario receives a pair of magical die.")
         print(GameV3.luigi+"It's a pair of magic die. Roll it and it's numbers will rewrite the future in your favor or disfavor.")
         time.sleep(GameV3.timingText)
         print(GameV3.mario+"Why would I want that? I could easily take the world by force.")
         time.sleep(GameV3.timingText)
         print(GameV3.luigi+"Sure, but just keep it anyway. You never know what'll happen.")
         time.sleep(GameV3.timingText)
         print(GameV3.mario+"Alright fine. I'll be going now. Cya later, Luigi.")
         time.sleep(GameV3.timingText)
         print(GameV3.luigi+"Bye bye!!")
         strength = Mario.strengthMario
         skill = Mario.skillMario
         reason = Mario.reasonMario
         character = Mario.nameMario
         character2 = Luigi.nameLuigi
         break
     if (characterChoose == "luigi"):
         print(GameV3.luigi+"Get some rest, Mario. You've done this too much.")
         time.sleep(GameV3.timingText)
         print(GameV3.mario+"Fine. I guess I am a bit exhausted.")
         time.sleep(GameV3.timingText)
         print(GameV3.luigi+"Mmmm. Good. I guess I'll head out then.")
         time.sleep(GameV3.timingText)
         print(GameV3.mario+"Ah, Luigi, wait. Take this with you.")
         time.sleep(GameV3.timingText)
         print("Luigi receives a pair of magical die")
         print(GameV3.luigi+"What's this?")
         time.sleep(GameV3.timingText)
         print(GameV3.mario+"It's a pair of magical die I found while saving Peach.")
         time.sleep(GameV3.timingText)
         print(GameV3.mario+"If you ever have your back against the wall, then roll it and your problem will go away. Or get worse.")
         time.sleep(GameV3.timingText)
         print(GameV3.luigi+"So, gambling?")
         time.sleep(GameV3.timingText)
         print(GameV3.mario+"Yes, but it's better than being defeated, yes?")
         time.sleep(GameV3.timingText)
         print(GameV3.luigi+"I suppose. Well then, I'll go now. Thank you Mario. Rest well.")
         time.sleep(GameV3.timingText)
         print(GameV3.mario+"Thank you Luigi. I'll see you later")
    
         strength = Luigi.strengthLuigi
         skill = Luigi.skillLuigi
         reason = Luigi.reasonLuigi
         character = Luigi.nameLuigi
         character2 = Mario.nameMario
         break
print(GameV3.loadingScreen)
GameV3.textTimer(0,GameV3.tutorialLength,GameV3.tutorialTexter,GameV3.timingText)
print(GameV3.loadingScreen)

print("\n"+character+" makes his way to Donkey Kong's jungle.")
time.sleep(GameV3.timingText)
print(character+" arrives at the jungle.")
time.sleep(GameV3.timingText)
print("He looks around for Donkey Kong and eventually finds him.")
time.sleep(GameV3.timingText)
print(str(GameV3.kong)+str(character)+"! What brings you here?")
time.sleep(GameV3.timingText)
print(character+": I've come to borrow the Banana Gun. I need it to slay Bowser once and for all.")
time.sleep(GameV3.timingText)
print(str(GameV3.kong)+str(character)+", I can't just let you have it. That's a sacred treasure. A one-of-a-kind. You cannot have it.")
time.sleep(GameV3.timingText)
print(character+": Please, Kong. I need it.")
time.sleep(GameV3.timingText)
print(GameV3.kong+": How about this? Let's have a contest of strength. We fight snd whoever wins gets what they want. You win, you get the treasure. I win, I get a million bananas.")
time.sleep(GameV3.timingText)
print(character+": A million bananas?? That's alot.")
time.sleep(GameV3.timingText)
print(GameV3.kong+"That's what the Banana Gun is worth. Do you accept?")
time.sleep(GameV3.timingText)
print(character+": You're on.\n")
print("\nCHALLENGE 1 - CONTEST OF STRENGTH\n")
GameV3.rollTheDice(GameV3.roll,character,GameV3.magicalDice1,GameV3.magicalDice2,GameV3.magicDieTotal,character+" wrestles with Donkey Kong.",character+" defeats Donkey Kong.",character+" is defeated by Donkey Kong.\n"+GameV3.kong+"Hah! I win! Looks like you owe me a million bananas! Get to work, "+character+"!",strength,GameV3.yourChance,50,56,GameV3.timingText)

print(character+": *pants* I win. I win, Kong.")
time.sleep(GameV3.timingText)
print(GameV3.kong+"Aghhh. FINE. HERE, TAKE IT AND LEAVE.")
time.sleep(GameV3.timingText)
print(character+" takes the Banana Gun from Donkey Kong.")
print(character+": Thanks, Donkey Kong. I'll repay you when I'm done with Bowser.")
time.sleep(GameV3.timingText)
print(GameV3.kong+"You better.\n\n")
time.sleep(GameV3.timingText)

print(character+" leaves the jungle and begins heading towards Bowser's castle.")
if (characterChoose == "luigi"):
    print(character+": Oh. That's right. I forgot that to get to Bowser's castle, I gotta traverse across a bunch of dangerous regions and fight Bowser's minions.")
    time.sleep(GameV3.timingText)
    print(character+"I'm sure Mario would've had no problem getting to the castle. He's traversed these lands at least a hundred times.\n")
    time.sleep(GameV3.timingText)
else:
    print(character+": Oh that's right. I got to pass through Bowser's territory and deal with Bowser's minions. Shouldn't be too hard.")
    print(character+": *deep breath* One more run. One more run through these regions and I'll be done forever. I'll never have to come back here.\n")
    time.sleep(GameV3.timingText)
print("\nCHALLENGE 2 - THE JOURNEY TO BOWSER'S CASTLE\n")
#Challenge 2
GameV3.rollTheDice(GameV3.roll,character,GameV3.magicalDice1,GameV3.magicalDice2,GameV3.magicDieTotal,character+" begins the journey to Bowser's castle.",character+" arrives at Bowser's castle and makes his way to the throne room.",character+" is defeated while traversing the land.",skill,GameV3.yourChance,50,44,GameV3.timingText)

print(character+" arrives at the throne room.\n\n")

#huh story kinda cringe but anything for a good mark
if (characterChoose == "mario"):
    print(GameV3.bowser+"Ah, Mario, you're fina--")
    time.sleep(GameV3.timingText)
    print(character+": SHUT UP! I'M HERE TO KILL YOU FOR GOOD. THIS WILL NOT HAPPEN AGAIN. I WILL SETTLE THIS ONCE AND FOR ALL.")
    time.sleep(GameV3.timingText)
    print(character+": I'M SICK OF DEALING WITH YOU. HOW MANY TIMES HAVE I DEFEATED YOU NOW? 100? 200? 400? I'VE LOST COUNT.")
    time.sleep(GameV3.timingText)
    print(character+" pulls out the Banana Gun.")
    print(character+": DO YOU SEE THIS? THIS BANANA GUN? DO YOU KNOW WHAT IT DOES?")
    time.sleep(GameV3.timingText)
    print(GameV3.bowser+"W-W-Wait, Mario, let's t-talk. Put that away. I'll k-kill Peach if you s-shoot me..")
    time.sleep(GameV3.timingText)
    print(character+": YOU'RE SCARED. HAHAH, SO THAT MEANS THIS BANANA IS THE REAL DEAL, EH?")
    time.sleep(GameV3.timingText)
    print(GameV3.bowser+"Mario, p-please. Don't s-shoot me. I'm n-not the one behind this kidnapping plot.")
    time.sleep(GameV3.timingText)
    print(character+": OH REALLY? THEN TELL ME, WHO IS? HMM? WHO? TELL ME RIGHT NOW.")
    time.sleep(GameV3.timingText)
    print(GameV3.bowser+"The mastermind is Princess-- AGHHH!!")
    time.sleep(GameV3.timingText)
    print("Bowser falls flat on his face. He is dead it seems.")
else:
    print(GameV3.bowser+"Ahh! There's a face I don't see often! Luigi, brother of Mario, what brings you here? Where is Mario?")
    time.sleep(GameV3.timingText)
    print(character+": Resting. I am here on his behalf.")
    time.sleep(GameV3.timingText)
    print(character+": Bowser. I am here to kill you once and for all with this.")
    print("Luigi pulls out the Banana Gun.")
    time.sleep(GameV3.timingText)
    print(GameV3.bowser+"That's....Luigi, p-put that away. You know w-what it does right?")
    time.sleep(GameV3.timingText)
    print(character+": Yes. I will shoot you with it and end Mario's suffering.")
    time.sleep(GameV3.timingText)
    print(GameV3.bowser+"W-WAIT! WAIT! I'M NOT THE MASTERMIND BEHIND MARIO'S SUFFERING! I SWEAR!")
    time.sleep(GameV3.timingText)
    print(character+": Oh really? Who is it then? Hm? Who?")
    time.sleep(GameV3.timingText)
    print(GameV3.bowser+"The mastermind is Princess--- AGH!!!")
    time.sleep(GameV3.timingText)
    print("Bowser falls flat on his face. He is dead it seems.")
print(character+" stares at Bowser's body and falls into deep thought.")
time.sleep(GameV3.timingText)
print(str(GameV3.peach)+str(character)+"! Oh thank y----")
time.sleep(GameV3.timingText)
print(character+": Shhhhh. Let me think.")
print("\nCHALLENGE 3 - REASON\n")

GameV3.rollTheDice(GameV3.roll,character,GameV3.magicalDice1,GameV3.magicalDice2,GameV3.magicDieTotal,character+" falls into deep thought.",character+" begins realizing that Princess Peach might be the mastermind.",character+" thinks what Bowser said is fake and there's no way a Princess, let alone Peach, would do something like this.\n"+character+" takes Princess Peach and escorts her back home without harboring any suspicions.",reason,GameV3.yourChance,30,24,GameV3.timingText)
print("\n"+character+": (Hmm. The mastermind is a Princess? I only know of 3 Princesses. Princess Peach, Princess Daisy, and Princess Rosalina.)")
time.sleep(GameV3.timingText)
print(character+": (Rosalina and Daisy are far away, I know that is certain. No way, was Bowser going to say Peach? Impossible)")
time.sleep(GameV3.timingText)
print(character+": (But why would he suddenly die like that? Was he silenced?)")
time.sleep(GameV3.timingText)
print(character+": (If it really was Peach then...)")
print(character+" starts thinking back on Peach's past.")
time.sleep(GameV3.timingText)
print(character+": (She was kidnapped well over a hundred times. Every time she was rescued, she went right back to her castle and barely, no not barely, she did nothing to improve security. She stayed in the same vulnerable castle over and over again.)")
time.sleep(GameV3.timingText)
print(character+": (And her gratitude to being rescued....even the first time she was saved, her reaction was almost too cool and collected.)\n")
time.sleep(GameV3.timingText)
print(character+": Peach! Is it really you? Are you the one doing all this?")
time.sleep(GameV3.timingText)
print(GameV3.peach+"Of course not! Why would I ever do something like this?\n")

#this whole part is the ending
#theEnding is user input 
theEnding = str(input(character+": (What should I do? I don't want to believe that it's her but I feel like she is the mastermind. What should I do? Trust her or kill her?) ('trust' or 'kill)  ")).lower()
if (theEnding == "trust"):
    time.sleep(GameV3.timingText)
    print("\n"+character+": Alright then. I believe you. Come, let's get out of here.")
    time.sleep(GameV3.timingText)
    print(GameV3.peach+"Thank you for saving me, "+character+"! I hope this never happens again!")
    time.sleep(GameV3.timingText)
    print(character+" escorts Peach back to her castle without harboring any suspicions.")
elif (theEnding == "kill" or theEnding == "shoot"):
    time.sleep(GameV3.timingText)
    print("\n"+character+" points the Banana Gun at Princess Peach and fires.")
    time.sleep(GameV3.timingText)
    print(GameV3.peach+"GAAAAAAAHHHHHHHHHHHH!!!!!!!!")
    print("Princess Peach's body begins to turn into someone else. Someone familiar.....")
    time.sleep(GameV3.timingText)
    print(GameV3.wario+"AHHHH YOU CRAZY LUNATIC!! WHY WOULD YOU EVER SHOOT PEACH?!?!?!?")
    time.sleep(GameV3.timingText)
    print(GameV3.wario+"AHAHAHA!!! I GOT YOU REAL GOOD THOUGH, DIDN'T I?")
    time.sleep(GameV3.timingText)
    print(character+": WHERE IS PEACH? WHERE IS SHE?")
    print("Wario dies.")
    time.sleep(GameV3.timingText)
    print(character+": Dammit. Well, I guess I should head back and tell "+character2+" about this. We'll need to find the real Peach.")
else:
    while (theEnding != "shoot" or theEnding != "kill" or theEnding != "trust"):
        theEnding = str(input("Decide. Trust the Princess or kill the Princess? ('trust' or 'kill')  "))
        if (theEnding == "trust"):
          time.sleep(GameV3.timingText)
          print("\n"+character+": Alright then. I believe you. Come, let's get out of here.")
          time.sleep(GameV3.timingText)
          print(GameV3.peach+"Thank you for saving me, "+character+"! I hope this never happens again!")
          time.sleep(GameV3.timingText)
          print(character+" escorts Peach back to her castle without harboring any suspicions.")
          break
        elif (theEnding == "kill" or theEnding == "shoot"):
          time.sleep(GameV3.timingText)
          print("\n"+character+" points the Banana Gun at Princess Peach and fires.")
          time.sleep(GameV3.timingText)
          print(GameV3.peach+"GAAAAAAAHHHHHHHHHHHH!!!!!!!!")
          print("Princess Peach's body begins to turn into someone else. Someone familiar.....")
          time.sleep(GameV3.timingText)
          print(GameV3.wario+"AHHHH YOU CRAZY LUNATIC!! WHY WOULD YOU EVER SHOOT PEACH?!?!?!?")
          time.sleep(GameV3.timingText)
          print(GameV3.wario+"AHAHAHA!!! I GOT YOU REAL GOOD THOUGH, DIDN'T I?")
          time.sleep(GameV3.timingText)
          print(character+": WHERE IS PEACH? WHERE IS SHE?")
          print("Wario dies.")
          time.sleep(GameV3.timingText)
          print(character+": Dammit. Well, I guess I should head back and tell "+character2+" about this. We'll need to find the real Peach.")
          break
    
print("THE END\n\nTHANK YOU FOR PLAYING!!\n\nCredits: Dylan Tran")
quit()
    