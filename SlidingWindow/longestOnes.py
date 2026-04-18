from typing import List

def valid(window, k) -> bool:
    if not window and k ==0:  # empty window is invalid
        return False
    max_freq = max(window.values())
    window_len = sum(window.values())
    return window_len - max_freq <= k

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        window = {}
        result = 0

        for right in range(len(nums)):
            x = nums[right]
            window[x] = window.get(x, 0) + 1

            # shrink left until valid
            while not valid(window, k):
                y = nums[left]
                window[y] -= 1
                if window[y] == 0:
                    del window[y]
                left += 1

            # update result after every valid window
            result = max(result, right - left + 1)

        return result



if __name__=="__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    solution = Solution()
    print(solution.longestOnes(nums,k))

    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    solution = Solution()
    print(solution.longestOnes(nums, k))

    nums = [0,0,0,0]
    k= 0
    print(solution.longestOnes(nums, k))