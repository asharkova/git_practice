import collections


def solution(data, n):
    final = []
    different = [item for item, count in collections.Counter(data).items() if count <= n]
    for i in range(0, len(data)):
        for j in range(0, len(different)):
            if data[i] == different[j]:
                final.append(data[i])
    if data:
        print(','.join(map(str, final)))
    else:
        print('')


if __name__ == '__main__':
    data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    n = 2
    solution(data, n)


