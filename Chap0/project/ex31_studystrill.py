print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

doorwant = input("> ")

print("Sudentlly, a heavily wind push you into the door #1,and there are twice the doors around you")
print("This is the door.\n#1\t#3\n   You\n#2\t#4\nWhich one do you like?")

door = input("> ")

if door == "1":
    print("There's a gaint bear here eating a cheese cake. What do you do?")
    print("1. Take a cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your leg off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear run away" % bear)

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity =="2":
        print("Your body survives powered by a mind of jello. Good jobs!")
    else:
        print("The insanity rote your eyes into a pool of muck. Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
