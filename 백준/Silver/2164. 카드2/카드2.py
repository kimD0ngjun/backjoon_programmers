# 파이썬에서 queue 문제 풀 때는 deque를 기본으로 쓴다고 생각하기
from collections import deque

size = int(input())
queue = deque(range(1, size + 1))

while len(queue) > 1:
    poll_number = queue.popleft()
    back_number = queue.popleft()
    queue.append(back_number)

print(queue.pop())
