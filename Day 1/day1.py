#Calculate how much fuel is required to launch all the modules

from math import floor


def day1():
    file = open("input.txt", "r")
    modules = file.readlines()
    fuel_required = 0
    fuel_for_fuel = 0

    for mass in modules:
        fuel = floor(int(mass) / 3) - 2
        fuel_required += fuel
        while floor(fuel / 3) - 2 > 0:
            new_fuel = floor(fuel / 3) - 2
            fuel = new_fuel
            fuel_for_fuel += new_fuel
    file.close()
    print("Fuel requirements", fuel_required)
    print("Fuel for fuel", fuel_for_fuel + fuel_required)


if __name__ == '__main__':
    day1()





