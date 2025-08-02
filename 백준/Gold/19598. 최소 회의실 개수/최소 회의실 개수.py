import heapq
import sys


def sys_input():
    return sys.stdin.readline().strip()

start_list = []
queue = []

N = int(sys_input())

for _ in range(N):
    start_list.append(tuple(map(int, sys_input().split())))

start_list.sort(key=lambda x: x[0])

"""
일일이 비교하면 시간복잡도 n^2
만약
(0, 40), (15, 30), (5, 10), (10, 15) 이렇게 주어지고 비교한다 가정할 때,
분기 중에 (15, 30)과 (10, 15)을 비교한다면 얘넨 하나의 회의실에서도 처리 가능하니까
이걸 합쳐서 (10, 30)으로 만들기?

1. 다만 이러면 시작시간 기준 정렬이 필요함
(0, 40), (5, 10), (10, 15), (15, 30) -> 시작시간 기준 정렬

2. 문제점: (5, 10)과 (15, 30)이 하나의 회의실에서 이뤄지는 게 가능하므로 
(5, 30)으로 만들면 이후에 (5, 30)이랑 (10, 15)는 별개의 회의실이라는 오류가 발생
-> 이걸 위해 끝 시간의 비교가 추가로 필요해짐
-> 끝 시간과 기준이 되는 회의의 시작 시간의 비교?

이 상태에서 이제 종료 시간을 고려한 추가 정렬을 해야 한다
힙트리?
종료 시간을 기준으로 정렬하는 최소 힙을 할당해서 시작시간 기준 정렬 리스트를 순회하며 넣는다.

이때, 힙의 역할은 최선 종료시간을 계속 갖고와서 비교케 한다 만약 최선 종료시간보다 뒤쳐지는 시작시간을 가진 회의가 발견됐다면, 
그건 새로운 회의실 할당이 필요없다는 것이므로 pop도 같이 겸한다. 어찌됐든 최선 종료시간은 우선순위 큐 내부의 힙트리에 의해 유지된다.
(이 관점이 그리디 관점 같기도?)

어떤 분기든 간에 힙에 있는 놈들은 그 분기까지의 '겹치는' 회의들만 모여있는 셈
"""

for conference in start_list:
    start, end = conference

    if queue and queue[0][0] <= start:
        heapq.heappop(queue)

    heapq.heappush(queue, (end, start))

print(len(queue))