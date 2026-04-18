class Solution:
    def twoSum(self, nums, target):

        keys = sorted(range(len(nums)), key=nums.__getitem__)
        left, right = 0, len(nums) - 1
        pairs = []

        while left < right:

            cur_sum = nums[keys[left]] + nums[keys[right]]

            if cur_sum > target:
                right -= 1
            elif cur_sum < target:
                left += 1
            else:
                pairs.append([nums[keys[left]], nums[keys[right]]])
                left += 1
                right -= 1

        return pairs


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()

        for c in range(len(nums)):

            cur_num = nums[c]
            new_list = nums[:c] + nums[c + 1:]

            pairs = self.twoSum(new_list, -cur_num)

            for p in pairs:
                triplet = tuple(sorted(p + [cur_num]))
                result.add(triplet)

        return [list(t) for t in result]

