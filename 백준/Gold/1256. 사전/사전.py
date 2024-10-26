from math import comb

N, M, K = map(int, input().split())

def solve(N, M, K):
    result = []

    while N > 0 or M > 0:
        # 'a'를 선택했을 때의 경우의 수 계산
        if N > 0:
            # 'a'를 선택했을 때의 조합 수
            # a는 맨 앞에 정해져있으니, 그 뒤로 남은 조합 개수 세리기(그 남은 문자들 개수가 N + M - 1개)
            # 걔중에 남은 a의 개수들 기반 조합 방법 세리면, a로 시작하는 조합 개수 카운팅 가능
            try:
                a_first = comb(N + M - 1, N - 1)
            # K의 범위가 넘어설 떄(comb 함수에서 에러 발생)
            except ValueError:
                return -1
        else:
            a_first = 0

        # a를 선택했을 때의 경우의 수가 K보다 크거나 같으면 a를 선택
        if a_first >= K:
            result.append('a')
            N -= 1  # a 소비
        else:
            # 그렇지 않으면 z 선택
            result.append('z')
            K -= a_first  # K만큼 덜어내서 다음 분기 초기화
            M -= 1  # z 소비

    return ''.join(result)


answer = solve(N, M, K)

print(answer)


# """
# N.t. 문자열 자릿수는 오로지 N + M 내에서
# N.t. 각각의 문자열은 N개, M개를 씀
# N.t. 순열 활용
# N.t. a: "a"의 남은 개수, b: "b"의 남은 개수
# """
#
#
# # permutation
# def perm(a, z, cur, results):
#     if a == 0 and z == 0:
#         results.append(cur)
#         return results
#
#     # "a"가 우선적으로 배치될 수 있도록 a 관련 조건 우선
#     if a > 0:
#         perm(a - 1, z, cur + "a", results)
#
#     # "a"가 남아있든 말든 항상 "a" 관련 처리가 먼저 이뤄지고 그 다음에 "z" 처리
#     if z > 0:
#         perm(a, z - 1, cur + "z", results)
#
#     return results
#
#
# results = perm(N, M, "", [])
#
# if len(results) < K:
#     print(-1)
# else:
#     print(results[K - 1])
