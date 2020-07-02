"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
import random

def quicksort(array):
    # Randomly select pivot
    random_element_index = random.randint(0, len(array))
    pivot = array[random_element_index]

    # Move pivot to the end
    array[random_element_index] = array[-1]
    array[-1] = pivot


    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test))