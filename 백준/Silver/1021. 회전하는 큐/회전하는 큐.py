from collections import deque

# 큐 생성
def create_queue(size):
    queue = deque()
    for i in range(1, size + 1):
        queue.append(i)
    return queue

# 2번 연산
def second(queue, count):
    for _ in range(count):
        temp = queue.popleft()
        queue.append(temp)
    return queue

# 3번 연산
def third(queue, count):
    for _ in range(count):
        temp = queue.pop()
        queue.appendleft(temp)
    return queue

# 초기값 세팅
result = 0

# 입력 단계
size, counts = map(int, input().split())
input_str = input()
value_list = [int(x) for x in input_str.split()]

queue = create_queue(size)

for value in value_list:
    # 큐에서 값 인덱스 추출
    index = queue.index(value)

    # 만약 인덱스가 길이 평균 내림 이하면 정방향 회전
    if index < len(queue) // 2:
        queue = second(queue, index)
        result += index # 인덱스가 곧 연산 횟수

    # 만약 인덱스가 길이 평균 내림 넘기면 역방향 계산
    else:
        queue = third(queue, len(queue) - index)
        result += min(len(queue) - index, index)  # 왼쪽 이동과 오른쪽 이동 중 작은 값을 선택

    # 큐에서 해당 값 제거
    queue.popleft()

print(result)
