import re


def fantz(binary, number):
    length_of_binary = len(binary)
    possible_variants = []
    for i in range(length_of_binary):
        count_possible_variants = bin(number ** (i))[2:]
        if len(count_possible_variants) > length_of_binary:
            break
        possible_variants.append(count_possible_variants)
    print(possible_variants)
    return possible_variants


def find_part_in_binary(binary, possible_variants):
    binary = str(binary)
    counter_of_parts = 0
    possible_variants.reverse()
    for variant in possible_variants:
        part_of_binary = re.compile(variant)
        result = part_of_binary.findall(binary)
        if result != []:
            for one_result in result:
                binary = re.sub(part_of_binary, "", binary)
                counter_of_parts = counter_of_parts + 1
    print(counter_of_parts)
    return counter_of_parts


if __name__ == '__main__':
    with open("fantz.in", "r") as file:
        for line in file:
            binary, number = line.split(" ")
            number = int(number)
    print("in: " + binary, number)
    if len(binary) > 100 or number > 100 or number < 0:
        print("wrong input values, please try again")
        result = -1
    else:
        possible_variants = fantz(binary, number)
        binary = str(binary)
        result = find_part_in_binary(binary, possible_variants)
    with open("fantz.out", "w") as file:
        file.write(str(result))
