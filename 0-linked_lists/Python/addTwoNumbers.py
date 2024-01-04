"""LeetCode Solution #1.

~~~Add 2 Numbers~~~
This program takes in two singly Linked
Lists and then returns the sum of the addition of
the numbers stored in each as a Linked List too.
"""
from typing import Optional


class ListNode:
    """Represents a Singly Linked List's Node."""

    def __init__(self, val=0, next=None) -> None:
        """Initialize the Node.

        Args:
            val (int): Number
            next (Any): Pointer to Next Node
        """
        self.val = val
        self.next = next


class Solution:
    """Represents my Solution."""

    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:
        """Calculate the sum of 2 Numbers stored as Linked Lists.

        Args:
            l1 (Optional[ListNode]): First Linked List
            l2 (Optional[ListNode]): Second Linked List

        Returns:
            result: The linked list representing the solution
        """
        # since they're sequences of the ListNode object
        # we could reverse the list,
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            """Transpose the Linked List passed to it.

            Args:
                head (Optional[ListNode]): Head of Linked List

            Returns:
                result: A reversed Linked List.
            """
            result = []
            while head:
                result.append(head)
                head = head.next
            return result[::-1]

        revL1 = reverseList(l1)
        revL2 = reverseList(l2)
        # store {l1,l2}.val into 2 lists,
        # join them and convert to int
        # sum these 2 and store the reversed sum into array
        # split result and then create new Linked List
        # def toList()

"""
if __name__ == "__main__":
    try:
        pass
    except expression as identifier:
        pass
"""
