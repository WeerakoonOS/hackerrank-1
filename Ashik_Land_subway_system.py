n = input()
m = input()
stations = map(int, raw_input().strip().split())

paths = []
path = raw_input()
while True:
    paths.append(map(int, path.strip().split()))
    try:
        path = raw_input()
    except:
        break

cost = 0
visited_stations = []

for station in stations:
    loc = station
    visited_stations.append(station)
    do_loop = True
    while loc != 0 and do_loop:
        for path in paths:
            if path[1] == loc:
                if path[0] in visited_stations:
                    do_loop = False
                    cost += path[2]
                else:
                    cost += path[2]
                    loc = path[0]
                    visited_stations.append(path[0])

print cost * 2

