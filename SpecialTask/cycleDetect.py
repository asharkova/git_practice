from operator import mul


def base10ToOther(number, base):
    """
    Converts number from base 10 to another base

    number {int} -- number as the string that needs to be converted
    base {int} -- original base of the integer
    return {str} -- integer as a string
    """
    e = number//base
    q = number % base
    if number == 0:
        return '0'
    elif e == 0:
        return str(q)
    else:
        return base10ToOther(e, base) + str(q)


def baseOtherTo10(number, base):
    """
    Checks if number in base 10, if not converts it, otherwise returns number.

    number {str} -- number as the string that needs to be converted
    base {int} -- original base of the integer
    return {str} -- integer as a string
    """
    if 2 <= base < 10:                         # Checking if number already in base 10
        # Find exponentiation for number base. Put it in the list.
        exponentiation = sorted([base ** i for i in range(0, len(number))], reverse=True)
        # Multiply exponentiation and integers from number, sum them up to get number in the base 10.
        number = sum(list(map(mul, exponentiation, [int(i) for i in number])))
        return str(number)
    elif base == 10:
        return number


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Numbers(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def length(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter

    def isCycle(self, moves):
        cycle_length = 0
        first_pointer = self.head
        second_pointer = self.head
        length = 0
        for i in range(0, moves):
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next.next
            if first_pointer.value == second_pointer.value:
                cycle_length += 1
                first_pointer = first_pointer.next
                if first_pointer.value == second_pointer.value:
                    return cycle_length
                else:
                    while first_pointer.value != second_pointer.value:
                        first_pointer = first_pointer.next
                        cycle_length += 1
                    return cycle_length
        return cycle_length


def solution(n, b):
    numbers = Numbers()
    moves = 0
    numbers.append(Element(int(n)))
    while int(n) and int(n) > 0:
        moves = moves + 1
        for i in range(0, 2):
            # Iterate through algorithm till n exists and n is non-negative
            n = [n[i] for i in range(0, len(n))]       # Create a list made of integer strings
            # Start with a random minion ID n, which is a non-negative integer of length k in base b
            id_length = len(n)
            # Define x and y as integers of length k. x has the digits of n in descending order, and
            # y has the digits of n in ascending order
            x = ''.join(sorted(n, reverse=True))
            x = baseOtherTo10(x, b)
            y = ''.join(sorted(n))
            y = baseOtherTo10(y, b)
            # Define z = x - y.
            z = int(x) - int(y)
            z = base10ToOther(z, b)
            # Add leading zeros to z to maintain length k if necessary
            if len(str(z)) < id_length:
                zero_amount = id_length - len(str(z))
                z = '0' * zero_amount + str(z)
            numbers.append(Element(int(z)))
            # Assign n = z to get the next minion ID, and go back to step 2
            n = str(z)
        cycle_length = numbers.isCycle(moves)
        if cycle_length != 0:
            return cycle_length


if __name__ == '__main__':
    solution('210022', 3)
