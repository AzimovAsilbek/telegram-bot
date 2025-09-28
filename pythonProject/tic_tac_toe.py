def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # Gorizontal va vertikal tekshirish
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    # Diagonal tekshirish
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def tic_tac_toe():
    # Bo'sh doska
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    for turn in range(9):  # Maksimal 9 yurish bo'lishi mumkin
        print_board(board)
        print(f"Navbat: {current_player}")
        try:
            row, col = map(int, input("Qator va ustunni kiriting (0-2, masalan: 0 1): ").split())
            if board[row][col] == " ":
                board[row][col] = current_player
                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Yutdi: {current_player}!")
                    return
                current_player = "O" if current_player == "X" else "X"  # Navbatni o'zgartirish
            else:
                print("Bu joy band! Qaytadan urinib ko'ring.")
        except (ValueError, IndexError):
            print("Noto'g'ri kiritish! Qaytadan urinib ko'ring.")

    print_board(board)
    print("Durrang!")


# O'yinni boshlash
tic_tac_toe()
