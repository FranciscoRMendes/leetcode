from typing import List


# ─── BUILD PREFIX SUM ─────────────────────────────────────────────────────────
#
# prefix[i] = sum of nums[0..i-1]
# prefix[0] = 0  (sentinel, makes range queries clean)
#
# range sum [l, r] (inclusive) = prefix[r+1] - prefix[l]

def build(nums: List[int]) -> List[int]:
    prefix = [0] * (len(nums) + 1)
    for i, x in enumerate(nums):
        prefix[i + 1] = prefix[i] + x
    return prefix


def range_sum(prefix: List[int], l: int, r: int) -> int:
    return prefix[r + 1] - prefix[l]


# ─── SUBARRAY SUM EQUALS K ────────────────────────────────────────────────────
#
# Key insight: sum(i..j) == k  ←→  prefix[j] - prefix[i] == k
#                                ←→  prefix[i] == prefix[j] - k
#
# Store seen prefix sums in a hashmap and look up complement on the fly.
# Works for negative numbers (unlike sliding window).

def subarray_sum_equals_k(nums: List[int], k: int) -> int:
    count = 0
    prefix = 0
    seen = {0: 1}           # prefix sum 0 seen once (empty subarray)

    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count


# ─── SUBARRAY SUM DIVISIBLE BY K ─────────────────────────────────────────────
#
# Key insight: sum(i..j) % k == 0  ←→  prefix[j] % k == prefix[i] % k
# Store remainder frequencies; use (remainder % k + k) % k to handle negatives.

def subarray_divisible_by_k(nums: List[int], k: int) -> int:
    count = 0
    prefix = 0
    remainders = {0: 1}

    for x in nums:
        prefix += x
        rem = prefix % k
        count += remainders.get(rem, 0)
        remainders[rem] = remainders.get(rem, 0) + 1

    return count


# ─── 2D PREFIX SUM ────────────────────────────────────────────────────────────
#
# prefix[r][c] = sum of rectangle from (0,0) to (r-1, c-1)
# region sum (r1,c1)..(r2,c2) = prefix[r2+1][c2+1]
#                               - prefix[r1][c2+1]
#                               - prefix[r2+1][c1]
#                               + prefix[r1][c1]      ← inclusion-exclusion

def build_2d(matrix: List[List[int]]) -> List[List[int]]:
    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    for r in range(rows):
        for c in range(cols):
            prefix[r+1][c+1] = (matrix[r][c]
                                 + prefix[r][c+1]
                                 + prefix[r+1][c]
                                 - prefix[r][c])
    return prefix


def region_sum(prefix: List[List[int]], r1: int, c1: int, r2: int, c2: int) -> int:
    return (prefix[r2+1][c2+1]
            - prefix[r1][c2+1]
            - prefix[r2+1][c1]
            + prefix[r1][c1])
