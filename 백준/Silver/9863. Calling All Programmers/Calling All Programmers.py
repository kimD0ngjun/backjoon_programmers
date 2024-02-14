import sys
from queue import deque

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 큐 함수
def queue_chooser(callers, skip_num, count):
    queue = deque()
    answer = []

    # caller ready
    for i in range(1, callers + 1):
        queue.append(i)
    
    # popleft and repeat
    for _ in range(count):
        for i in range(skip_num):
            popped = queue.popleft()
            if i == skip_num - 1:
                winner = popped
            else:
                queue.append(popped)

    answer.append(winner)
    return answer

# 입력 처리
answers = []
while True:
    input_data = sys_input()
    # 큐의 초기 길이(n), popleft 횟수(m), 총 popleft 횟수(k)
    callers, skip_num, count = map(int, input_data.split())
    
    if callers == 0 and skip_num == 0 and count == 0:
        break
    
    answers.extend(queue_chooser(callers, skip_num, count))

# 정답 출력
for item in answers:
    print(item)
