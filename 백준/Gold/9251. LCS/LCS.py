a = input()
b = input()

# print(a[0])

"""
memo는 len(a) * len(b)의 이중 리스트
memo[i][j] : 
문자열 a의 인덱스 i까지의 부분문자열과 문자열 b의 인덱스 j까지의 부분문자열 비교해서 나온 최대 공통 부분문자열 길이
"""
memo = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        """
        b의 인덱스 j에 위치한 문자가 a의 인덱스 i에 위치한 문자와 같다면, 바로 직전 분기의 메모 값에서 +1
        if a[i] == b[j]: memo[i][j] = memo[i-1][j-1] + 1 
        근데 다르다면, 직전 분기의 메모 값을 그대로 옮겨주면 되고
        직전 분기의 기준이 꼭 a여야 하나? 이중반복문이니 b 기준으로 돌려도 똑같은 결과가 나와야 되는데
        그럼 인덱스 i는? 둘 중에 더 큰 놈을 더 이어붙이며 연속해나가야 최댓값이 나올듯
        else: memo[i][j] = memo[i][j-1] or memo[i-1][j]
        """
        if a[i-1] == b[j-1]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])

print(memo[len(a)][len(b)])