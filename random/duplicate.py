from typing import List, Tuple
import random


# Function signature (you implement this)
def find_error_nums(nums: List[int]) -> Tuple[int, int]:
    duplicate = None
    seen = set()
    for i in nums:
        if i in seen:
            duplicate = i
            break
        else:
            seen.add(i)

    n = len(nums)
    s = n * (n + 1) / 2
    actual_sum = sum(nums) - i
    missing_number = s - actual_sum
    # result[1] = int(missing_number)
    return duplicate, int(missing_number)


def run_test(input_arr: List[int], expected: Tuple[int, int]) -> None:
    result = find_error_nums(input_arr)

    print(f"Input:     {input_arr}")
    print(f"Expected:  Duplicate={expected[0]}, Missing={expected[1]}")
    print(f"Got:       Duplicate={result[0]}, Missing={result[1]}")

    if result == expected:
        print("✅ PASS\n")
    else:
        print("❌ FAIL\n")


def deterministic_tests():
    # Basic cases
    run_test([1, 2, 2, 4], (2, 3))
    run_test([1, 1], (1, 2))
    run_test([2, 2], (2, 1))

    # Unordered
    run_test([3, 1, 2, 5, 3], (3, 4))
    run_test([4, 3, 6, 2, 1, 1], (1, 5))

    # Edge-ish
    run_test([1, 5, 3, 2, 2, 6, 7, 8, 9, 10], (2, 4))
    run_test([2, 3, 4, 5, 6, 7, 8, 9, 10, 10], (10, 1))


# --- Fuzz testing ---
def generate_test(n: int) -> Tuple[List[int], Tuple[int, int]]:
    arr = list(range(1, n + 1))

    missing = random.randint(1, n)
    duplicate = random.randint(1, n)

    while duplicate == missing:
        duplicate = random.randint(1, n)

    # remove missing
    arr.remove(missing)
    # add duplicate
    arr.append(duplicate)

    random.shuffle(arr)

    return arr, (duplicate, missing)


def fuzz_tests(num_tests: int = 100, n: int = 100):
    for i in range(num_tests):
        arr, expected = generate_test(n)
        result = find_error_nums(arr)

        if result != expected:
            print(f"❌ Fuzz Test Failed at iteration {i}")
            print(f"Input: {arr}")
            print(f"Expected: {expected}, Got: {result}")
            return

    print(f"✅ All {num_tests} fuzz tests passed!")


if __name__ == "__main__":
    print("=== Deterministic Tests ===")
    deterministic_tests()

    print("=== Fuzz Tests ===")
    fuzz_tests()
