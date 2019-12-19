
a, b = open("input.txt.txt").read().split("\n")
a, b = [x.split(",") for x in [a, b]]

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}
def get_coordinates(a):
    x = 0
    y = 0
    ans = set()
    for cmd in a:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ['L', 'R', 'U', 'D']
        for _ in range(n):
            x+= DX[d]
            y+= DY[d]
            ans.add((x,y))
        return ans

PA = get_coordinates(a)
PB = get_coordinates(b)
both = PA&PB
ans = min([abs(x)+abs(y) for (x, y) in both])
print(ans)

