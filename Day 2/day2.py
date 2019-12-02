#Restore Intcode program to display value of index 0

def main():
    file = open("input.txt", "r")
    for i in file:
        intcode = list(map(int, i.split(",")))

    intcode_program(intcode, 12, 2)
    part2()


def intcode_program(intcode, input_1, input_2):
    intcode[1] = input_1
    intcode[2] = input_2
    for n in range(0, len(intcode), 4):
        if intcode[n] == 1:
            intcode[intcode[n + 3]] = intcode[intcode[n + 1]] + intcode[intcode[n + 2]]
        elif intcode[n] == 2:
            intcode[intcode[n + 3]] = intcode[intcode[n + 1]] * intcode[intcode[n + 2]]
        elif intcode[n] == 99:
            print(intcode[0])
            return intcode[0]


def part2():
    file = open("input.txt", "r")
    for i in file:
        intcode = list(map(int, i.split(",")))
    for noun in range(0, 99):
        for verb in range(0, 99):
            intcode[1] = noun
            intcode[2] = verb
            if intcode_program(intcode, noun, verb) == 19690720:
                print(100 * noun + verb)
                return 100 * noun + verb
            else:
                intcode = list(map(int, i.split(",")))


if __name__ == '__main__':
    main()
