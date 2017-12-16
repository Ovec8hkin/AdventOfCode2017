nums = list(range(0, 256))
#nums = [0, 1, 2, 3, 4]
lengths = "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224".split(",")
#lengths = "3,4,1,5".split(",")


def reverse_sublist(the_list, start, length):
    sublist = []

    for i in range(length):
        sublist.append(the_list[(start+i) % len(the_list)])

    sublist.reverse()

    for i in range(length):
        the_list[(start+i) % len(the_list)] = sublist[i]



def part1():
    print("PART 1:\n")
    start_index = 0
    skip_size = 0

    for value in lengths:
        length = int(value)
        reverse_sublist(nums, start_index, length)
        start_index = (start_index+(length+skip_size)) % len(nums)
        skip_size += 1

    print(nums)


def part2():
    print("PART 2:\n")


print(nums)
part1()
part2()