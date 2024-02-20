import sys
from collections import deque

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

"""
입력 처리
"""
def answer():
    half_conveyor, limit = map(int, sys_input().split())

    # 요소 : 내구도, 로봇이 밟고 있는지 여부
    belts = [[int(x), False] for x in sys_input().split()]

    queue = deque(belts)

    """
    큐를 썼지만 착오 방지를 위해서
    appendleft와 pop을 사용할 것
    """

    zero_dur_count = 0 # 총 내구도 개수
    count = 0 # 분기당 내구도 개수
    level = 0 # 분기

    while zero_dur_count < limit:
        level += 1
        """rotate"""
        rotation = queue.pop()
        queue.appendleft(rotation)
        queue[len(queue) // 2 - 1][1] = False

        ## 우선 마지막 바로 앞 인덱스까지 걷기 처리
        for i in range(len(queue)//2 - 2, -1, -1):
            if queue[i][1] == True and queue[i + 1][1] == False and queue[i + 1][0] > 0:
                queue[i][1] = False
                queue[i+1][1] = True
                
                queue[i+1][0] -= 1
                if i + 1 == len(queue)//2 - 1:
                    queue[len(queue) // 2 - 1][1] = False

        ## 올리는 위치 포지션 인 처리
        if queue[0][1] == False and queue[0][0] > 0:
            queue[0][1] = True
            queue[0][0] -= 1

        """check durability"""
        for i in range(len(queue)):
            if queue[i][0] <= 0:
                count += 1

        zero_dur_count = count
        count = 0

    print(level)

answer()