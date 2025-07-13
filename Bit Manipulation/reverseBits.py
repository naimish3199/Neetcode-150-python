# LeetCode Problem: 190. Reverse Bits
# https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Returns reverse bits of a given 32 bits unsigned integer 

        Approach:
        Extract last bit of n and appends it to the result's leftmost bit. This is done by:
        - Iterating over all 32 bits (from 0 to 31)
        - For each bit position i, extract the i-th bit from n using (n >> i) & 1
        - Place this bit at the (31-i)-th position in the result using (i_bit << (31-i))
        - Combine it with result using bitwise OR
        - Repeat for all 32 bits to build the reversed number

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        result = 0
        for i in range(32):
            i_bit = (n >> i) & 1 
            result = result | (i_bit << (31-i))
        return result

if __name__ == "__main__":
    n = 4294967293
    sol = Solution()
    print(f"For n = {n} (binary: {n:032b}), the reversed bits are: {sol.reverseBits(n):032b} (decimal: {sol.reverseBits(n)})")