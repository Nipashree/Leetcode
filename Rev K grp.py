class Solution:
    def reverseKGroup(self, head, k):

        current = head

        # Check if there are k nodes
        for i in range(k):
            if current is None:
                return head
            current = current.next

        # Reverse k nodes
        prev = None
        current = head

        for i in range(k):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # head is now the last node of reversed group
        head.next = self.reverseKGroup(current, k)

        return prev
