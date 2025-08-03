import sys


def sys_input():
    return sys.stdin.readline().strip()

results = []

while True:
    line = sys_input()

    if line == "0":
        break

    histogram = list(enumerate(map(int, line.split()[1:])))

    stack = []
    max_area = 0

    for el in histogram:
        idx, height = el

        if stack and stack[-1][1] > height:
            while stack and stack[-1][1] > height:
                pop_idx, pop_height = stack.pop()

                if stack:
                    width = idx - (stack[-1][0] + 1)
                else:
                    width = idx

                if width * pop_height > max_area:
                    max_area = width * pop_height

        stack.append(el)

    if stack:
        last_idx, last_height = stack.pop()

        max_area = last_height if last_height > max_area else max_area

        while stack:
            last_pop_idx, last_pop_height = stack.pop()

            if stack:
                last_width = last_idx - stack[-1][0]
            else:
                last_width = last_idx + 1

            if last_width * last_pop_height > max_area:
                max_area = last_width * last_pop_height

    results.append(max_area)

print(*results, sep="\n")