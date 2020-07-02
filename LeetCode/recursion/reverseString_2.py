class Solution(object):
    def reverseString(self, s):
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


if __name__ == '__main__':
    solution = Solution()
    solution.reverseString(s=["h", "e", "l", "l", "o"])
