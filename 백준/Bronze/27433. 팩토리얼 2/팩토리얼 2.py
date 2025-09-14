N = int(input())

def fac(n):
    if n == 1 or n == 0:
        return 1

    return fac(n-1) * n

print(fac(N))