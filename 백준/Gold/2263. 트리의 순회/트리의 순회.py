"""
https://www.acmicpc.net/problem/2263
"""
"""
루트를 기준으로 '정점이 아닌' 왼쪽 '묶음'와 오른쪽 '묶음' 형태로 나누기

묶음을 기준으로 다시 재귀적으로 쪼개나간다고 생각하기

프리오더: 전위 순회 (루 -> 왼 -> 오)
인오더: 중위 순회 (왼 -> 루 -> 오)
포스트오더: 후위 순회 (왼 -> 오 -> 루)

ex)
중위 순회 : [1, 2, 3] 
후위 순회 : [1, 3, 2]

중위 순회의 인덱스 0(1)은 무조건 트리의 가장 왼쪽
그 다음 인덱스 1(2)은 인덱스 0(1)의 직계 부모
그 다음 인덱스 2(3)은 인덱스 0(1)의 오른쪽 재귀

후위 순회의 인덱스 0(1) 역시 무조건 트리의 가장 왼쪽
그 다음 인덱스 1(3)은 인덱스 0(1)의 오른쪽 재귀
그 다음 인덱스 2(2)은 인덱스 0(1)의 직계 부모

트리 모양이 바뀌어도(이진 트리라는 틀을 부수지 않는 선에서 루트를 재지정해도) 똑같은 결과가 나오나?

루트로 삼을 수 있는 노드는 어떤 노드인가?

역순으로 가기?
-> 인오더만을 보고 역순으로 그려나가기가 가능?

* 포스트오더(후위순회)의 맨 마지막 인덱스 요소가 곧 전체 트리의 루트 노드?
"""
import sys
sys.setrecursionlimit(1_000_000)


# 트리 노드 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


# 전체 트리의 루트 노드를 기점으로
# 인오더(중위순회)에서 해당 값의 앞 애들은 첫번째 왼쪽, 뒷쪽 애들은 첫번째 오른쪽이 됨
# 그 오른쪽을 다시 후위순회에서 전부 배제시킨 후 나온 마지막 인덱스가 왼쪽의 재귀 루트 노드가 됨
# .....이걸 통해 재귀함수 작성


"""
메모리 초과가 뜨는 이유? -> 재귀적으로 호출하면서 계속 슬라이싱으로 배열 할당
시간 초과가 안 뜨는(사실 잘 모르겠지만) 걸 보면 재귀적으로 파고들면서 트리를 생성하는 건 맞는듯

지금 배열을 따로 변형하는 게 아닌, 그저 쪼개고 쪼개는 거에 불과하니까
이걸 굳이 배열을 할당하지 말고 인덱스와 인덱스를 할당해서 원본에서 가리켜 가져오는 걸로 리팩토링하기..?
"""


# 재귀 시점의 트리의 루트 및 해당 왼쪽 후위 노드 리스트 및, 오른쪽 후위 노드 리스트
# 해당 리스트(재귀 트리)의 루트 노드, 중위 순회의 시작 인덱스와 끝 인덱스, 후위 순회의 시작 인덱스와 끝 인덱스
def recursion(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return None

    # 언제나 후위 순회의 마지막 인덱스 값이 곧 해당 재귀 서브트리의 루트 노드 값
    root_value = post_order[post_end]

    root = Node(root_value)
    root_in_index = in_order_index[root_value]

    # 중위순회 왼쪽 서브트리 인덱스 범위 : in_start  ~  root_in_index - 1
    # -> 크기는 root_index_in - in_start
    # 중위순회 오른쪽 서브트리 인덱스 범위 : root_in_index + 1  ~  in_end

    # 후위순회 왼쪽 서브트리 인덱스 범위 : post_start  ~  post_start + root_in_index - 1 - in_start
    # 후위순회 오른쪽 서브트리 인덱스 범위 : post_start + root_in_index - in_start  ~  post_end - 1

    root.left_child = recursion(
        in_start, root_in_index - 1, post_start, post_start + root_in_index - 1 - in_start
    ) # ok

    root.right_child = recursion(
        root_in_index + 1, in_end, post_start + root_in_index - in_start, post_end - 1
    )

    return root


# 전위 순회 함수
def preorder_traversal(root, result):
    if root:
        # 현재 노드를 방문
        result.append(root.data)
        # 왼쪽 뭉치 전위 순회
        preorder_traversal(root.left_child, result)
        # 오른쪽 뭉치 전위 순회
        preorder_traversal(root.right_child, result)


# 입력 받기
V = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

in_order_index = {}

for i in range(len(in_order)):
    in_order_index[in_order[i]] = i

# root 노드 값을 굳이 할당할 필요 x
tree = recursion(0, len(in_order) - 1, 0, len(post_order) - 1)

result = []

preorder_traversal(tree, result)
print(' '.join(map(str, result)))