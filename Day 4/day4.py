# Recover the elves' lost password for the fuel station
a = 0
b = 0
for i in range(165432, 707912 + 1):
    each_num = [int(x) for x in str(i)]
    doubles = any([each_num[i] == each_num[i + 1] for i in range(len(each_num) - 1)])
    descending = any([each_num[i] > each_num[i + 1] for i in range(len(each_num)-1)])
    matching_digits = any([(i == 0 or each_num[i] != each_num[i - 1]) and each_num[i] == each_num[i + 1] and (
                i == len(each_num) - 2 or each_num[i] != each_num[i + 2])
                           for i in range(len(each_num) - 1)])
    if doubles and not descending:
        a += 1
    if matching_digits and not descending:
        b += 1
print("Part 1 ->", a)
print("Part 2 ->", b)
