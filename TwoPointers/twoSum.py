from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        nums = sorted(nums)
        while left<right:
            if nums[left]+nums[right]==target:
                return [left, right]
            elif nums[left]+nums[right]<target:
                left += 1
            else:
                right -= 1


if __name__=="__main__":
    solution = Solution()
    nums = [2,7,11,15]
    print(solution.twoSum(nums, 9))

    nums = [3,2,4]
    print(solution.twoSum(nums, 6))