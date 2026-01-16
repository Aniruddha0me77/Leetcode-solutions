class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def pairSum(self) -> int:
        curr = ListNode()
        curr.next = self.head        
        num = []
        max = 0
        while curr.next:
            num.append(curr.next.val)
            curr = curr.next
        j = len(num)-1
        for i in range(len(num)//2):
            if max < num[i] + num[j]:
                max = num[i] + num[j]
            j -= 1
            

        return max






