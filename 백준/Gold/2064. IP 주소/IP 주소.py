N = int(input())
ips = []

for _ in range(N):
    ip = list(map(int, input().split(".")))
    ip_32 = (ip[0] << 24) | (ip[1] << 16) | (ip[2] << 8) | ip[3]
    ips.append(ip_32)

max_ip = max(ips)
min_ip = min(ips)
diff = max_ip ^ min_ip

prefix = 0
for i in range(32):
    if diff & (1 << (31 - i)):
        break
    prefix += 1

mask = (0xffffffff << (32 - prefix)) & 0xffffffff
network = min_ip & mask

print(f"{(network >> 24) & 255}.{(network >> 16) & 255}.{(network >> 8) & 255}.{network & 255}")
print(f"{(mask >> 24) & 255}.{(mask >> 16) & 255}.{(mask >> 8) & 255}.{mask & 255}")