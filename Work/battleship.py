NUMBER_OF_PLAYERS = 2
NUMBER_OF_SHIPS = 5
BOARD_SIZE = 5

def createBoard(size:int):
    board = [['-' for _ in range(size)] for _ in range(size)]
    return board

def printBoard(board:list[list]):
    for row in board:
        print(row)

def addShip(board:list[list], x, y):
    board[x][y] = '@'

def isShip(board:list[list], x, y):
    if board[x][y] == '@':
        return True 

def initShips(board:list[list]):
    n = 1
    while n <= NUMBER_OF_SHIPS:
        x = y = -1
        print(f'Enter the row number (0-4) for Ship {n}: ', end='')
        while x == -1 or x >= BOARD_SIZE:
            if x >= BOARD_SIZE:
                print(f'Row should be between 0 and {BOARD_SIZE-1}: ', end='')
            x = int(input())
            
        print(f'Enter the column number (0-4) for Ship {n}: ', end='')
        while y == -1 or y >= BOARD_SIZE:
            if y >= BOARD_SIZE:
                print(f'Column should be between 0 and {BOARD_SIZE-1}: ', end='')
            y = int(input())
        if isShip(board, x, y):
            print('Coordinates are already used.')
        else:
            addShip(board, x, y)
            print(f'Ship {n} is {x, y}')
            n += 1
    return board

if __name__ == '__main__':
    print('-' * 30)
    print('Welcome to the world of Battleships')
    print('-' * 30)
    print('You are PLAYER 1.')
    board_1 = createBoard(BOARD_SIZE)
    initShips(board_1)
    printBoard(board_1)
    print('Your are PLAYER 2.')
    board_2 = createBoard(BOARD_SIZE)
    initShips(board_2)
    printBoard(board_2)