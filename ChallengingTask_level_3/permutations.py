import itertools
print(list(itertools.permutations([1, 2, 3])))

s = input("\nType the numbers separated by coma: ").split(',')
print(list(itertools.permutations(s)))
