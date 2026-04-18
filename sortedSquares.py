from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        final_list = []

        while right >= left:
            left_num = nums[left]
            right_num = nums[right]
            if left_num**2 > right_num**2:
                final_list.insert(0,left_num**2)
                left += 1
            elif left_num**2 <= right_num**2:
                final_list.insert(0,right_num**2)
                right -= 1

        return final_list



if __name__=="__main__":
    solution = Solution()
    nums = [-4,-1,0,3,10]
    final_list = solution.sortedSquares(nums)
    print(final_list)

    nums = [-7, -3, 2, 3, 11]
    final_list = solution.sortedSquares(nums)
    print(final_list)
