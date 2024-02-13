import sys

stack = []

# 입력 함수
def sys_input():
    return sys.stdin.readline().strip()

# 계산 함수
def dfs(amount):
    stack = [(0, 0)]  # start, sum_amount
    neighbors = [1, 2, 3]
    count = 0
    
    while stack:
        current, sum_amount = stack.pop()
        sum_amount += current 
        
        if sum_amount == amount: 
            count += 1
        
        if sum_amount > amount: 
            continue  # 팝만 된 상태로 스택이 한 칸 비워짐
        
        for neighbor in neighbors:
            stack.append((neighbor, sum_amount)) 
    
    return count

num = int(sys_input())

for _ in range(num):
    amount = int(sys_input())
    print(dfs(amount))