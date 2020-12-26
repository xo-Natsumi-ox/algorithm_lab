import unittest


def input():
    with open("naive.in", "r") as file:
        return file.read().splitlines()


def output(result):
    with open("naive.out", "w") as file:
        file.write(str(result))


def naive_search(string, substring):
    result = []
    string_length = len(string)
    substring_length = len(substring)
    for element_in_string in range(string_length - substring_length + 1):
        for element_in_substring in range(substring_length):
            if string[element_in_string + element_in_substring] != substring[element_in_substring]:
                break
        else:
            result.append((element_in_string, element_in_string + substring_length - 1))
    return result


if __name__ == '__main__':
    string, substring = input()
    result = naive_search(string, substring)
    output(result)
    print(result)
