import zlib
import time

s = 'hello world!hello world!hello world!hello world!'
t = zlib.compress(s.encode("utf-8"))
#r = zlib.compress(s.encode("utf-16"))
print(t)
#print(r)

print(zlib.decompress(t))
#print(zlib.decompress(r))

from timeit import Timer
#Class for timing execution speed of small code snippets.
u = Timer("for i in range(200):1+1")
print(u.timeit())


# start = time.time()
# for i in range(200):
#     1 + 1
# end = time.time()
# print(end - start)

#help(Timer)
