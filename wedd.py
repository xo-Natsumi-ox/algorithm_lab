import unittest


def count_couple(couples):
    couples.sort()
    tribes = []
    for human in couples:
        for tribe in tribes:
            if human[0] in tribe:
                tribe.add(human[1])
                break

            if human[1] in tribe:
                tribe.add(human[0])
                break
        else:
            tribes.append({human[0], human[1]})
    return tribes


def count_boys_and_girls(tribes):
    print(tribes)

    girls_in_tribes = []
    boys_in_tribes = []
    people_in_tribles = []
    for tribe in tribes:
        girls = []
        boys = []
        human_in_tribles = []
        for human in tribe:
            human_in_tribles.append(human)
            if human % 2:
                boys.append(human)

            else:
                girls.append(human)

        girls_in_tribes.append(len(girls))
        boys_in_tribes.append(len(boys))
        people_in_tribles.append(len(human_in_tribles))
    allvariants = sum(boys_in_tribes) * sum(girls_in_tribes)
    boys_and_girls = zip(boys_in_tribes, girls_in_tribes)
    variants_in_one_tribe = sum((boy * girl for boy, girl in boys_and_girls))
    result = allvariants - variants_in_one_tribe
    return result


class TestMethods(unittest.TestCase):
    def test_one(self):
        self.assertEqual(count_boys_and_girls(count_couple([(1, 3), (3, 5), (5, 7), (4, 6), (2, 4), (6, 8)])), 16)

    def test_two(self):
        self.assertEqual(count_boys_and_girls(count_couple([(4, 3), (2, 1), (1, 7), (8, 6), (6, 5)])), 11)

    def test_three(self):
        self.assertEqual(count_boys_and_girls(count_couple([(4, 2), (3, 1), (1, 5), (8, 6), (4, 6)])), 12)

    def test_four(self):
        self.assertEqual(count_boys_and_girls(count_couple([(1, 2), (3, 4), (5, 6), (4, 6)])), 4)

    def test_five(self):
        self.assertEqual(count_boys_and_girls(count_couple([(1, 3), (4, 5), (4, 6), (3, 8)])), 5)


if __name__ == '__main__':
    couples_of_people = []
    with open("wedd.in", "r") as file:
        for row in file:
            first, second = row.split(" ")
            first = int(first)
            second = int(second)
            couples_of_people.append((first, second))

    length_of_couples = len(couples_of_people)
    if length_of_couples > 10000:
        print("too many couples are inputted or not at all")
    else:
        result = count_boys_and_girls(count_couple(couples_of_people))
        print(result)
        print("******unittest*******")
        unittest.main()
    with open("wedd.out", "w") as file:
        file.write(str(result))
