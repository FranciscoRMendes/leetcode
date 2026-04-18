from typing import List

def valid(nums: List[int], limit) -> bool:
    min_num = min(nums)
    max_num = max(nums)
    if max_num-min_num <= limit:
        return True
    return False



class Solution:
    def longestSubarray(self, nums: List[int], limit: int)->int:
        left = 0
        result = 0
        window = {}

        for right in range(len(nums)):
            # 1. expand window
            x = nums[right]
            window[x] = window.get(x, 0) + 1

            # 2. shrink window until valid
            while not valid(window, limit):
                y = nums[left]
                window[y] -= 1
                if window[y] == 0:
                    del window[y]
                left += 1

            # 3. update answer
            result = max(result, right - left + 1)

        return result


if __name__=="__main__":
    solution = Solution()
    nums = [8, 2, 4, 7]
    limit = 4
    result = solution.longestSubarray(nums, 4)
    print(result)
    solution = Solution()
    nums = [10,1,2,4,7,2]
    limit = 4
    result = solution.longestSubarray(nums, 5)
    print(result)