file = open("input.txt").read()
count = 0
horizontal = ""
vertical = 0
image_array = []
layers = int(file)
image_array2 = []
for i in file:
    for j in

for i in file:
    if count != 25:
        horizontal += i
        count += 1
    elif count == 25:
        count = 0
        vertical += 1
    if vertical == 6:
        image_array.append(horizontal)
        vertical = 0
        horizontal = ""
least_zero_layer = ""
least_zeroes = 15
for layer in image_array:
    if layer.count("0") < least_zeroes:
        least_zeroes = layer.count("0")
        print(least_zeroes)
        least_zero_layer = layer
one_digits = 0
two_digits = 0
for i in least_zero_layer:
    if i == "1":
        one_digits += 1
    if i == "2":
        two_digits += 1
print(least_zero_layer)
print(one_digits, two_digits)
print(one_digits*two_digits)
#15 130