import sys
import heapq

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 짧은 시간이 앞에 오도록

length = int(sys_input())

times = [int(time) for time in sys_input().split()]
times.sort()

sum_list = []

for i in range(length):
    sum_list.append(sum(times[:i+1]))

print(sum(sum_list))