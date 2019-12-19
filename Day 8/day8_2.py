numbers = [int(x) for x in open("input.txt").read()]
layer_list = []
size = int(len(numbers)/(25*6))
for i in range(size):
    for j in range(25*6):
        layer_list.append(j)
print(layer_list)

