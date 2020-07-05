# © 2020 지성. all rights reserved.
# <llllllllll@kakao.com>
# Apache License 2.0

import enum
import random
from ttt.agent import Agent

# 게임 결과
class GameResult(enum.Enum):
    lose = 1
    draw = 2
    win = 3

# 상대방 입장에서의 결과 반전
def reverse_game_result(game_result):
    if game_result == GameResult.lose:
        return game_result.win
    if game_result == GameResult.win:
        return game_result.lose
    return GameResult.draw

# Minimax 탐색
def best_result(game_state):
    # 게임 결과 확인
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return GameResult.win
        elif game_state.winner() is None:
            return GameResult.draw
        else:
            return GameResult.lose

    # Minimax 탐색
    best_result_so_far = GameResult.lose
    for candidate_move in game_state.legal_moves():
        # 다음 수에 대한 게임 결과 확인
        next_state = game_state.apply_move(candidate_move)
        # 상대방의 최선의 수
        opponent_best_result = best_result(next_state)
        our_result = reverse_game_result(opponent_best_result)
        # 현재 결과가 지금까지의 최선의 수보다 나은지 확인
        if our_result.value > best_result_so_far.value:
            best_result_so_far = our_result
    return best_result_so_far

# Minimax를 이용한 에이전트
class MinimaxAgent(Agent):
    def select_move(self, game_state):
        winning_moves = []
        draw_moves = []
        losing_moves = []
        # 모든 경우의 수 탐색
        for possible_move in game_state.legal_moves():
            # 다음 수에 대한 게임 결과 확인
            next_state = game_state.apply_move(possible_move)
            # 상대의 다음 수에 대한 게임 결과 확인
            opponent_best_outcome = best_result(next_state)
            our_best_outcome = reverse_game_result(opponent_best_outcome)
            # 결과에 따라 다음 수를 분류
            if our_best_outcome == GameResult.win:
                winning_moves.append(possible_move)
            elif our_best_outcome == GameResult.draw:
                draw_moves.append(possible_move)
            else:
                losing_moves.append(possible_move)
        # 결과가 가장 좋은 다음 수 선택
        if winning_moves:
            return random.choice(winning_moves)
        if draw_moves:
            return random.choice(draw_moves)
        return random.choice(losing_moves)