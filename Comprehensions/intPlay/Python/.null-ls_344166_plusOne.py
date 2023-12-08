"""LeetCode Solution #4.

~~~You can bring a Plus One~~~
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer. The digits are
ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Case:
    1. digits = [1,2,3] => [1,2,4]: the leading value is Incremented by one
    2. digits = [4,3,2,1] => [4,3,2,2]: the leading value is Incremented by one
    2. digits = [9] => [1,0]: idk, maths maybe? XD

Constraints:
    1. 1 <= digits.length <= 100
    2. 0 <= digits[i] <= 9
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
