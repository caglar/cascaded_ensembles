def circle_around(x, y):
    r = 1
    i, j = x-1, y-1

    while True:
        while i < x+r:
            i += 1
            yield r, (i, j)

        while j < y+r:
            j += 1
            yield r, (i, j)

        while i > x-r:
            i -= 1
            yield r, (i, j)

        while j > y-r:
            j -= 1
            yield r, (i, j)

        r += 1
        j -= 1
        yield r, (i, j)

car = circle_around(5, 5)

for loc in car:
    if loc[0] == 10:
        break
    if loc[1][0] >=0 and loc[1][0] <= 13 and loc[1][1] <= 13 and loc[1][1] >= 0:
        print loc

