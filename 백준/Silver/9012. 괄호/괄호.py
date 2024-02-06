sequence = int(input())
answer = []

for i in range(sequence):
    ps = input()
    stack = []

    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                stack.append(p) # 오답 체킹용 임의 푸시
                break

    result = "NO" if stack else "YES"
    answer.append(result)
    
print("\n".join(answer))