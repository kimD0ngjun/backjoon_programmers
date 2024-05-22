import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    is_deleted = [False] * len(operations)
    
    for i in range(len(operations)):
        value = operations[i]
        
        # 삽입
        if value[:1] == "I":
            int_value = int(value[2:])
            heapq.heappush(min_heap, (int_value, i))
            heapq.heappush(max_heap, (-int_value, i))
        
        # 삭제
        elif value[:1] == "D":
            if value[2:] == "1":
                if len(max_heap) > 0:
                    is_deleted[heapq.heappop(max_heap)[1]] = True
            elif value[2:] == "-1":
                if len(min_heap) > 0:
                    is_deleted[heapq.heappop(min_heap)[1]] = True

        # 삭제 동기화
        while len(max_heap) > 0 and is_deleted[max_heap[0][1]] == True:
            heapq.heappop(max_heap)

        while len(min_heap) > 0 and is_deleted[min_heap[0][1]] == True:
            heapq.heappop(min_heap)
    
    if len(min_heap) == 0:
        return [0, 0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]
