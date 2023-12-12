"""LeetCode Solution #3.

~~~Define your own Square Root~~~
Given a non-negative integer x, return the Square Root of x
rounded down to the nearest integer.

Case:
    1. x = 4 => 2: the Square Root of 4 is 2
    2. x = 8 => |2.8282| = 2: rounded off to the nearest integer

Constraints:
    1. The returned integer should be non-negative
    2. 0 <= x <= 2^31 - 1: Make sure it's O(n) or better!
"""


class Solution:
    """Represents my Solution."""

    def mySqrt(self, x: int) -> int:
        """Determine the Square Root of a number.

        So, I might have done some digging and I got a possible
        solution here. Let's use some Isaac Newton Magic in our
        code. We shall be implementing the following formula
        in our design:
            X_n+1 = 1/2(X_n + S / X_n)
            where X is an approximation and S is the Square

        Args:
            x (int): number

        Returns:
            The Square Root rounded off the nearest non-negative integer.
        """
        if x < 0:
            return 0
        # initialize a base guess of the Square Root
        guess = 2
        # for a number of iterations we store the
        # Newtonian Approximation of the Square
        for _ in range(69):
            guess = 0.5 * (guess + x / guess)
        # then finally return the value of the Approximation
        return int(guess)
