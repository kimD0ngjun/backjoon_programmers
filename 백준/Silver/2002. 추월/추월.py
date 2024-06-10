"""
https://www.acmicpc.net/problem/2002
"""
from collections import deque

N = int(input())

# 들어간 차
enter_queue = deque()

for i in range(N):
    enter_queue.append(input())

# 나온 차
exit_queue = deque()

for i in range(N):
    exit_queue.append(input())


"""
연산 과정
"""
answer = 0

while exit_queue:
    exited_car = exit_queue.popleft()

    # 엔터 큐의 최전 인덱스 요소는 모든 제거과정을 거친 후의 값
    # 그러므로 정리가 끝난 exit queue와 비교했을 때 다른 값이라면
    # 다른 값에 의해 추월당했다는 의미
    if enter_queue[0] != exited_car:
        answer += 1
        # 이미 추월한 차는 더 이상 볼일 없으니 정리
        enter_queue.remove(exited_car)
    else:
        enter_queue.popleft()

print(answer)




