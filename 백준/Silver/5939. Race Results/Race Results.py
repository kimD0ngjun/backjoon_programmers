import sys
import copy

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 시간 계산 함수
def time(time_list):
    hours = time_list[0]
    minutes = time_list[1]
    seconds = time_list[2]

    return hours * 3600 + minutes * 60 + seconds


count = int(sys_input())
input = []

# 시간 입력
for i in range(count):
    # 초기 인덱스, 시간 리스트
    input.append([list(map(int, sys_input().split()))])

for i in range(count):
    input[i].append(time(input[i][0]))


result = sorted(input, key=lambda x: x[1])

for i in range(count):
    result_str = " ".join(map(str, result[i][0]))
    print(result_str)
