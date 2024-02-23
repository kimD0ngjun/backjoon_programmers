import sys
import heapq

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

cases = int(sys_input())
lectures = []

for _ in range(cases):
    start, end = map(int, sys_input().split())
    lectures.append((start, end))

# 시작시간 오름차순 정렬
lectures.sort(key=lambda x: x[0])

count = 0
heap = []

# 가장 일찍 시작하는 강의의 끝나는 시간 먼저 할당
# 가장 일찍 시작하는 강의부터 이어지는 강의들 확인
heapq.heappush(heap, lectures[0][1])

for i in range(1, cases):
    # 탐색된 강의의 시작 시간이 현재 가장 빨리 끝나는 강의보다 더 빨리 시작하면
    # 새로운 강의실이 필요한 것이 된다
    if lectures[i][0] < heap[0]:
        # 그 강의의 끝나는 시간 추가 할당
        heapq.heappush(heap, lectures[i][1])
    # 탐색된 강의의 시작 시간이 현재 가장 빨리 끝나는 강의보다 더 늦게 시작하면
    # 기존 강의실에서 이을 수 있다
    else:
        # 가장 빨리 끝나는 강의를 빼고 해당 강의를 넣어 시간을 잇는다
        heapq.heappop(heap)
        heapq.heappush(heap, lectures[i][1])

# 최종 힙 배열의 길이가 이어지지 않고 별개로 갈라진 강의실 개수
print(len(heap))


