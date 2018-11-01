from random import randint

computer_lives = 5
player_lives = 5

# available weapon => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False


# make the computer pick one item at random
computer = choices[randint(0, 2)]


# define a win or lose function instead of the proctional way
def winoloss(status):
    # handle win or lose based on the status we pass in
    print("Called the win or lose function")
    print("*******************************")
    print("You", status, "!", "Would you like to play again")
    choice = input("Y/N: ")

    if choice == "Y" or choice == "y":
        # reset the game
        # change global variable
        global player_lives
        global computer_lives
        global player
        global computer

        player_lives = 5
        computer_lives = 5
        player = False
        computer = choices[randint(0, 2)]

    elif choice == "N" or choice == "n":
        print("You chose to Quit")
        exit()


# show the computer's choice in the terminal window
print("Computer chooses: ", computer)

while player is False:
    print("=====================================")
    print("computer_lives", computer_lives, "/5")
    print("player_lives", player_lives, "/5")
    print("=====================================")
    print("Choose your weapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    # print("Player chooses:", player)

# check to see if you picked the same thing
    if (player == computer):
        print("Tie! Live to shoot another day")
        print("computer", computer_lives, "player", player_lives)

    elif player == "Rock":
        if computer == "Paper":
            # compuer won
            player_lives -= 1
            print("You lose", computer, "covers", player, "\n")
        else:
            print("You win!", player, "smashes", computer, "\n")
            computer_lives -= 1

    elif player == "Paper":
        if computer == "Scissors":
            player_lives -= 1
            print("You lose!", computer, "cuts", player, "\n")
        else:
            print("You win!", player, "covers", computer, "\n")
            computer_lives -= 1

    elif player == "Scissors":
        if computer == "Rock":
            player_lives -= 1
            print("You lose!", computer, "samshes", player, "\n")
        else:
            print("You win!", player, "cuts", computer, "\n")
            computer_lives -= 1

    elif player == "Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!""\n")

    # handle win or lose
    if player_lives is 0:
        winoloss("lost")

    elif computer_lives is 0:
        winoloss("won")

    player = False
    Computer = choices[randint(0, 2)]
