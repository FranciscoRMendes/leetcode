from typing import List


class Solution(object):
    def valid(self, word):
        return all([x == 1 for x in word.values()])

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = {}
        max_len = 0
        left = 0
        for right in range(len(s)):
            right_letter = s[right]
            word[right_letter] = word.get(right_letter, 0) + 1
            if not self.valid(word):
                left_letter = s[left]
                word[left_letter] -= 1
                if word[left_letter] == 0:
                    del word[left_letter]
                left += 1
            else:
                max_len = max(max_len, len(word))

        return max_len


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [seen[complement], i]
            seen[x] = i


class Solution:

    def vol(self, lh, rh, left, right):
        # lh = window[left]
        # rh = window[right]
        vol = min(lh, rh) * (right - left)
        return vol

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_vol = 0
        while right > left:
            cur_vol = (right - left) * min(height[left], height[right])
            max_vol = max(max_vol, cur_vol)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_vol





