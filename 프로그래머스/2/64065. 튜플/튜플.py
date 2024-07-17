"""
https://www.acmicpc.net/problem/1300
"""
from collections import Counter

def solution(s):
    # 양쪽의 '{', '}' 두 개 덮인 거 걷어내기
    s = s[2:-2]
    # print(s)

    # 안쪽의 '},{' 기준으로 리스트화
    array_a = s.split('},{')
    # print(array_a)

    # 문자열 요소를 리스트 변환 후, set 집합으로 변환
    array_b = [set(list(map(int, item.split(',')))) for item in array_a]
    # print(array_b)

    # 모든 요소의 합집합 연산
    # union = set()
    # for set_element in array_b:
    #     union = union.union(set_element)
    # print(list(union))

    # 각 요소가 등장한 횟수를 세기
    element_counts = Counter()
    for set_element in array_b:
        element_counts.update(set_element)

    # 가장 많이 등장한 요소 순서대로 리스트에 배치
    sorted_elements = sorted(element_counts.items(), key=lambda x: -x[1])
    result = [element for element, _ in sorted_elements]

    print(result)
    return result

# 
# solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
# solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
# solution("{{20,111},{111}}")
# solution("{{123}}")
# solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")