# time 1s, memory 128 MB
T = int(input())

"""
1. line의 "("와 ")"의 개수는 같아야 한다
2. "(())"는 유효하지만, "))(("는 유효하지 않다(이하 IN = "(", OUT = ")")
3. IN이 등장하면 push, OUT이 등장하면 pop
"""

IN = "("
OUT = ")"
answers = []

for _ in range(T):
    line = input()
    stack = []
    result = "YES"

    for e in line:
        try:
            if e == IN:
                stack.append(e)
            elif e == OUT:
                stack.pop()
        except IndexError:
            result = "NO"
            break

    if len(stack) > 0:
        result = "NO"

    answers.append(result)

print(*answers, sep="\n")