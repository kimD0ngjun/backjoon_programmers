import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()


cases = int(sys_input())
meetings = []

for _ in range(cases):
    start, end = map(int, sys_input().split())
    meetings.append((start, end))

# 끝나는 시간 오름차순 정렬
# 가장 짧게 '끝나야' 그만큼 뒤에 더 많이 회의 배치 가능성 업
# 만약 end가 같은 케이스가 2개라면 그제야 시작시간 비교해서 가장 작은 거
meetings.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

# 가장 일찍 끝나는 것을 기점으로 다음 분기에서의 가장 일찍 끝나는 것을 탐색
# start는 상관하지 않는다. 어차피 end가 앞에 있을 수록 start도 앞에 있을 테니
# end가 같은 시점일 때 이제 start를 고려하게 된다
for start, end in meetings:
    if end_time <= start:
        end_time = end
        count += 1

print(count)
