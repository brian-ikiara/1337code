"""LeetCode Solution #2.

~~~Is it a Palindrome~~~
Given an integer x, return true if x is a Palindrome
and false otherwise.

Case:
    1. x = 121 => true: reads forwards and backwards as 121
    2. x = -121 => false: reads backwards as 121-
    3. x = 10 => false: it just isn't a Palindrome

Constraints:
    -2^31 <= x <= 2^31 - 1: Make sure it's O(n) or better!
"""


class Solution:
    """Represents my Solution."""

    def isPalindrome(self, x: int) -> bool:
        """Determine if a number is a Palindrome.

        Args:
            x (int): number

        Returns:
            Confirmation.
        """
        return f'{x}' == f'{x}'[::-1]
