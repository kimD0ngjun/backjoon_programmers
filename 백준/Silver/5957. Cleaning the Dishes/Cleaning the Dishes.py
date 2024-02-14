import sys

wash_stack = []
dry_stack = []
result_stack = []

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 설거지 함수
def wash_dish(order, count):
    if order == 1:
        for _ in range(count):
            washed_dish = wash_stack.pop()
            dry_stack.append(washed_dish)
    
    if order == 2:
        for _ in range(count):
            dried_dish = dry_stack.pop()
            result_stack.append(dried_dish)

# 출력 함수
def print_reverse_list(lst):
    lst.reverse()
    for item in lst:
        print(item)

# 입력 처리
dishes = int(sys_input())

for i in range(dishes, 0, -1):
    wash_stack.append(i)

while len(result_stack) != dishes:
    input_data = sys_input()
    # 세척(1), 건조(2) 명령 / 접시 개수
    order, count = map(int, input_data.split())
    
    wash_dish(order, count)

print_reverse_list(result_stack)
