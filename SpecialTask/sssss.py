import collections


def solution(data, n):
    value_to_remove = [item for item, count in collections.Counter(data).items() if count > n]
    final = [i for i in data if i not in value_to_remove]
    if data:
        print(','.join(map(str, final)))
    else:
        print('')


if __name__ == '__main__':
    data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    n = 1
    solution(data, n)


