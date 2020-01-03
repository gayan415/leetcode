"""
https://leetcode.com/problems/remove-linked-list-elements/
203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 01
class Solution1:
	def removeElements(self, head: ListNode, val: int) -> ListNode:
    myList = ListNode(0)
    myHead = myList
    while head:
      if head.val != val:
        tmp = ListNode(head.val)
        myList.next = tmp
          myList = tmp
      head = head.next
    return myHead.next

# Solution 02
class Solution2:
  def removeElements(self, head: ListNode, val: int) -> ListNode:
    if head == None: return None
      head.next = self.removeElements(head.next, val);
      if head.val == val:
        return head.next
      return head
