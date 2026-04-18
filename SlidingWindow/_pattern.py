from typing import List


# ─── VARIABLE SIZE WINDOW (shrink until valid) ────────────────────────────────

def valid(window: dict) -> bool:
    # define the validity condition for the window
    return True


def variable_window(s: str):
    left = 0
    result = 0
    window = {}

    for right in range(len(s)):
        # expand: add s[right] to window
        x = s[right]
        window[x] = window.get(x, 0) + 1

        # shrink until window is valid
        while not valid(window):
            y = s[left]
            window[y] -= 1
            if window[y] == 0:
                del window[y]
            left += 1

        # update answer — window [left, right] is now valid
        result = max(result, right - left + 1)

    return result


# ─── FIXED SIZE WINDOW ────────────────────────────────────────────────────────

def fixed_window(nums: List[int], k: int):
    window_sum = sum(nums[:k])
    result = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]           # add incoming element
        window_sum -= nums[right - k]       # drop outgoing element
        result = max(result, window_sum)

    return result
