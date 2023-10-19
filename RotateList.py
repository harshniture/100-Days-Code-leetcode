# Given the head of a linked list, rotate the list to the right by k places.

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head :
            return head
                               
…       add_nodes = [ListNode(value) for value in rot_val]
        add_nodes[-1].next = head
        
        for i in range(rot-1,0,-1):
            add_nodes[i-1].next = add_nodes[i]
        
        head = add_nodes[0] 

        return head