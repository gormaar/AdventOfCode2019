f = open("input.txt").read()


def part1():
    ans = 0
    for i, v in enumerate(f):
        try:
            if v == f[i+1]:
                ans += int(v)
        except IndexError:
            pass
    if f[0] == f[-1]:
        ans += int(f[0])
    print("Part 1 ->", ans)


def part2():
    ans = 0
    for i, v in enumerate(f):
        steps = len(f)/2
        try:
            if v == f[i+int(steps)]:
                ans += int(v)
        except IndexError:
            pass
    if f[0] == f[-1]:
        ans += int(f[0])
    print("Part 2 ->", ans)

part1()
part2()