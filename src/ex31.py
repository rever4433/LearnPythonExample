print("You enter a dark room with two doors. Do you go throughdoor #1 or door #2?")
door = input("> ")
if door == "1":
 print("There's a giant bear here eating a cheese cake. Whatdo you do?")
 print("1. Take the cake.")
 print("2. Scream at the bear.")
 bear = input("> ")
 if bear == "1":
    print("The bear eats your face off. Good job!")
 elif bear == "2":
    print("The bear eats your legs off. Good job!")
else:
 print("Well, doing %r is probably better. Bear runsaway." %bear)
 
if door == "2":
 print("You stare into the endless abyss at Cthulhu'sretina.")
 print("1. Blueberries.")
 print("2. Yellow jacket clothespins.")
 print("3. Understanding revolvers yelling melodies.")
 
 insanity = input("> ")

 if insanity == "1" or insanity == "2":
         print("Your body survives powered by a mind of jello.Good job!")
 else:
         print("The insanity rots your eyes into a pool of muck.Good job!")
         
else:
 print("You stumble around and fall on a knife and die. Goodjob!")