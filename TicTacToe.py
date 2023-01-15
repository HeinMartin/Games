import numpy as np

class TicTacToePlayer:
    def __init__(self, token, name):
        self.token = token
        self.name = name

    def getToken(self) -> str:
        return self.token

    def getName(self) -> str:
        return self.name

# saving peviously set tokens, initialize with no tokens
field = np.array([ ["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"] ])

def drawField(tabOffset=False) -> None:
    for row in field:
        if tabOffset == True:
            print("\t", end="")
        for col in row:
            print("|_{}_".format(col), end = "")

        print("|")
            
def clearField(printInfo=False) -> None:
    global field
    field = np.array([ ["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"] ])
    
    if printInfo == True:
        print("The Field is cleared.")

def addNewToken(row, col, token, overwrite=False) -> int:

    '''
    This function adds a given token to the field at given row (downwards) and column (sidewards), 
    both integers from 1 to 3.
    You can also let this function overwrite already set tokens by setting overwrite=True; 
    the default value is overwrite=False.
    Return values:
         0  token was set successfully
        -1  type of row or column position is no integer
        -2  type of token is no string
        -3  already set token can not be overwritten (overwrite=False)
        -4  position to set token is out of range
    '''

    # check for valid position and token input
    if type(row) != int or type(col) != int:
        # input is no integer
        return -1
    if type(token) != str:
        # input is no valid token
        return -2

    if (row >= 1 and row <= 3) and (col >= 1 and col <= 3):
        if overwrite == False:
            if field[row-1][col-1] != "_":
                # there is already a token set and can not be overwritten
                return -3

        field[row-1][col-1] = token
        return 0
    else:
        # position is invalid
        return -4

def positionInput(_input) -> int:
    pos = 0

    try:
        pos = int(_input)
    except ValueError:
        return None
    if pos >= 1 and pos <= 3:
        return pos
    else:
        return None

def checkFullField() -> bool:
    for i in field:
        for j in i:
            if j == "_":
                return False

    return True

def checkWinner(player) -> bool:
    # check constellations for field for winning condition
    t = player.getToken()
    for i in range(0, 3):
        if np.array_equal(field[i,:], [t, t, t]):
            return True
        elif np.array_equal(field[:,i], [t, t, t]):
            return True
    if [field[0][0], field[1][1], field[2][2]] == [t, t, t]:
        return True
    elif [field[2][0], field[1][1], field[0][2]] == [t, t, t]:
        return True
    
    return False

def winningSequence(player) -> None:
    print("\t{} wins the game!".format(player.getName()))

def lobby() -> TicTacToePlayer:
    # Create Player1 and Player2.
    print("\nCreating Players...")
    print("\nYou can give each Player a name. Otherwise press ENTER.")
    
    name = input("Name for Player1: ")
    if name == "":
        name = "Player1"
    player1 = TicTacToePlayer('X', name)
    
    name = input("Name for Player2: ")
    if name == "":
        name = "Player2"
    player2 = TicTacToePlayer('O', name)

    # Information about Player.
    print("\n{} with token: {}".format(player1.getName(), player1.getToken()))
    print("{} with token: {}".format(player2.getName(), player2.getToken()))
    
    # Declare First Player.
    print("\n{} starts...".format(player1.getName()))
    currentPlayer = player1
    print("")

    # Create field.
    clearField()
    drawField()
    print("")

    return player1, player2, currentPlayer

# methods for testing mode
def setWinningField(constellation: int, t = "X",  draw = False) -> None:
    global field

    if constellation == 0:
        field[0,:] = [t, t, t]
    elif constellation == 1:
        field[1,:] = [t, t, t]
    elif constellation == 2:
        field[2,:] = [t, t, t]
    elif constellation == 3:
        field[:,0] = [t, t, t]
    elif constellation == 4:
        field[:,1] = [t, t, t]
    elif constellation == 5:
        field[:,2] = [t, t, t]
    elif constellation == 6:
        field[0][0], field[1][1], field[2][2] = t, t, t
    elif constellation == 7:
        field[0][2], field[1][1], field[2][0] = t, t, t
    
    if draw == True:
        drawField()

def setFullField() -> None:
    global field
    for i in range(0, 3):
        for j in range(0, 3):
            field[i][j] = "Y"


def main():

    player1, player2, currentPlayer = lobby()

    # idea: print also "row" and "column" next to field --> let player decide to use it
    while(1):

        print("It\'s {}\'s turn.".format(currentPlayer.getName()))
        
        # let the player set the row from 1-3
        x = positionInput(input("row:\t"))
        while x == None:
            print("Try again!")
            print("Type in integer values in in from 1 to 3.")
            x = positionInput(input("row:\t"))

        # let the player set the column from 1-3
        y = positionInput(input("column:\t"))
        while y == None:
            print("Try again!")
            print("Type in integer values in in from 1 to 3.")
            y = positionInput(input("column:\t"))

        # if the chosen position is empty set token
        # if the position is occupied, it's the same player's turn
        if addNewToken(x, y, currentPlayer.getToken()) == -3:
            print("This position is already occupied!")
            continue

        # print field
        drawField()
        print("")

        # check if the current player wins
        if checkWinner(currentPlayer) == True:
            # set winning sequence
            winningSequence(currentPlayer)
            
            # ask for play again -> restart by going to lobby, or terminate
            answer = input("\nDo you want to Play again? Y/y or N/n: ")
            while answer != "N" and answer != "n" and answer != "Y" and answer != "y":
                answer = input("Sorry? Please type \"Y\" or \"y\" for yes, \"N\" or \"n\" for no: ")
            if answer == "N" or answer == "n":
                print("\nThank you for playing!")
                break
            else:
                player1, player2, currentPlayer = lobby()
                continue
        
        # check for completely filled Field, so a draw
        if checkFullField() == True:
            print("The field is filled completely! No one wins!")
            
            # ask for play again -> restart by going to lobby, or terminate
            answer = input("\nDo you want to Play again? Y/y or N/n: ").strip().lower()
            while answer != "n" and answer != "y":
                answer = input("Sorry? Please type \"Y\" or \"y\" for yes, \"N\" or \"n\" for no: ")
            if answer == "n":
                print("\nThank you for playing!")
                break
            elif answer == "y":
                player1, player2, currentPlayer = lobby()
                continue
        
        # switch player
        if currentPlayer == player1:
            currentPlayer = player2
        else:
            currentPlayer = player1
        
if __name__ == "__main__":
    main()
