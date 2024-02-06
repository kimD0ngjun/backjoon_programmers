from collections import deque
import sys

count = int(input())

for i in range(count):
    testcase = input()
    amounts, target = map(int, testcase.split())

    serial = sys.stdin.readline()
    queue = deque(list(map(int, serial.split())))

    sequence = 0  # 순서
    
    # 반복문 구간
    while queue:
        importance = max(queue)  # 중요도
        
        check = queue.popleft()
        target -= 1
        
        if check == importance:
            sequence += 1
            # 찾던 값이 추출된 경우
            if target == -1: 
                # 찾는 값이 나오면 반복문 파괴
                print(sequence)
                break
        else:
            queue.append(check)
            # 찾던 값이 추출된 경우
            if target == -1:
                target = len(queue) - 1

    
