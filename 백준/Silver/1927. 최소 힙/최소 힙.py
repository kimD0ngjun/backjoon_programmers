import heapq
import sys

heap=[]

count = int(sys.stdin.readline())

def calculator(number):
    if number == 0:
        if len(heap) == 0:
            print(0)
        if len(heap) > 0:
            value = heapq.heappop(heap)
            print(value)
        
    if number != 0:
        heapq.heappush(heap, number)

for i in range(count):
    input_number = int(sys.stdin.readline())
    calculator(input_number)