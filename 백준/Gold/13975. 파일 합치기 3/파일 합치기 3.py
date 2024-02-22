import sys
import heapq

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 해당 분기에서 더하지 않은 것들끼리 최대한 작게 더하는 게 핵심?
# 만약 하나가 남아서 그걸 포함시켜야 한다면 걘 그냥 다음 분기로 넘기면 되지 않나?
# 그리디 풀 때는 최소 최대가 우선 기준이라면 힙과 정렬 적극 생각하기

testcases = int(sys_input())
result = []

for _ in range(testcases):
    files_length = int(sys_input())
    files = [int(file) for file in sys_input().split()]

    # 최소힙 할당
    sum_amount = 0
    heapq.heapify(files)

    while len(files) > 1:
        # 현재 시점에서의 최소값 2개 추출
        min_file = heapq.heappop(files)
        next_file = heapq.heappop(files)

        sum_amount += min_file + next_file

        # 2개가 빠지고 새로운 값 하나가 추가된 것이 힙 배열에 업데이트됨
        heapq.heappush(files, min_file + next_file)

    result.append(sum_amount)

for item in result:
    print(item)