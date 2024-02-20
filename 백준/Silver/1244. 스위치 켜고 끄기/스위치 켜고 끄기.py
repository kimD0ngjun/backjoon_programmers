import sys

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 스위치 조작 함수
def turn(gender, switch, switches):
    # male
    if gender == 1:
        for i in range(switch - 1, length, switch):
            switches[i] = not switches[i]

    # female
    if gender == 2:
        center = switch - 1
        switches[center] = not switches[center]

        # 투 포인터 알고리즘
        left = center
        right = center

        while True:
            left -= 1
            right += 1

            if left < 0 or right >= len(switches):
                break

            if switches[left] == switches[right]:
                switches[left] = not switches[left]
                switches[right] = not switches[right]
            else:
                break

    return switches

"""
입력 처리
"""

length = int(sys_input())
switches = [bool(int(x)) for x in sys_input().split()]

students = int(sys_input())

for _ in range(students):
    gender, switch = tuple(map(int, sys_input().split()))
    switches = turn(gender, switch, switches)

update_switch = [str(int(x)) for x in switches]

result = ""

for i in range(len(update_switch)):
    result += update_switch[i] + " "

    if (i + 1) % 20 == 0:
        result += "\n"

print(result)