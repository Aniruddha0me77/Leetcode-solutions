class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def display(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next

def rotateRight(head, k: int)-> ListNode:
        length = 0
        cur = ListNode()
        cur.next = head
        while cur.next:
            length += 1
            cur = cur.next       
        if length == 0:
            return head    
        elif k%length == 0:           
                    return head
        elif length > k:
            for i in range(k):
                if head and head.next:
                    curr = ListNode()
                    curr.next = head
                    pre = [head]
                    while head.next:
                        head = head.next
                        curr = curr.next
                    curr.next = None
                    head.next = pre[0]
        else:
            new = k
            while (new % length) != 0:
                new -= 1
            new_k = k-new
            for i in range(new_k):
                if head and head.next:
                    curr = ListNode()
                    curr.next = head
                    pre = [head]
                    while head.next:
                        head = head.next
                        curr = curr.next
                    curr.next = None
                    head.next = pre[0]

        return head
