import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 입력 처리
tests = int(sys_input())
result = []

# 테스트케이스 단위
for _ in range(tests):
    test = int(sys_input())
    cases = []

    for i in range(test):
        cases.append(sys_input())

    # 각 테스트 케이스를 정렬
    cases.sort()

    prefix = False
    for i in range(test - 1):
        # 인접한 두 케이스끼리만 비교
        # 문자열 사전순으로 정렬되어 있기 때문에 i 요소 길이만큼 슬라이싱해서 i+1 요소와 비교
        if cases[i] == cases[i + 1][:len(cases[i])]:
            prefix = True
            break

    if prefix:
        result.append("NO")
    else:
        result.append("YES")

for item in result:
    print(item)
