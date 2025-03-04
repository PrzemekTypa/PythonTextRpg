import os
import time
import sys

# Variable for riddles
riddle_solved = False

# Variables for time module
a = 0.05
b = 4
c = 1
d = 10

#Display starting menu
def prompt():
    print("\t\t\tWelcome to my game\n\n\
    \t  The king has given you a mission to rescue Princess\n\tnamed Fiona who is being held captive by a dragon.\n\t"
      "For the promise of payment in gold and the hand\n\tof the princess, you gladly accept the request.\n\t"
      "After a long journey, you finally reach the castle walls.\n\tThe sun is just setting.\n\tDrawbridge is open,"
      " entering carefully\n\tyou can see three paths.\n\n\
    Moves: 'go {direction}' (travel north, south, east, or west)\n\
    \t   'get/take {item}' (add nearby item to inventory)\n\n")

    input("Press any key to continue...")

#Clears screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# map
rooms = {
    'Main hall': {'North': 'Library', 'West': 'Round room', 'East': 'Dead end room'},
    'Library': {'North': 'UndeadWarrior room', 'South': 'Main hall'},
    'Round room': {'East': 'Main hall', 'Item': 'Sword'},
    'Dead end room': {'West': 'Main hall'},
    'UndeadWarrior room': {'West': 'Corridor', 'Boss': 'Undead Warrior'},
    'Corridor': {'North': 'Troll room', 'West': 'Storage room',},
    'Storage room': {'East': 'Corridor', 'Item': 'Shield'},
    'Troll room': {'North': 'Dining room', 'Boss2': 'Troll', 'Item': 'Helmet'},
    'Dining room': {'North': 'Dragons lair', 'East': 'Bedroom', 'Item': 'Potion'},
    'Bedroom': {'West': 'Dining room', 'Item': 'Armor', 'Boss3': 'Weird looking Ogre'},
    'Dragons lair': {'Boss4': 'Dragon'}
    }

#Inventory list
inventory = []


#Track current room
current_room = "Main hall"



#result of last move
msg = ""

clear()
prompt()

#Gameplay loop
while True:

    clear()

    #display info of current room and items held
    if current_room == "Main hall":
        print(f"You enter the {current_room}.\nIt is an old abandoned room, amazing in its size.\nNo one has been here for a long time.\nYou see three paths: (North/West/East) \nInventory : {inventory}\n{'-' * 25}")
    
    elif current_room == "Library":
        print(f"You are in the {current_room}.\nStrange noises can be heard\noutside the north door.You can\nopen the door and check where \nthe noise is coming from\nor go back and look around.\n What do you do?: (North/South)\nInventory : {inventory}\n{'-' * 25}")
        if len(inventory) < 1:
            print("\nYou dont feel prepared.\n")
        elif len(inventory) == 1:
            print("\nWith the sword in your hand you feel comfortable to check whats in the next room.\n")
    
        
    elif current_room == "Round room" and not riddle_solved:
        print(f"You are in the {current_room}.\nAn old man sitting in the corner of the room greets you.\n\nInventory : {inventory}\n{'-' * 25}")
        dialogue = "'If you guess the riddle I'll let you take the prize,\nBUT if you don't know the answer\nI'll turn you into a donkey.\nWhat goes on four legs in the morning, two legs in the afternoon, and three legs in the evening?\n'"
        for character in dialogue:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(a)
                
        
        answer = input("What is your answer?: ")
        if answer.lower() == "man" or answer.lower() == "human":
            dialogue = "'\nCorrect, you can take your reward and leave.\n(get sword/go east)\n'"
            for character in dialogue:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(a)
            riddle_solved = True
            
        else:
            print("Too bad, You'll be a donkey for the rest of your life.\n\nGAME OVER.\n")
            time.sleep(d)
            break

    
    
    elif current_room == "Dead end room":
        print(f"You are in the {current_room}.\nThere is a lever in the middle of the room.\nWhat do you want to do?\n(go west/pull)\nInventory : {inventory}\n{'-' * 25}")
        if user_input.casefold() == "pull":
            print("The moment you pull the lever, a trap door opens below you.\nYou fall straight onto the spikes.\nYou're Dead.")
            time.sleep(d)
            break
        elif user_input.casefold() == "go west":
            action == "go west"
        
    elif current_room == "Corridor":
        print(f"You are in the long {current_room}.\nThere is a small Storage room in the west and some big door leading north. (west/north) \nInventory : {inventory}\n{'-' * 25}")
        
    
    elif current_room == "Storage room":
        print(f"You are in the {current_room}.\nBetween the brooms and the pile of lumber, you see a shiny shield.\nWhat do you do? (go east/get Shield)\nInventory : {inventory}\n{'-' * 25}")
    
    elif current_room == "Dining room":
        print(f"You are in the {current_room}.\nThe last opponent is waiting behind the northern door.\nThere are lots of potions on the table.\nWhat do you do. (north/east/potion)\nInventory : {inventory}\n{'-' * 25}")
        if len(inventory) < 5:
            print("You realize you're not fully prepared for this fight.")
        elif len(inventory) >= 5:
            print("Fully armed, you're ready to finally face the dragon.")
        
            
    #Display msg
    print(msg)

    #Item indicator
    if "Item" in rooms[current_room].keys():

        nearby_item = rooms[current_room]["Item"]

        if nearby_item not in inventory:
            print(f"You see a {nearby_item}")

    
    #boss encounter
    if 'Boss' in rooms[current_room].keys():
        
        #Lose
        if len(inventory) < 1:
            print(f"You are in the {current_room}. \nInventory : {inventory}\n{'-' * 25}")
            print(f"Without any equipment, you had no chance of defeating {rooms[current_room]['Boss']}.\nYou're dead.")
            time.sleep(d)
            break
        #Win
        else:
            print(f"You are in the {current_room}. \nInventory : {inventory}\n{'-' * 25}")
            print(f"Having a sword, you easily defeated the {rooms[current_room]['Boss']}!\nThe only way available is the west.")
            
    elif 'Boss2' in rooms[current_room].keys():
        
        #Lose
        if len(inventory) < 2:
            print(f"You are in the {current_room}. \nInventory : {inventory}\n{'-' * 25}")
            print(f"With the sword alone you failed to attack and defend at the same time from {rooms[current_room]['Boss2']} massive club.\nYou're dead.")
            time.sleep(d)
            break
        #Win
        else:
            print(f"You are in the {current_room}. \nInventory : {inventory}\n{'-' * 25}")
            print(f"With a shield, you were able to block the {rooms[current_room]['Boss2']} attacks with ease.You won the skirmish!\nAlso the {rooms[current_room]['Boss2']} dropped his helmet.\nThe road leads north. (north/helmet)")
    
    elif 'Boss3' in rooms[current_room].keys():
        
        #Lose
        if len(inventory) < 4:
            print(f"You are in the {current_room}. \nInventory : {inventory}\n{'-' * 25}")
            print(f"You see {rooms[current_room]['Boss3']} sleeping in the bed.\nYou try to sneak in silently but the Ogre suddenly wakes up and smack you on the head.\nHe then quickly apologizes, however the lack of helmet or potion make this wound fatal.\nYou're dead. ")
            time.sleep(d)
            break
        #Win
        else:
            print(f"You are in the {current_room}. \nInventory : {inventory}\n{'-' * 25}")
            print(f"You see {rooms[current_room]['Boss3']} sleeping in the bed.\nYou sneak in silently and deliver the killing blow!\nYou see the armor lying on the chair, it's a bit small but you'll fit in somehow. (west/armor)")

    elif 'Boss4' in rooms[current_room].keys():
        
        #Lose
        if len(inventory) < 5:
            print(f"You are in the {current_room}. \nInventory : {inventory}\n{'-' * 25}")
            dialogue = '"WHO DARE DISTURB ME?!"'
            for character in dialogue:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(a)
                time.sleep(c)

            print()
            print(f"then a huge {rooms[current_room]['Boss4']} emerges from behind a pillar. Without being fully armed, the {rooms[current_room]['Boss4']} quickly turns you into a living torch.\n You're dead.")
            time.sleep(d)
            break
        #Win
        else:
            print(f"You are in the {current_room}. \nInventory : {inventory}\n{'-' * 25}")
            time.sleep(c)
            print(f"After a fierce battle, you manage to land the final blow on {rooms[current_room]['Boss4']},\nyou ask the beast:\n")
            time.sleep(c)
            dialogue = '"Where is the princess?!"'
            for character in dialogue:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(a)
            print()
            time.sleep(c)
                
            print(f"\nWith his last breath, the {rooms[current_room]['Boss4']} replies:\n")
            time.sleep(c)
            dialogue = '"You fought bravely, you deserve to go with the princess. Shes waiting for you in the bedroom."'
            for character in dialogue:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(a)
            print()
            time.sleep(c)
            
            print("\nSuddenly it dawned on you, the king mentioned something\nabout the princess's strange behavior during the night.\n")
            time.sleep(b)
            print("The monster in the bedroom you slew wasn't an Ogre.\n")
            time.sleep(b)
            print("Realizing this, you decide to leave the castle and never show up in these lands again.\n\n")
            time.sleep(b)
            print(f"{'-' * 25}THE END{'-' * 25}\n\n")
            time.sleep(d)
            break



    # Player move as input
    user_input = input("Enter your move:\n")
    
        
    #Splits move into words
    next_move = user_input.split(' ')

    #First word is action
    action = next_move[0].title()

    if len(next_move) >1:
        item = next_move[1:]
        direction = next_move[1].title()

        item = ''.join(item).title()

    #Moving between rooms
    if action == "Go":

        try:
            current_room = rooms[current_room][direction]
            msg = f"You travel {direction}."
            
        except:
            msg = f"You can't go that way."

    #Picking up items
    elif action == "Get" or "take":

        try:
            if item == rooms[current_room]["Item"]:

                if item not in inventory:

                    inventory.append(rooms[current_room]["Item"])
                    msg = f"You picked {item}."

                else:
                    msg = f"You already have the {item}."

            else:
                msg = f"Can't find {item}."

        except:
            msg = "Wrong answer."

    #Exit game
    elif action == "Exit":
        break
    
    
    # Any other commands
    else:
        msg = "Invalid Command"

    