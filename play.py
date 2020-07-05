# © 2020 지성. all rights reserved.
# <llllllllll@kakao.com>
# Apache License 2.0

from ttt import minimax
from ttt import board, types

COL_NAMES = 'ABC'

def print_board(board):
    print('   A   B   C')
    for row in (1, 2, 3):
        pieces = []
        for col in (1, 2, 3):
            piece = board.get(types.Point(row, col))
            if piece == types.Player.x:
                pieces.append('X')
            elif piece == types.Player.o:
                pieces.append('O')
            else:
                pieces.append(' ')
        print(f'{row}  {" | ".join(pieces)}')

def point_from_coords(text):
    col_name = text[0]
    row = int(text[1])
    return types.Point(row, COL_NAMES.index(col_name) + 1)

def main():
    game = board.GameState.new_game()

    human_player = types.Player.x
    bot =minimax.MinimaxAgent()

    while not game.is_over():
        try:
            print_board(game.board)
            if game.next_player == human_player:
                human_move = input('착수 : ').upper()
                point = point_from_coords(human_move.strip())
                move = board.Move(point)
            else:
                move = bot.select_move(game)
            game = game.apply_move(move)
        except ValueError:
            print('정확한 좌표를 입력하세요.')
        except IndexError:
            print('정확한 좌표를 입력하세요.')
        except AssertionError:
            print('이미 돌이 존재합니다.')

    print_board(game.board)
    winner = game.winner()
    if winner is None:
        print('무승부!')
    else:
        print(f'{str(winner)}의 승리!')

if __name__ == '__main__':
    main()