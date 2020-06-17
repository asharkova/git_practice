def solution(l):
    counter = 0
    memo = [0] * len(l)
    for i in range(len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[j] % l[i] == 0:
                memo[j] += 1
                counter += memo[i]
    return counter


if __name__ == "__main__":
    print(solution([1, 2, 3, 4, 5, 6]))
