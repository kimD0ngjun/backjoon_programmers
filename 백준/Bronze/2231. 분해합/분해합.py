N = int(input())

num = 1

# while문 대신 for문으로 범위 지정시키기
for num in range(1, N + 1):
    digits = sum((map(int, str(num))))

    if num + digits == N:
        print(num)
        break

    if num == N:
        print(0)