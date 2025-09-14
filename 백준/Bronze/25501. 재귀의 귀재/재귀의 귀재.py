T = int(input())

# 문자열, left 인덱스, right 인덱스, 호출 카운트
def recursion(s, l, r, c):
    c += 1
    if l >= r: return 1, c
    elif s[l] != s[r]: return 0, c
    else: return recursion(s, l+1, r-1, c)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))

answers = []

for _ in range(T):
    answers.append(isPalindrome(input()))

for answer in answers:
    print(*answer)