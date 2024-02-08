# 양방향 연결 리스트 문제가 되는 건가?
# 근데 아무리 봐도 스택인데...?

# 문자열(대문자, 소문자) : 노드 '추가'
# 화살표키를 누른 후 바로 직후의 문자열 : 노드 '중간 삽입'
# 백스페이스키 : 해당 위치의 노드 '중간 삭제'

# 근데 이럴 필요 없이 걍 스택으로 생각하면 편한데...
# 포인터와 한 개의 스택으로는 출력 초과 실패가 뜸

import sys
from collections import deque

def sInput():
    return sys.stdin.readline().strip()

T = int(sInput())

for i in range(T):
    key_log = sInput()
    cursor_left = deque()
    cursor_right = deque()

    for c in key_log:
        if c == '<':
            if cursor_left:
                cursor_right.appendleft(cursor_left.pop())
        elif c == '-':
            if cursor_left:
                cursor_left.pop()
        elif c == '>':
            if cursor_right:
                cursor_left.append(cursor_right.popleft())
        else:
            cursor_left.append(c)

    while cursor_right:
        cursor_left.append(cursor_right.popleft())

    print("".join(cursor_left))