import sys

T = int(input())
answers = []

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    """
    i*j 메모이제이션?
    파일을 인덱스로 두고, 그 인덱스 짝꿍 중 서로 인접하는 애들끼리?
    는 안되겠네 합쳐지면서 배열 길이가 짧아지니 인덱스 범위 변화 (폐기)

    memo[i][j]를 i부터 j까지의 구간을 합쳤을 때의 최소 비용(계속 갱신)으로 두는 건가
    대신 i <= j 조건을 유지시켜둬서 테이블의 대각선 윗쪽만 쓰는

    memo[i][j]가 i부터 j까지의 범위에 해당하는 파일들을 양분했을 때,
    그 합이 최소가 되는 양분 기준을 찾아 최소값을 갱신해야 된다는 건데

    memo[i][j] = min(memo[i][k] + memo[k+1][j]) (단, i <= k < j)
    -> 간격 작은 애들부터 미리 최소값 찾아 채우면 더 넓은 간격 채우기 가능할듯
    [][][][][][][][]
    [ [][][][][][] ]
    [ [ [][][][] ] ]
    [ [ [ [][] ] ] ]
    """
    memo = [[[sys.maxsize, 0] for _ in range(K)] for _ in range(K)] # 최소비용, 분할 플래그
    for i in range(K):
        memo[i][i][0] = 0
        memo[i][i][1] = i
    for i in range(K-1):
        memo[i][i+1][0] = files[i] + files[i+1]
        memo[i][i+1][1] = i

    temp = [0] * (K+1) # 구간합
    for i in range(K):
        temp[i+1] = temp[i] + files[i]

    for length in range(2, K): # 간격(2부터 K-1까지)
        # 간격 2 기준으로 02, 13, 24... N-2 N 이런 식이어야 되는디 슬라이싱은 안되나..?
        # 간격 length 기준으로 0 length, 1 length+1, 2 length+2 ... N-length N
        for i in range(K-length):
            j = i + length
            """
            이 부분 더 리팩토링하면 pypy 말고 python으로 통과 가능할 것 같은데....
            지금 간격 탐색을 2부터 K까지 진행하고 있을 때
            간격 2를 전부 탐색해서 최소 간격에 해당하는 인덱스 i,j를 찾았을 것...
            얘를 저장해서 다음 3 분기에 써먹는.. 그런 식으로 줄여갈 수 있으려나
            
            1~7 구간을 본다 했을 때 1~3의 최적 구간이 2, 4~7의 최적 구간이 6으로 분할 플래그가 잡힌다면 
            1~7의 최소비용이 1~3 최소비용 + 4~7 최소비용일때, 분할 플래그는 2와 6 사이에 있을 수밖에 없다?
            """
            # 직전(현재 간격 - 1의 최적 분할 플래그 추출)
            opt_i = memo[i][j-1][1]
            opt_j = memo[i+1][j][1]

            # 구간 단위로 최소 합침 비용 갱신하기
            for k in range(opt_i, opt_j + 1):
                """
                sum()이 시간이 너무 오래 걸리나?
                구간 단위의 합산비용도 미리 메모이제이션해보기
                """
                # memo[i][j][0] = min(memo[i][j][0], memo[i][k][0] + memo[k+1][j][0] + temp[j+1] - temp[i])
                value = memo[i][k][0] + memo[k+1][j][0] + temp[j+1] - temp[i]
                if value < memo[i][j][0]:
                    memo[i][j][0] = value # 최소 합산비용 갱신
                    memo[i][j][1] = k # 분할 플래그 갱신

    answers.append(memo[0][K-1][0])

print(*answers, sep="\n")