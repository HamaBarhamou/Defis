# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution(object):

    def insertion_queue(self, tete, noeud):
        if tete is None: return noeud
        ptr = tete
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = noeud
        return tete

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        somme = None
        ptr1 = l1
        ptr2 = l2
        r = 0
        while ptr1 is not None and ptr2 is not None:
            s = (ptr1.val + ptr2.val + r)
            u = s%10
            noeud = ListNode(u)
            somme = self.insertion_queue(somme, noeud)
            r = int(s/10)
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        if ptr1 is not None:
            ptr = ptr1
        elif ptr2 is not None:
            ptr = ptr2
        else:
            ptr = None

        while ptr is not None:
            s = ptr.val + r
            u = s%10
            noeud = ListNode(u)
            somme = self.insertion_queue(somme, noeud)
            r = int(s/10)
            ptr = ptr.next
        
        if r != 0:
            noeud = ListNode(r)
            somme = self.insertion_queue(somme, noeud)
                 
        return (somme)

def main():
    # Test avec les cas limites
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=' ')
        result = result.next

if __name__ == "__main__":
    main()