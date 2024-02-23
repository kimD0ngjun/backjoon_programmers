import sys


# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()


result = []
cases = int(sys_input())

for _ in range(cases):
    people = int(sys_input())
    test = []

    for _ in range(people):
        a, b = map(int, sys_input().split())
        test.append((a, b))

    test.sort(key=lambda x: x[0])

    # 정렬 기준인 1차에서 1등인 사람의 다른 시험(2차) 순위 내에 들어야 그 사람도 통과함
    cut_line = test[0][1]
    count = 1

    for i in range(people):
        if cut_line > test[i][1]:
            count += 1
            cut_line = test[i][1]

    result.append(count)

for item in result:
    print(item)