# LeetCode Problem: 268. Missing Number
# https://leetcode.com/problems/missing-number

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Returns the missing number from the array `nums` containing n distinct numbers in the range [0, n].

        XOR Properties Used:
        - a ^ a = 0 (any number XOR itself is 0)
        - a ^ 0 = a (any number XOR 0 is the number itself)
        - XOR is commutative and associative, so order doesn't matter
        - By XOR-ing all numbers, pairs cancel out and only the unique number remains.

        Time Complexity: O(n), where n is the number of elements in nums.
        Space Complexity: O(1), only a constant amount of extra space is used.
        """
        result = len(nums)
        for i in range(len(nums)):
            result ^= nums[i] ^ i
        return result
    
if __name__ == "__main__":
    nums = [9,6,4,2,3,5,7,0,1]
    sol = Solution()
    print(f"The missing number in array {nums} is: {sol.missingNumber(nums)}")