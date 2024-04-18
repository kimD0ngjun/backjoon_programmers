from collections import deque

# 큐 생성
def create_queue(size):
    queue = deque()
    for i in range(1, size + 1):
        queue.append(i)
    return queue

# 큐 회전 함수 생성
def rotate(queue, count):
    for _ in range(count - 1):
        temp = queue.popleft()
        queue.append(temp)
    return queue

# 초기값 세팅
values = []

# 입력 단계
size, position = map(int, input().split())

# 큐 생성
queue = create_queue(size)

# 회전초밥
# 큐가 비워질 때까지 회전해서 선택한다
while queue:
    queue = rotate(queue, position)
    values.append(queue.popleft()) # 뽑히는 순서대로 리스트에 담아두기

# 정답 세팅 및 출력
result = "<" + ", ".join(map(str, values)) + ">"
print(result)
