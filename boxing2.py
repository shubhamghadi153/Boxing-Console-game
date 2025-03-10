player = input("Enter a Player name : ")
 
print("Welcome To Game",player)

start = input("Enter a s to start the game or e to exit : ")
class attack():
    __score =0
    def kick(self):
        self.__score= self.__score + 10

        return f"Score is {self.__score}"
    def punch(self):
        self.__score= self.__score + 5

        return f"Score is {self.__score}"
    def sidekick(self):
        self.__score = self.__score + 15
        return f"Score is {self.__score}"
    def  defence(self):
        self.__score = self.__score -5
        
        return f"Score is {self.__score}"

def handle_move(obj, move):
    if move.upper() == "K":
        return obj.kick()
    elif move.upper() == "P":
        return obj.punch()
    elif move.upper() == "S":
        return obj.sidekick()
    elif move.upper() == "D":
        return obj.defence()
    else:
        return "Invalid move!"  # Handle invalid move input



# Main game logic inside the boxing function
def boxing():
    obj = attack()  # Create an instance of the attack class
    highest_score = 0  # Track the highest score
    action = input("Enter your choice: 'A' for attack or 'D' for defence: ")
    for i in range(5):  # Loop for 5 rounds
        # Ask the user for an action (attack or defence)
        
        if action.upper() == "A":
            move = input("Enter your move: 'K' for kick, 'P' for punch, 'S' for sidekick, 'D' for defence: ")
            print(handle_move(obj, move))
        elif action.upper() == "D":
            print(obj.defence())
        else:
            print("!!!Invalid Action!!!")  # Handle invalid actions

        # Dynamically update the highest score
        if obj._attack__score >= highest_score:
            highest_score = obj._attack__score

    # Display the results at the end of the game
    print(f"Congratulations {player}, Your final score is {obj._attack__score}")
    print(f"Highest score till now is {highest_score}")

    # Replay option
    again = input("Enter 'A' to play again or any other key to quit: ")
    if again.upper() == "A":
        boxing()  # Recursive call to restart the game
    else:
        print("Thanks for playing!")

# Entry point for starting or exiting the game
if start.upper() == "S":
    boxing()
elif start.upper() == "E":
    print("Exit successfully")
else:
    print("Invalid Selection!!!")

print("............Game Over............")