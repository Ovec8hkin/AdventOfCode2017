
def part1():

    sum = 0

    with open("day2input.txt") as f:

        for line in f:

            numbers = line.split("\t");

            highest = 0
            smallest = 1000

            for num in numbers:

                if int(num) > highest:
                    highest = int(num)
                elif int(num) < smallest:
                    smallest = int(num)

            diff = highest - smallest

            sum += diff

        print(sum)


def part2():

    sum = 0
    with open("day2input.txt") as f:

        for line in f:

            numbers = line.split("\t");
            found_sum = False;
            for i in range(len(numbers)):

                current = float(numbers[i])

                for j in range(len(numbers)):

                    if float(numbers[j]) == current:
                        continue

                    print(numbers[j])

                    if current % float(numbers[j]) == 0:

                        found_sum = True

                        sum += current/float(numbers[j])

                        break

                if found_sum:
                    break



        print(sum)
