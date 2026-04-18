class Solution:
    def minInsertions(self, s: str) -> int:
        left = 0
        right = len(s)-1
        s = list(s)
        while left < right:
            left_char = s[left]
            right_char = s[right]
            if left_char != right_char:
                s.insert(right+1, left_char)
                s.insert(left, right_char)
                left+=1
                right-=1
            else:
                right-=1
                left+=1
        return s



if __name__ == "__main__":
    solution = Solution()
    s = "mbadm"
    s = "zzazz"
    print(solution.minInsertions(s))

    s = "leetcode"
    print(solution.minInsertions(s))
