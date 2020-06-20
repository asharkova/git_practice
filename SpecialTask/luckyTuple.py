def solution(l):
    # triple_array = [[l[x], l[y], l[z]] for x in range(len(l)) for y in range(x + 1, len(l))
    #                 for z in range(y + 1, len(l)) if l[z] % l[y] == 0 and l[y] % l[x] == 0]
    # print(len(triple_array))
    # print(triple_array)
    # l.sort()
    triple_array = []
    for list in l:
        for x in range(len(l)):
            for y in range(x+1, len(l)):
                for z in range(y+1, len(l)):
                    if l[z] % l[y] == 0 and l[y] % l[x] == 0:
                        triple_array.append([l[x], l[y], l[z]])
    return len(triple_array), triple_array


if __name__ == "__main__":
    #print(solution([1, 2, 3, 4, 5, 6]))
    #print(solution([2, 4, 8, 12, 2, 6]))
    #print(solution([6, 3, 4, 1]))
    #print(solution([1, 13, 7, 19, 17, 1, 1]))
    print(solution([[1, 2, 4], [1, 2, 4]]))