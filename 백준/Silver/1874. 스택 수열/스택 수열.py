import sys

def solve(lines):
    lines = lines.strip().split("\n")
    n = int(lines[0])

    stack = []
    top = 0
    index = 1
    result = ""

    while index <= n:
        value = int(lines[index])

        if value > top:
            for i in range(top, value):
                stack.append(i + 1)
                result += "+\n"
            top = value
        elif stack[-1] != value:
            print("NO")
            return

        stack.pop()
        result += "-\n"
        index += 1

    print(result)

input_lines = sys.stdin.readlines()
input_text = "".join(input_lines)
solve(input_text)
