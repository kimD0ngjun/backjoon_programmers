"""
https://www.acmicpc.net/problem/1092
"""
import sys


def sys_input():
    return sys.stdin.readline().rstrip()


# 입력
N = int(input())
cranes = list(map(int, sys_input().split()))
cranes.sort(reverse=True)

M = int(input())
boxes = list(map(int, sys_input().split()))
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
else:
    while boxes:
        # 현재 크레인의 마지막 작업 추적 포인트
        point = 0
    
        for crane in cranes:
            # 나름의 최적화
            if boxes and crane < boxes[-1]:
                continue
    
            for box in boxes:
    
                if crane >= box:
                    boxes.remove(box)
                    break
    
        time += 1
    
    print(time)
