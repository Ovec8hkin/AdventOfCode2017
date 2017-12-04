import math
import networkx as nx

def findIndex(number, known_br_i, known_br_j, br_value):

    difference = number - br_value

    i = known_br_i
    j = known_br_j

    counter = 0
    while counter < difference:
        if i > 0:
            i -= 1
        elif j > 0:
            j -= 1

        counter += 1

    return i, j





def part1():
    print("PART 1: \n\n")

    i = 513
    j = i+1

    indexes = (514, 432)

    print(indexes)

    i_of_1 = math.floor(514/2.0)
    j_of_1 = math.floor(514/2.0)

    print(i_of_1)
    print(j_of_1)

    number_of_steps = (math.fabs(indexes[0] - i_of_1))+(math.fabs(indexes[1] - j_of_1))

    print(number_of_steps)







def part2():
    print("Part 2: \n\n")


part1()
print("\n")
part2()