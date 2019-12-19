from collections import defaultdict

digits = [int(x) for x in open("input.txt").read().strip()]
layers = int(len(digits)/(25*6))
C = defaultdict(lambda:defaultdict(int))
for l in range(layers):
    for i in range(25*6):
        C[l][digits[l*25*6+i]] += 1
best = (10000,0)
for l in range(layers):
    print(l,C[l][0])
    if (C[l][0],l)<=best:
        best = (C[l][0],l)
l=best[1]
print(best,C[l],C[l][0],C[l][1])
print(C[l][1]*C[l][2])
