import sys

order = {}

numbers = input()
count = int(numbers.split()[0])
find_count = int(numbers.split()[1])

for i in range(count):
    serial = sys.stdin.readline()
    url, pwd = serial.split()
    
    order[url] = pwd

for i in range(find_count):
    url = input()
    print(order.get(url))