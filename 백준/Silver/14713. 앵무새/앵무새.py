"""
각 문장들을 큐로써 담아버린다
쓴 문장을 요소 단위로 탐색해서 큐의 입구에 존재하는지 확인한다
없으면 Impossible
"""
from collections import deque

count = int(input())

# queue 모으는 리스트
queue_list = []

for _ in range(count):
    queue_list.append(deque(input().split()))

paragraph = deque(input().split())
result = "Possible"

for word in paragraph:
    popped = False

    # 큐를 순회했을 때 같은 것이 나오는가?
    for queue in queue_list:

        if len(queue) != 0 and queue[0] == word:
            queue.popleft() # 해당 큐 문장 단어 제거
            popped = True
            # print("확인:" + str(paragraph))
            break

    # 같은 것이 없다면 작성 못하는 문장
    # 브레이크
    if not popped:
        result = "Impossible"
        break

# 앵무새 문장들 길이 0인지(전부 소진됐는지) 확인
for queue in queue_list:
    if len(queue) != 0:
        result = "Impossible"
        break


print(result)

