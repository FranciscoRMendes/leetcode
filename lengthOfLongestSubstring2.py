
def valid(window):
    return all(count <= 1 for count in window.values())

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        window = {}

        for right in range(len(s)):
            # expand right window
            x = s[right]
            window[x] = window.get(x, 0) + 1

            # shrink window until valid
            while not valid(window):
                y = s[left]
                window[y] -= 1
                if window[y] == 0:
                    del window[y]
                left +=1

            # update answer
            result = max(result, right - left + 1)

        return result

if __name__ == '__main__':
    s = "abcabcbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))

    s = "bbbbb"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))

    s = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))

    s = "dvdf"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
