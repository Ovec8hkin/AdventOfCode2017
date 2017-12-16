registers = dict()


def part1():
    print("PART 1:\n")

    with open('day8input.txt') as f:

        for line in f:

            register = line.split(" ")[0]
            registers[register] = 0

        print(registers)

    with open('day8input.txt') as f:
        for line in f:
            parts = line.split(" ")

            register_to_update = parts[0]
            operator = parts[1]
            update = int(parts[2])
            condition_register = parts[4]
            condition_operator = parts[5]
            condition_value = int(parts[6])

            if condition_operator == "==":
                if registers[condition_register] == condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == "<":
                if registers[condition_register] < condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == "<=":
                if registers[condition_register] <= condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == ">":
                if registers[condition_register] > condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == ">=":
                if registers[condition_register] >= condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == "!=":
                if registers[condition_register] != condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update

        print(registers)

        print(sorted(registers.values()))

        registers.clear()


def part2():
    print("PART 2:\n")
    with open('day8input.txt') as f:

        for line in f:

            register = line.split(" ")[0]
            registers[register] = 0

        print(registers)


    maxValue = 0
    with open('day8input.txt') as f:
        for line in f:
            parts = line.split(" ")

            register_to_update = parts[0]
            operator = parts[1]
            update = int(parts[2])
            condition_register = parts[4]
            condition_operator = parts[5]
            condition_value = int(parts[6])

            if condition_operator == "==":
                if registers[condition_register] == condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == "<":
                if registers[condition_register] < condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == "<=":
                if registers[condition_register] <= condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == ">":
                if registers[condition_register] > condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == ">=":
                if registers[condition_register] >= condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update
            elif condition_operator == "!=":
                if registers[condition_register] != condition_value:
                    if operator == "inc":
                        registers[register_to_update] += update
                    else:
                        registers[register_to_update] -= update

            if registers[register_to_update] > maxValue:
                maxValue = registers[register_to_update]

        print(maxValue)

part1()
part2()