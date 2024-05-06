from itertools import permutations
frase, iterable = input().split()
for i in sorted(permutations(frase, int(iterable))):
    print(''.join(i))
