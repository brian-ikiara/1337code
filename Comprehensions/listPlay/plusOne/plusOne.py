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
    3. digits lacks leading zeros
"""
from typing import List


class Solution:
    """Represents my Solution."""

    def plusOne(self, digits: List[int]) -> List[int]:
        """Increment the value of the leading digit by one.

        Args:
            digits (List[int]): Number represented as a List

        Returns:
            A list representing the next number as a List.
        """
        if not digits:
            return []
        if len(digits) > 1 and len(digits) < 101:
            niner = []
            i = len(digits)
            while i > 0:
                niner.append('9')
                i -= 1
            strDigits = [str(x) for x in digits]
            if int(''.join(strDigits)) < int(''.join(niner)):
                parseDigit = []
                j = 0
                while j < len(strDigits):
                    parseDigit.append(strDigits[j])
                    if strDigits == niner and parseDigit != niner:
                        sum = int(''.join(strDigits)) + 1
                        while sum % (10 * len(strDigits)) == 0:
                            parseDigit.append(0)
                            sum /= 10
                        return [int(y) for y in parseDigit]
                    strDigits.pop(j)
                    j = j + 1
        last = digits[-1]
        digits.pop(-1)
        digits.append(last + 1)
        return digits


"""LeetCode Solution #4.

    ~~~You can bring a Plus One~~~
    You are given a large integer represented as an integer array digits,
    where each digits[i] is the ith digit of the integer. The digits are
    ordered from most significant to least significant in left-to-right order.
    The large integer does not contain any leading 0's.
    Increment the large integer by one and return the resulting array of
    digits.

    Case:
        1. digits = [1,2,3] => [1,2,4]: the leading value is Incremented by one
        2. digits = [4,3,2,1] => [4,3,2,2]: value is Incremented by one
        2. digits = [9] => [1,0]: idk, maths maybe? XD

    Constraints:
        1. 1 <= digits.length <= 100
        2. 0 <= digits[i] <= 9
        3. digits lacks leading zeros
    \"""
    from typing import List


    class Solution:
        \"""Represents my Solution.\"""

        def plusOne(self, digits: List[int]) -> List[int]:
            \"""Increment the value of the leading digit by one.

            Args:
                digits (List[int]): Number represented as a List

            Returns:
                A list representing the next number as a List.
            \"""
            if not digits:
                return []
            if len(digits) < 101:
                niner = []
                i = len(digits)
                while i > 0:
                    niner.append('9')
                    i -= 1
                strDigits = [str(x) for x in digits]
                if int(''.join(strDigits)) < int(''.join(niner)):
                    j = 0
                    parseDigit = []
                    while j < len(strDigits):
                        if strDigits == niner:
                            sum = str(int(''.join(strDigits)) + 1)
                            while sum % (10 * len(strDigits)) == 0:
                                parseDigit.append(0)
                                sum /= 0
                        parseDigit.append(int(strDigits[j]))
                        strDigits.pop(j)
                        j += 1
                    return parseDigit
                else:
                    last = digits[-1]
                    digits.pop(-1)
                    digits.append(last + 1)
                    return digits
"""
