import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 재귀 커스터마이징 재도전
def binary_search(lines, need, minimum, maximum):
    """음... 얘가 문제는 아니네"""
    # # 혹시 모를 예외처리
    # if minimum + maximum == 0:
    #     return 0

    if minimum > maximum:
        return maximum

    cut = (maximum + minimum) // 2
    total_sum = 0

    for line in lines:
        if cut <= line: # cut단위가 line을 넘어서면 안 되니깐(근데 이러면 또 0 나누기 에러 발생)
            total_sum += line // cut

    if total_sum >= need:
        return binary_search(lines, need, cut + 1, maximum)
    else:
        return binary_search(lines, need, minimum, cut - 1)


count, need = map(int, sys_input().split())
lines = []
for _ in range(count):
    lines.append(int(sys_input()))

lines.sort()
maximum = max(lines)
minimum = 1 # 랜선 길이가 0일 수는 없다...!

print(binary_search(lines, need, minimum, maximum))