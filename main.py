print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
 
''')

print("Welcome to Treasure Island!")
print("Let's begin the game. Your mission is to find the treasure!")
while True:
    choice1 = input("You are at a crossroad, where do you want to go 'left' or "
                    "'right'? ↔ \n").lower()

    if choice1 == "left":
        choice2 = input("You\'ve come to a lake. There is an island in the middle "
                        "of the lake.\n Type 'wait' or 'swim' to continue.\n").lower()

        if choice2 == "wait":
            choice3 = input(
                "Great! You are close to your treasure. There are three "
                "doors in front of you. One red , one yellow and one "
                "blue. Which one would you like to go "
                "through? 🚪\n Type 'red' or 'blue' or 'yellow' to reach "
                "your "
                "destination!\n").lower()

            if choice3 == "red":
                print("Oh no! You were burned by fire 🔥."
                      "Game over.❌ ")
            elif choice3 == "blue":
                print("I guess, it was not your day. You were eaten by the "
                      "beasts. Game over ❌")
            elif choice3 == "yellow":
                print("Hey you were a pro! Congrats you win 🏆. The treasure is "
                      "all yours 🔑...")
            else:
                print("Game Over!!!")

        else:
            print("Alas! You were attacked by an angry trout. Game over ❌")

    else:
        print("Oops! you fell into a pit 🕳️. Game Over ❌")

    ch = (input("Do you want to play again? Type 'yes' or 'no'.\n ")).lower()
    if ch == "yes" or ch == "y":
        continue
    else:
        break








