import re
import unittest


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


def count_result(binary, number):
    possible_variants = fantz(binary, number)
    binary = str(binary)
    result = find_part_in_binary(binary, possible_variants)
    return result


def in_out_result():
    with open("fantz.in", "r") as file:
        for line in file:
            binary, number = line.split(" ")
            number = int(number)
    print("in: " + binary, number)
    if len(binary) > 100 or number > 100 or number < 0:
        print("wrong input values, please try again")
        result = -1
    else:
        result = count_result(binary, number);
    with open("fantz.out", "w") as file:
        file.write(str(result))


class TestMethods(unittest.TestCase):
    def test_one(self):
        self.assertEqual(count_result("10110001", 4), 4)

    def test_two(self):
        self.assertEqual(count_result("10101010101", 5), 3)

    def test_three(self):
        self.assertEqual(count_result("[10110100", 9), 4)

    def test_four(self):
        self.assertEqual(count_result("10000100001", 4), 3)

    def test_five(self):
        self.assertEqual(count_result("1111101", 5), 1)


if __name__ == '__main__':
    in_out_result()
    print("******unittest*******")
    unittest.main()
