def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check row
            return True
        if all(board[j][i] == player for j in range(3)):  # Check column
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):  # Top-left to bottom-right
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Top-right to bottom-left
        return True

    return False

def is_draw(board):
    """Checks if the game is a draw (no empty spaces left)."""
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic-Tac-Toe."""
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Get the current player's move
        print(f"Player {players[current_player]}'s turn.")
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            # Validate input and check if the cell is empty
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("Cell already taken. Choose another.")
                continue

            # Make the move
            board[row][col] = players[current_player]
            print_board(board)

            # Check for a winner or draw
            if check_winner(board, players[current_player]):
                print(f"Player {players[current_player]} wins!")
                break
            if is_draw(board):
                print("It's a draw!")
                break

            # Switch to the other player
            current_player = 1 - current_player

        except ValueError:
            print("Invalid input. Please enter numbers only.")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()