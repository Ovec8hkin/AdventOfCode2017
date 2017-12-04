def part1():

    with open('day4input.txt') as f:

        goodlines = 0

        for line in f:

            passed = True

            line = line.rstrip()
            words = line.split(" ")

            words_dict = {}

            for word in words:

                if ''.join(sorted(word)) in words_dict:
                    passed = False
                    break
                else:
                    words_dict[''.join(sorted(word))] = 1

            if passed:
                goodlines += 1

        print(goodlines)


def part2():
    print("Part 2")



part1()