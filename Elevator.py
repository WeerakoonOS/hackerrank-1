n, k = map(int, raw_input().split())
p = map(int, raw_input().split())
p.sort(reverse=True)

t = 0
for i in p[::k]:
    t += 2 * (i-1)

print t
