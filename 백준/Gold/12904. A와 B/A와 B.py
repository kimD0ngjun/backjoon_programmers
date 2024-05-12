"""
문자열의 뒤에 A를 추가한다.
문자열을 뒤집고 뒤에 B를 추가한다.
"""

# 반대로 간다면

"""
A를 제거한다.
B를 제거하고 문자열을 뒤집는다.
"""

S = input()
T = input()

for i in range(len(S), len(T)):
    if T[-1] == "A":
        T = T[:-1]
    elif T[-1] == "B":
        T = T[:-1]
        T = T[::-1]

# print(S)
# print(T)

if S == T:
    print(1)
else:
    print(0)