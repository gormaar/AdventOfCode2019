def main():
    file = open("input.txt", "r")
    intcode = []
    for i in file:
        intcode = list(map(int, i.split(",")))
    intcode_program(intcode)


def intcode_program(intcode):
    instruction_pointer = 1
    print(intcode)
    for i in range(0, len(intcode), instruction_pointer):
        if range(intcode[i]) == 5:
            parameter3 = 1
            parameter2 = intcode[i][1]
            parameter1 = intcode[i][2]
            opcode = intcode[i][4]
            print(parameter3, parameter2, parameter1, opcode)
            if opcode == 1:
                pass
        elif range(intcode[i]) == 4:
            parameter3 = 0
            parameter2 = intcode[i][0]
            parameter1 = intcode[i][1]
            opcode = intcode[i][3]
            print(parameter3, parameter2, parameter1, opcode)




if __name__ == "__main__":
    main()




