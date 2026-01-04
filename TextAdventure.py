# Text-Based RPG Game
# Author: Your Name
# Description: A command-line RPG where players make choices to rescue a princess.
import sys  # Importing sys module to handle system-specific parameters and functions #

def main():  # Main function to run the RPG game 
    print("Welcome to our RPG game!")
    while True:  # Loop to allow restarting the game 
        print("This is the start of the game, you're either here to restart your adventure or begin your quest.")
        command = input("Enter one of the commands for the game either 'menu', 'start adventure', or 'quit': ")  # command - user input
        if command.lower() == 'menu':  # lower - converts input to lowercase
            print("Welcome to the menu of our game")
            print("Would you like to see the instructions and the lore? (yes/no)")
            response = input("> ")  # response - user input
            if response.lower() == 'yes':
                print("Here are the instructions and lore:")
                print("Instructions:")
                print("1. Use command: 'menu', 'scenario 1', 'scenario 2', or 'start adventure' to access the game.")
                print("2. Follow the prompts to navigate the game.")
                print("Lore:")
                print("The goblin king has kidnapped the princess. Your quest is to rescue her from the goblin fortress.")
                print("You are a brave knight on a quest to save the kingdom.")
                print("Start your adventure by typing the command 'start adventure'")
            else:
                print("Okay, you can continue on your quests!")
        elif command.lower() == 'start adventure':
            start_adventure()
        elif command.lower() in ('quit', 'exit'):
            print("Goodbye!")
            sys.exit()  # Exit the program #
        else:
            print(f"You entered: {command}")  # Echo the command back to the user #

def start_adventure():  # Function to handle the adventure scenarios 
    print("You've just started your adventure")
    print("Good luck on your quest to save the princess from the goblin king!")
    # Adventure loop to handle scenarios
    while True:
        print("Enter 'scenario 1' to face your first challenge, 'scenario 2' for the throne room, or 'quit' to return to the menu.")
        cmd = input("> ")  # cmd - user input
        if cmd.lower() == 'scenario 1':
            print("You've encountered the entrance to the goblin camp.")
            print("What will you do?")
            print("1. sneak into the goblin camp")
            print("2. face the goblins head-on")
            action = input("> ")
            if action == "1":
                print("You sneak into the goblin camp. You successfully avoid detection!")
                print("You can now proceed to 'scenario 2' when ready.")
            elif action == "2":
                print("You face the goblins head-on. You die a heroic death! Although you have failed your quest, your bravery will be remembered.")
                return
            else:
                print("Invalid action.")
        elif cmd.lower() == 'scenario 2':
            print("You've reached the goblin king's throne room.")
            print("What will you do?")
            print("1. challenge the goblin king to a duel")
            print("2. try to negotiate with the goblin king")
            action = input("> ")  # action - user input
            if action == "1":
                print("You challenge the goblin king to a duel and emerge victorious!")
                print("You have rescued the princess and completed your quest!")
                print("Congratulations, brave knight!")
                return
            elif action == "2":
                print("You try to negotiate with the goblin king, but he refuses to release the princess.")
                print("You are captured and thrown into the dungeon.")
                return
            else:
                print("Invalid action.")
        elif cmd.lower() in ('quit', 'exit'):  # Allow quitting the adventure # cmd - user input
            return
        else:
            print("Unknown command inside adventure.")

if __name__ == '__main__':  # Entry point of the program 
    main()
