def solution(mach, facula):
    # Convert arguments mach and facula into integers to be able to operate with them
    mach, facula = int(mach), int(facula)

    # Determine number of generations as 0
    counter = 0

    # Until bot mach and facula don't equal 1 iterate through the loop to find number
    # of generation to destroy the LAMBCHOP device
    while not (mach == 1 and facula == 1):
        # Check if mission still could be performed
        if facula <= 0 or mach <= 0:
            return "impossible"
        if facula == 1:
            # If one of the bomb types equals 1, return the number of generations
            # as string. Where counter is how many bombs were produced before, plus another type of bombs
            # that left and minus one, because initial number of bombs should be (1, 1)
            return str(counter + mach - 1)
        else:
            # If condition above is not satisfied then we continue to calculate
            # how many steps we need till next generation
            counter += int(mach/facula)
            mach, facula = facula, mach % facula
    return "impossible"


if __name__ == '__main__':
    print(solution('1', '2'))
    print(solution('1', '1'))
    print(solution('4', '7'))
    print(solution('2', '4'))

