def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True

    return False


def is_draw(board):
    return all(cell in ["X", "O"] for cell in board)


def start_up():
    print("================================")
    print("     TIC TAC TOE GAME")
    print(" Developed by Sheharyar Sarmad")
    print("================================")
    print("Board Positions:")
    print(" 1 | 2 | 3 ")
    print("---|---|---")
    print(" 4 | 5 | 6 ")
    print("---|---|---")
    print(" 7 | 8 | 9 ")
    print()


def end_up():
    print("\nThanks for playing!")
    print("Developed by Sheharyar Sarmad")


def main():
    while True:
        start_up()

        board = [str(i) for i in range(1, 10)]
        current_player = "X"

        while True:
            print_board(board)

            try:
                choice = input(
                    f"Player {current_player}, choose a position (1-9) or type 'exit': "
                )

                if choice.lower() == "exit":
                    end_up()
                    return

                choice = int(choice)

                if choice < 1 or choice > 9:
                    print("Please enter a number between 1 and 9.")
                    continue

                if board[choice - 1] in ["X", "O"]:
                    print("That position is already taken.")
                    continue

                board[choice - 1] = current_player

                if check_winner(board, current_player):
                    print_board(board)
                    print(f"🎉 Player {current_player} wins!")
                    break

                if is_draw(board):
                    print_board(board)
                    print("🤝 It's a draw!")
                    break

                current_player = "O" if current_player == "X" else "X"

            except ValueError:
                print("Invalid input. Enter a number from 1-9.")

        play_again = input(
            "\nPlay again? (yes/no): "
        ).lower()

        if play_again != "yes":
            break

    end_up()


main()