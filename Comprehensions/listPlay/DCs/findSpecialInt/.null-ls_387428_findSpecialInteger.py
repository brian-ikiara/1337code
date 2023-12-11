"""Daily Challenge #1.

~~~There's an Integer that's special to me~~~
Given an integer array sorted in non-decreasing order, there is
exactly one integer in the array that occurs more than 25% of the
time, return that integer.

Case:
    1. arr = [1,2,2,6,6,6,6,7,10] => 6: the most repeated value is 6
    2. arr = [1,1] => 1: obviously, it's 1

Constraints:
    1. 1 <= arr.length <= 10^4
    2. 0 <= array[i] <= 10^5
"""
from typing import List


class Solution:
    """Represents my Solution."""

    def findSpecialInteger(self, arr: List[int]) -> int:
        """Return the integer with high occurence rate.

        So, our approach can divide the array into two then as we loop
        through each half we could be checking whether each integer
        falls under the range of 25%, 50%, 75% or 100% to 1%. We'll
        ignore all them ints that fall under 25%.

        Args:
            arr (List[int]): An array of integers

        Returns:
            An integer that occurs more than 25% of the time.
        """
        memo = dict({})
        counter = 0
        for digit in arr:
            memo[str(digit)] = counter
            current = digit
            if current == digit:
                counter += 1
        if counter 
