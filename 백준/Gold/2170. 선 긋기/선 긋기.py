import sys


def sys_input():
    return sys.stdin.readline().strip()

lines = []

N = int(sys_input())

for _ in range(N):
    lines.append(tuple(map(int, sys_input().split())))

"""
각 분기마다 비교했을 때 경우의 수는 2가지
1. 범위가 포함돼서 기존 길이에 합산되냐
2. 범위에서 벗어나 새로운 길이 관리가 필요하냐

1번은 그냥 2개 변수둬서 갱신하면 됨
2번은 흠...
예를 들어 A 영역 잘 계산해나가다가 B 영역이라는 A 영역에 포함되지 않는 경우가 나와서 길이 합산을 했는데, 나중에 다시 A 영역이 나오면 어떡하지

시작순 정렬? 회의실 문제?
"""

lines.sort(key=lambda x: x[0])
cur_start = lines[0][0]
cur_end = lines[0][1]
length = 0

for i in range(1, N):
    start, end = lines[i]

    if start > cur_end:  # 이전 구간과 안 겹침
        length += cur_end - cur_start
        cur_start, cur_end = start, end
    else:  # 겹침 → 끝점만 확장
        cur_end = max(cur_end, end)

# 마지막 남은 걸 안 더하고 있었네...
length += cur_end - cur_start

print(length)

"""
반례: 5가 나와야 하는데 4가 나오네잉
5
1 2
3 4
3 5
3 6
3 7
"""