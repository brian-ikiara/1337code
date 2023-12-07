/**
 * LeetCode Solution #1
 *
 * Here's the header file for the addTwoNumbers
 * program. More documentation in the actual C
 * file.
 *
 * Copyright @2023 Brian M'Ikiara
 */
#ifndef 0_ADDTWONUMBERS_H_
#define 0_ADDTWONUMBERS_H_

/**
 * s_ListNode - Struct for a Singly Linked List Node
 * @val: Number
 * @next: Pointer to next Node
 *
 * Description: Simplest form for demonstrating the
 * linked List data structure.
 */
typedef struct s_ListNode {
  int val;
  struct s_ListNode *next;
} ListNode;

/* Prototypes */
struct ListNode* addTwoNumbers(struct ListNode*, struct ListNode*);

#endif /* 0_ADDTWONUMBERS_H_ */
