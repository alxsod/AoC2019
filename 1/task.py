## non-recursive solution
file_contents = open('input.txt', 'r')
string_contents = file_contents.readlines()


def get_fuel(fuel, bool):
    fuel_by_fuel = 0
    fuel_override = fuel
    if(bool==False):
        return int(fuel/3) - 2
    while(fuel_override >= 0 and bool==True):
        fuel_override = int(fuel_override/3) - 2
        if(fuel_override <= 0):
            break
        else:
            fuel_by_fuel += fuel_override
    return fuel_by_fuel

def get_full_fuel(bool):
    fuel_sum = 0
    for line in string_contents:
        parsed_line = line.replace("\n", "")
        temp = int(parsed_line)
        fuel_sum += get_fuel(temp,bool)
    return fuel_sum

##Answer1
print("Answer 1: " + str(get_full_fuel(False)))

##Answer2
print("Answer 2: " + str(get_full_fuel(True)))
