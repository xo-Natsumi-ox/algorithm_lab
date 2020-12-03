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


if __name__ == '__main__':
    couples_of_people = []
    with open("wedd.in", "r") as file:
        for row in file:
            first, second = row.split(" ")
            first = int(first)
            second = int(second)
            couples_of_people.append((first, second))

    couples = [(1, 2), (8, 7), (3, 8), (8, 10), (1, 5)]
    length_of_couples = len(couples_of_people)
    if length_of_couples > 10000:
        print("too many couples are inputted or not at all")
    else:
        result = count_boys_and_girls(count_couple(couples))
        print(result)
    with open("wedd.out", "w") as file:
        file.write(str(result))
