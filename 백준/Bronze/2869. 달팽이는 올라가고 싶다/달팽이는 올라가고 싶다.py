from math import ceil
A, B, V = map(int, input().split())
day = ceil((V - B) / (A - B))
print(day)