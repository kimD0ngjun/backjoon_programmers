N = int(input())
answers = []

for _ in range(N):
    a, b = map(int, input().split())
    answers.append(a + b)

print(*answers, sep='\n')