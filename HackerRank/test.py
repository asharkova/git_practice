import random
import string


def print_rangoli(size):
    letters = string.ascii_lowercase
    random_letters = []
    for i in range(size):
        random_letters.append(random.choice(letters))
    print(random_letters)
    random_letters.reverse()
    print(random_letters)
    # middle_part = ("-".join(random_letters) + "-".join(random_letters.reverse()))
    height = size - 1



    print(middle_part)


if __name__ == '__main__':
    print_rangoli(3)
