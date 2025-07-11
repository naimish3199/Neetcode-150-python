# LeetCode Problem: Single Number
# https://leetcode.com/problems/single-number/description/

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Finds the element that appears only once in a list where every other element appears twice.
        Uses bitwise XOR to cancel out duplicate numbers.

        XOR Properties Used:
        - a ^ a = 0 (any number XOR itself is 0)
        - a ^ 0 = a (any number XOR 0 is the number itself)
        - XOR is commutative and associative, so order doesn't matter
        - By XOR-ing all numbers, pairs cancel out and only the unique number remains.

        Time Complexity: O(n), where n is the number of elements in nums.
        Space Complexity: O(1), only a constant amount of extra space is used.
        """
        # Initialize result to 0. XOR-ing with 0 leaves the number unchanged.
        result = 0
        # XOR all numbers together. Pairs cancel out, leaving the unique number.
        for num in nums:
            result ^= num
        # The result now holds the single number.
        return result
    
if __name__ == "__main__":
    nums = [4,1,2,1,2]
    sol = Solution()
    print(f"The single number is: {sol.singleNumber(nums)}")