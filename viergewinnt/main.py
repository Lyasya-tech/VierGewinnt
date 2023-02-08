import random

from viergewinnt.board import Board
from viergewinnt.player import Player
from viergewinnt.player import PCPlayer
from viergewinnt.player import AI
import time

if __name__ == '__main__':

    board = Board(6, 7)

    print('Hello! We are glad you want to play!' + '\n' + 'How do you want to play - with another meatbag or a great '
                                                          'and powerful random AI?')

    print("1. Two player game")
    print("2. Play against computer")
    print("3. Play against powerful AI brains")

    choice = int(input("Enter 1, 2 or 3: "))
    if choice == 1:
        print("Starting two player game.")

        p1 = Player(input('Choose the piece you want to use: X or O? '))
        p2 = Player(Player.opponent(p1))
        print(f'Player 1 is {p1.piece}{chr(10)}Player 2 is {p2.piece}')

        print(board)
        turn = random.randint(0, 1)
        game_over = False

        while not game_over and not board.is_full():
            if turn == 0:
                print('Player 1 it is your move')
                board.place_piece(p1.move(board), p1.piece)
                print(board)
                if board.win(p1.piece):
                    print('Player 1 wins! Congrats!')
                    game_over = True
            else:
                print('Player 2 it is your move')
                board.place_piece(p2.move(board), p2.piece)
                print(board)
                if board.win(p2.piece):
                    print('Player 2 wins! Congrats!')
                    game_over = True

            turn += 1
            turn = turn % 2

    elif choice == 2:
        print("Starting game against computer.")

        p1 = Player(input('Choose the piece you want to use: X or O? '))
        p2 = PCPlayer(Player.opponent(p1))
        print(f'Player 1 is {p1.piece}{chr(10)}Player 2 is {p2.piece}')

        print(board)
        turn = random.randint(0, 1)
        game_over = False

        while not game_over and not board.is_full():
            if turn == 0:
                print('Player 1 it is your move')
                board.place_piece(p1.move(board), p1.piece)
                print(board)
                if board.win(p1.piece):
                    print('Player 1 wins! Congrats!')
                    game_over = True
            else:
                time.sleep(1)
                print("it's Player 2 turn")
                board.place_piece(p2.move(board), p2.piece)
                print(board)
                if board.win(p2.piece):
                    print('Player 2 wins! Inevitable!')
                    game_over = True

            turn += 1
            turn = turn % 2

    elif choice == 3:
        print("Starting game against AI")

        p1 = Player(input('Choose the piece you want to use: X or O? '))
        p2 = AI(Player.opponent(p1))
        print(f'Player 1 is {p1.piece}{chr(10)}Player 2 is {p2.piece}')

        print(board)
        turn = random.randint(0, 1)
        game_over = False

        while not game_over and not board.is_full():
            if turn == 0:
                print('Player 1 it is your move')
                board.place_piece(p1.move(board), p1.piece)
                print(board)
                if board.win(p1.piece):
                    print('Player 1 wins! Congrats!')
                    game_over = True
            else:
                time.sleep(1)
                print("it's Player 2 turn")
                board.place_piece(p2.move(board), p2.piece)
                print(board)
                if board.win(p2.piece):
                    print('Player 2 wins! Inevitable!')
                    game_over = True

            turn += 1
            turn = turn % 2


    else:
        print("Invalid choice, please try again.")

    if board.is_full():
        print("It's a tie!")