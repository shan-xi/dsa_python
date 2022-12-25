from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, None)
        curr = dummy_head
        carry = 0
        while l1 is not None or l2 is not None or carry != 0:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0

            sum_value = v1 + v2 + carry
            carry = sum_value // 10
            new_node = ListNode(sum_value % 10, None)
            curr.next = new_node
            curr = new_node

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummy_head.next


class Util:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    @staticmethod
    def build_single_linked_list_from_array(arr):
        head = None
        for i, v in enumerate(arr):
            if head is None:
                head = ListNode(arr[i], None)
            else:
                temp = head
                head = ListNode(arr[i], None)
                head.next = temp
        return head

    @staticmethod
    def string_result(node: Optional[ListNode]) -> Optional[str]:
        s = ""
        while node is not None:
            s += str(node.val)
            node = node.next
        return s


s = Solution()
n1 = Util.build_single_linked_list_from_array([3, 4, 2])
n2 = Util.build_single_linked_list_from_array([4, 6, 5])
print(Util.string_result(s.addTwoNumbers(n1, n2)))
