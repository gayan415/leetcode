"""
https://leetcode.com/problems/reverse-linked-list/
206. Reverse Linked List

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

# Iterative solution
class Solution1:
  def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    nxt = None
    curr = head

    while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr= nxt
    
    head = prev
    return head
