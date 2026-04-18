def valid(window, k):
    # length of window
    window_len = sum(window.values())
    # max frequency char count
    max_freq = max(window.values())
    # valid if we can replace the rest within k
    return window_len - max_freq <= k

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        result = 0
        window = {}

        for right in range(len(s)):
            # expand right window
            x = s[right]
            window[x] = window.get(x, 0) + 1

            # shrink window until valid
            while not valid(window, k):
                y = s[left]
                window[y]-=1
                if window[y] == 0:
                    del window[y]
                left+=1
            result = max(result, right - left + 1)
        return result



if __name__ == '__main__':
    s = "ABAB"
    k = 2
    solution = Solution()
    print(solution.characterReplacement(s,k))

    s = "AABABBA"
    k = 1
    solution = Solution()
    print(solution.characterReplacement(s,k))

    # s = "bbbbb"
    # solution = Solution()
    # print(solution.characterReplacement(s))
    #
    # s = "pwwkew"
    # solution = Solution()
    # print(solution.characterReplacement(s))
    #
    # s = "dvdf"
    # solution = Solution()
    # print(solution.characterReplacement(s))