class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        cur_str = ""
        max_len = 0
        while right < len(s):
            if s[right] in cur_str:
                left = left + 1
                max_len = max(max_len, len(cur_str))
                cur_str = cur_str[left:right]
            else:
                cur_str+=s[right]
                right = right+1

            max_len = max(max_len, len(cur_str))

        return max_len


if __name__ == '__main__':
    # s = "abcabcbb"
    # solution = Solution()
    # print(solution.lengthOfLongestSubstring(s))
    #
    # s = "bbbbb"
    # solution = Solution()
    # print(solution.lengthOfLongestSubstring(s))
    #
    # s = "pwwkew"
    # solution = Solution()
    # print(solution.lengthOfLongestSubstring(s))

    s = "dvdf"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))

    s = "bbtablud"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))