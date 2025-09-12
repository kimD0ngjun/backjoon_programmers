# https://www.acmicpc.net/problem/11003
import heapq
import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))

"""
L = 3, 0 이하인 i는 무시
D_1 = A_(2-L) ~ A_2 -> -1부터 2까지 -> 1부터 2까지
D_2 = A_(3-L) ~ A_3 -> 0부터 1까지 -> 1부터 3까지
D_3 = A_(4-L) ~ A_4 -> 1부터 4까지
D_4 = A_(5-L) ~ A_5 -> 2부터 5까지
...

문제 설명 드릅게 지저분하네
"""

"""
힙은 시간초과 나네
힙 정렬 시간복잡도 n * logn -> 시간 초과
흠
"""
# heap = []
# answers = []
#
# # 값과 인덱스를 튜플로 같이 넣어 추적
# # 반복문의 인덱스는 슬라이드 right 인덱스
# # 얘를 기준으로 왼쪽 인덱스 연산(1이냐 계산값이냐..)
# for i in range(1, N + 1):
#     heapq.heappush(heap, (A[i], i))
#
#     # 힙 안 요소 뺄 것은 앞의 인덱스 기준으로 빼기
#     # 힙 내 최소값이 left 인덱스 범위 벗어나면 팝 처리
#     while heap and heap[0][1] < (i - L + 1):
#         heapq.heappop(heap)
#
#     answers.append(heap[0][0])
#
# print(*answers)

# 그냥 큐? 데크?
# 슬라이드 내에서의 최소값 선택을 위한 정렬 과정을 없앤다
# 힙에 요소를 넣을 때마다 최소연산 수행(nlogn) 그리고 인덱스 범위 벗어나면 팝처리되는 애들이 많음 -> 여기가 시간낭비?
# 힙 내에서 슬라이딩과 최소 연산 분리 방법은... 생각 안나네
queue = deque()
answers = []

# 분기마다 추가돼서 큐 뒤에 덧붙여짐(기존 최소값 vs 새로운 놈)
for i in range(N):
    # 새로 추가하려던 놈이 줄 서려는데, 자기보다 큰 놈이 앞에 있으니 걔네를 뺴버리고
    # 근데 어차피 최소값만 출력하면 되니 걔넨 뺀 김에 버리기
    while queue and A[queue[-1]] > A[i]:
        queue.pop()

    queue.append(i)

    # 인덱스 슬라이딩
    if queue[0] <= i - L:
        queue.popleft()

    answers.append(A[queue[0]])

print(*answers)