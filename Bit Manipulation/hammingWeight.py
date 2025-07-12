# LeetCode Problem: 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Counts the number of '1' bits (Hamming weight) in the binary representation of an integer.
        Uses Brian Kernighan's algorithm to efficiently count set bits.

        Property Used:
        - n & (n-1) => removes lowest set bit from n
        
        Time Complexity: O(k), where k is the number of set bits.
        Space Complexity: O(1).
        """
        count = 0
        while n:
            n &= n - 1  # Clears the least significant bit set (n & n-1)
            count += 1
        return count

        # Alternative approach (less efficient):
        # Time Complexity: O(log n), where n is the input number (number of bits in n)
        # Space Complexity: O(1)
        # count = 0
        # while n:
        #     count += n & 1  # Add 1 if the least significant bit is set
        #     n >>= 1         # Shift right by 1 to check the next bit
            
if __name__ == "__main__":
    num = 2147483645
    sol = Solution()
    print(f"Binary representation of {num} has {sol.hammingWeight(num)} set bit(s).")