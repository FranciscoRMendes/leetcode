from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for explorer in range(0, len(nums)):
            if nums[explorer] != 0:
                nums[anchor], nums[explorer] = nums[explorer], nums[anchor]
                anchor+=1

if __name__ == "__main__":
    solution = Solution()
    nums = [0,1,0,3,12]
    print(solution.moveZeroes(nums))

    nums = [0]
    print(solution.moveZeroes(nums))
