#Find the Manhattan distance from the central port to the closest intersection
import re


def main():
    f = open("input.txt", "r").readlines()
    a = [i.strip() for i in f[0].split(",")]
    b = [i.strip() for i in f[1].split(",")]
    direction_1 = []
    distance_1 = []
    direction_2 = []
    distance_2 = []

    finished = False
    for i in a:
        direction_1.append(re.findall(r'[A-Z]', i))
        numbers = re.findall(r'[0-9]+', i)
        c = list(map(int, numbers))
        for j in c:
            distance_1.append(j)
    for i in b:
        direction_2.append(re.findall(r'[A-Z]', str(i)))
        numbers = re.findall(r'[0-9]+', str(i))
        c = list(map(int, numbers))
        for j in c:
            distance_2.append(j)
    for cmd in a:
        d = cmd[0]
        print(d)
        n = int(cmd[1:])
        print(n)
    interceptions = get_coordinates(distance_1, distance_1, direction_2, distance_2)
    print(interceptions[0], interceptions[1])



def get_coordinates(directions_1, distance_1, directions_2, distance_2):
    interceptions_x = []
    interceptions_y = []
    x = 0
    y = 0
    for index, value in enumerate(directions_1):
        if value == ['U']:
            y += distance_1[index]
        elif value == ['D']:
            y -= distance_1[index]
        elif value == ['R']:
            x += distance_1[index]
        elif value == ['L']:
            x -= distance_1[index]
        x_2 = 0
        y_2 = 0
        for i, v in enumerate(directions_2):
            if v == ['U']:
                y_2 += distance_2[i]
            elif v == ['D']:
                y_2 -= distance_2[i]
            elif v == ['R']:
                x_2 += distance_2[i]
            elif v == ['L']:
                x_2 -= distance_2[i]

            if x_2 == x and y_2 == y:
                interceptions_x.append(x_2)
                interceptions_y.append(y_2)
    print("X ->", interceptions_x, "Y ->", interceptions_y)
    return interceptions_y, interceptions_x


if __name__ == '__main__':
    main()




