"""
https://www.acmicpc.net/problem/1092
"""
# 입력
N = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

"""
1. 둘다 내림차순 sort
2. 크레인 리스트를 박스 리스트 순으로 도장 찍듯이 
3. 분기마다 박스를 들 때 최적의 선택을 하도록
"""

# 연산
time = 0

# -1이 출력되는 케이스는 최대중량 박스가 최대적재능력 크레인보다 더 클 때 아닌가
if boxes[0] > cranes[0]:
    print(-1)
    exit()

while len(boxes) > 0:
    # 현재 크레인의 마지막 작업 추적 포인트
    point = 0

    for crane in cranes:
        for i in range(point, len(boxes)):
            box = boxes[i]

            if crane >= box:
                point = i
                boxes.remove(box)
                break

    time += 1

print(time)
