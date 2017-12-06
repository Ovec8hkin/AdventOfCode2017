import numpy

def part1():
    print("PART 1:\n")

    configurations = []

    #input_string = "5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6"

    input = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]

    while input not in configurations:

        configurations.append(list(input))
        high_index = input.index(max(input))
        #print(high_index)
        value = input[high_index]
        input[high_index] = 0

        for i in range(1, value+1):
            #print(i)
            input[(high_index + i) % len(input)] += 1

        #print(input)
        #print(configurations)

    print(len(configurations))




def part2():
    print("PART 2:\n")

    configurations = []

    # input_string = "5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6"

    input = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6]

    while input not in configurations:

        configurations.append(list(input))
        high_index = input.index(max(input))
        # print(high_index)
        value = input[high_index]
        input[high_index] = 0

        for i in range(1, value + 1):
            # print(i)
            input[(high_index + i) % len(input)] += 1

            # print(input)
            # print(configurations)

    previous = configurations.index(input)
    print(len(configurations) - previous)


part1()
part2()