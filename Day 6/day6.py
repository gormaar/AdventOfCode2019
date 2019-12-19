E = {}
for i in open("input.txt").readlines():
    a,b = i.strip().split(")")
    if a not in E:
        E[a] = []
    E[a].append(b)
print(E, "\n")

def f(x):
    ans = 0
    for y in E.get(x, []):
        ans += f(y)
        ans += 1
    return ans

ans = 0
for x in E:
    ans += f(x)
print(ans)








