def evenGenerator(n):
    i=0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1


n = int(input("Give me unsigned number: "))
values = []

print(evenGenerator(n))

for i in evenGenerator(n):
    values.append(str(i))

print('\nHere are the outcome of generator',",".join(values))
print(['%s' %d for d in evenGenerator(n)])