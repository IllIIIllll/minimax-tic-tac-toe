# © 2020 지성. all rights reserved.
# <llllllllll@kakao.com>
# Apache License 2.0

import enum
from collections import namedtuple

# O, X 선수 구현
class Player(enum.Enum):
    x = 1
    o = 2

    # 한 선수가 돌을 두면 other 메소드를 호출하여 변경
    @property
    def other(self):
        return Player.x if self == Player.o else Player.o

# 좌표
class Point(namedtuple('Point', 'row col')):
    def __deepcopy__(self, memodict={}):
        return self