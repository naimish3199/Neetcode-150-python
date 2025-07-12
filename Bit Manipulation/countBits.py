# LeetCode Problem: 338. Counting Bits
# https://leetcode.com/problems/counting-bits/

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        Returns a list where the ith element is the number of 1's in the binary representation of i, for all i in the range [0, n].

        Approach:
        - Dynamic programming using the relationship:
          result[i] = 1 + result[i - offset], where offset is the largest power of two less than or equal to i.
        - Efficiently builds up the result array by leveraging previously computed values.

        Example:
            0 -> 0000 -> 0
            1 -> 0001 -> 1 = 1 + dp[n-1]
            2 -> 0010 -> 1 = 1 + dp[n-2]
            3 -> 0011 -> 2 = 1 + dp[n-2]
            4 -> 0100 -> 1 = 1 + dp[n-4]
            5 -> 0101 -> 2 = 1 + dp[n-4]
            6 -> 0110 -> 2 = 1 + dp[n-4]
            7 -> 0111 -> 3 = 1 + dp[n-4]
            8 -> 1000 -> 1 = 1 + dp[n-8]
            
        Time Complexity: O(n), where n is the input number.
        Space Complexity: O(n), for the output list.
        """
        result = [0]*(n+1)
        offset = 1
        for i in range(1,n+1):
            if offset * 2 == i:
                offset = i
            result[i] = 1 + result[i-offset]
        return result
    
        # Alternative approach (less efficient): Calculate number of set bits for each integer from 0 to n
        # Time Complexity: O(n log n)
        # Space Complexity: O(n)
        
if __name__ == "__main__":
    n = 5
    sol = Solution()
    result = sol.countBits(n)
    print(f"For n = {n}, the number of 1's in binary representation of all integers from 0 to {n} is: {result}")