import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
pokemons = {"_": 0}
for i in range(1, N + 1):
    pokemons[input()] = i

# print(list(pokemons.keys()))
# print(list(pokemons.values()))
names = list(pokemons.keys())
for _ in range(M):
    line = sys.stdin.readline().rstrip()
    if (line.isdigit()):
        sys.stdout.write(f"{names[int(line)]}\n")
    else:
        sys.stdout.write(f"{pokemons[line]}\n")