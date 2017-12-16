lines = []


def part1():
    print("PART 1:\n")

    with open('day7input.txt') as f:

        for line in f:
            parts = line.split("->")
            print(parts)
            name = parts[0].split(" ")[0]
            stack = None
            if len(parts) == 2:
                stack = parts[1]

            lines.append((name, stack))

        lookup = lines[0][0]

        print(find_root(lookup, 0, None))


def find_root(lookup, bad_index, root):

    print("Finding Root")
    print(lookup)

    for i in range(0, len(lines)):

        if i == bad_index:
            continue;

        if lines[i][1] is not None and lookup in lines[i][1]:
            root = lines[i][0]
            root = find_root(root, i, root)

        #break;

    print("FINAL ROOT: "+root)
    return root;





def part2():
    print("PART 2:\n")

    lines.clear()

    with open('day7input.txt') as f:

        for line in f:
            line = line.replace("\n", "")
            parts = line.split("->")
            name = parts[0].split(" ")[0]
            weight = parts[0].split(" ")[1]
            stack = None
            if len(parts) == 2:
                stack = parts[1]

            lines.append((name, weight, stack))

        print(lines)
        lookup = lines[84][0]
        sum = lines[84][1];

        print(compute_stack(lookup, 0, sum))


def compute_stack(lookup, bad_index, sum):

    print("COMPUTE STACK")
    print(lookup)

    for i in range(0, len(lines)):

        if lookup in lines[i][0]:
            sum += lines[i][1]

        if i == bad_index:
            continue;

        if lines[i][2] is not None and lookup in lines[i][2]:

            stack = lines[i][2].replace(" ", "").split(",")
            print(stack)
            for item in stack:

                sum += compute_stack(item, i, sum)

    return sum

part1()
part2()