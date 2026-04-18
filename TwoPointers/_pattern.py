from typing import List


# ─── OPPOSITE ENDS (sorted array / shrinking window) ─────────────────────────

def opposite_ends(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1

    while left < right:
        current = nums[left] + nums[right]

        if current == target:
            return [left, right]
        elif current < target:
            left += 1
        else:
            right -= 1

    return []


# ─── SAME DIRECTION (fast / slow) ─────────────────────────────────────────────

def fast_slow(nums: List[int]):
    slow = 0

    for fast in range(len(nums)):
        # condition to advance slow pointer
        if nums[fast] != 0:             # example: skip zeros
            nums[slow] = nums[fast]
            slow += 1

    return slow                         # slow is the new length


# ─── THREE POINTERS (e.g. threeSum) ───────────────────────────────────────────

def three_pointers(nums: List[int], target: int):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:   # skip duplicates
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1

    return result
