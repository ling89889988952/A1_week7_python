from random import randint

computer_lives = 3
player_lives = 3
computer_choice = ""
player_choice = ""

# available weapon => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False


# make the computer pick one item at random
computer = choices[randint(0, 2)]


# show the computer's choice in the terminal window
print("Computer chooses: ", computer)

while player is False:
    print("Choose your weapon!\n")
    player = input("Rock, Paper or Scissors?\n")
    print("Player chooses: ", player)

# check to see if you picked the same thing
    if (player == computer):
        print("Tie! Live to shoot another day")
        print("computer", computer_lives, "player", player_lives)

    elif player == "Rock":
        if computer == "Paper":
            # compuer won
            computer_lives = computer_lives + 1
            player_lives = player_lives - 1
            print("You lose", computer, "covers", player)
            print("computer_lives", computer, "player_lives", player)
        else:
            computer_lives = computer_lives - 1
            player_lives = player_lives + 1
            print("You win!", player, "smashes", computer)
            print("computer_lives", computer, "player_lives", player)

    elif player == "Paper":
        if computer == "Scissors":
            computer_lives = computer_lives + 1
            player_lives = player_lives - 1
            print("You lose", computer, "covers", player)
            print("computer_lives", computer, "player_lives", player)
        else:
            computer_lives = computer_lives - 1
            player_lives = player_lives + 1
            print("You win!", player, "covers", computer)
            print("computer_lives", computer, "player_lives", player)

    elif player == "Scissors":
        if computer == "Rock":
            computer_lives = computer_lives + 1
            player_lives = player_lives - 1
            print("You lose!", computer, "samshes", player)
        else:
            omputer_lives = computer_lives - 1
            player_lives = player_lives + 1
            print("You win!", player, "cuts", computer)
            print("computer_lives", computer, "player_lives", player)

    elif player == "Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check your spelling!")

    if (int(computer_lives > 0)) or (player_lives > 0):
        print("Game continue")
        print("computer_lives", computer, "player_lives", player)

    elif (int(computer_lives == 0)) or (player_lives == 0):
        print("Game over")
        print("computer_lives", computer, "player_lives", player)
        exit()

    player = False
    computer = choices[randint(0, 2)]

