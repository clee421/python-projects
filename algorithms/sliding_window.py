"""
Given an array of positive integers nums and a positive integer target, return the minimal
length of a subarray whose sum is greater than or equal to target. If there is no such
subarray, return 0 instead.

https://leetcode.com/problems/minimum-size-subarray-sum
"""

from typing import List, Tuple

def min_sub_array_len(target: int, nums: List[int]) -> Tuple[int, int]:
        min_len = None

        i, j = 0, 0
        # len_range = (i, j)
        curr_sum = nums[0]
        while i <= j:
            # print("working with", (i, j), curr_sum)
            if curr_sum >= target:
                if min_len is None or (j - i) < min_len:
                    min_len = j - i + 1
                    len_range = (i, j)

            if min_len == 1:
                return min_len

            if curr_sum < target and j < len(nums) - 1:
                j += 1
                curr_sum += nums[j]
            else:
                curr_sum -= nums[i]
                i += 1

        # print(len_range)
        return len_range if min_len is not None else (-1, -1)

def main():
    nums = [2, 3, 1, 2, 4, 3]
    target = 7

    sub_arr = min_sub_array_len(target, nums)
    print(f"subarray: {sub_arr}, length: {sub_arr[1] - sub_arr[0] if sub_arr[0] != -1 else 0}")

if __name__ == "__main__":
    main()