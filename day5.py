
def part1():
    print("PART 1: \n")

    with open('day5input.txt') as f:

        jumps = []

        for line in f:

            jumps.append(int(line))

        jump = int(jumps[0])

        index = 0
        escaped = False

        counter = 0;

        print(len(jumps))

        while not escaped:

            if index < 0 or index > len(jumps)-1:
                break;

            jump = jumps[index]
            jumps[index] += 1
            index += int(jump)


            print(index)

            counter += 1

        print(counter)






def part2():
    print("PART 2:\n")

    with open('day5input.txt') as f:

        jumps = []

        for line in f:

            jumps.append(int(line))

        index = 0
        escaped = False

        counter = 0;

        print(len(jumps))

        while not escaped:

            if index < 0 or index > len(jumps)-1:
                break;

            jump = jumps[index]

            if jump >= 3:
                jumps[index] -= 1
            else:
                jumps[index] += 1

            index += int(jump)

            print(index)

            counter += 1

        print(counter)





part1()
part2()