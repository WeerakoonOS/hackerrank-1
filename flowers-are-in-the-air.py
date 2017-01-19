r, c, t = map(int, raw_input().split())

p, b, i = 0, 0, 0

if c > 2 * r:
    n = (c-2*r)//2
    p += n
    c -= 2*n
    t -= n
elif c < 2 * r:
    n = r-c//2
    b += n
    r -= n
    t -= 2*n

if r > t or c > 2*r or r < 0:
    print "Sorry Sameera"
    exit()
elif t > r:
    n = (t-r)//2
    p += n
    b += n
    r -= n
    c -= 2*n
    t -= 3*n

if r != t:
    print "Sorry Sameera"
    exit()
else:
    if i % 6 != 0:
        print "Sorry Sameera"
        exit()
    else:
        i = r//6
        print p, b, i
