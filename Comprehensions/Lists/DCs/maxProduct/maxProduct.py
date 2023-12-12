"""Daily Challenge #2.

~~~Can we Maximise our Productivity?~~~
Given the array of integers nums, you will choose two different indices i and
j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Case:
    1. nums = [3, 4, 5, 2] => 12: the max possible value is 12
    2. digits = [1, 5, 4, 5] => 16: idk maths?
    2. digits = [3, 7] => 12: lol XD

Constraints:
    1. 2 <= nums.length <= 500
    2. 1 <= nums[i] <= 10^2
"""
from typing import List


class Solution:
    """Represents my Solution."""

    def maxProduct(self, nums: List[int]) -> int:
        """Determine the maximum value of a given formula.

        Args:
            nums (List[int]): A list of numbers

        Returns:
            The maximum possible value of the formula.
        """
        """
        def findMax(n1: int, n2: int) -> int:
            \"""Compare the larger value of two integers.
            
            This implementation beats 97/112 of the Test Cases. It fails at the following
            Test Case:
                nums = [1,8,5,4,10,2,6,1,1,1,9] => 45 and not 72

            Args:
                n1 (int): First integer
                n2 (int): Second integer

            Returns:
                The larger of n1 and n2.
            \"""
            if not n1 or not n2:
                return -1
            return max(n1, n2)

        maxNum = (nums[0] - 1) * (nums[-1] - 1)
        left, right = 0, len(nums) - 1

        while left < right:
            curr = (nums[left] - 1) * (nums[right] - 1)
            maxNum = findMax(maxNum, curr)

            if nums[left] < nums[right]:
                left += 1
            else:
                right -= 1

        return maxNum
        """
        # The simplest approach is to make attempt to sort the
        # array and compare the product obtained with the value
        # of the last and second-from-last as the inputs to the
        # function. This totally nukes the need of iteration.
        #
        # I feel dumb!!! :crying:
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
