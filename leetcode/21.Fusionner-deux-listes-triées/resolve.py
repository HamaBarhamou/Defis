# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None and list2 is None: return None
        elif list1 is None: return list2
        elif list2 is None: return list1

        teteListe = None

        if list1.val < list2.val:
            ele = list1
            list1 = list1.next
        else:
            ele = list2
            list2 = list2.next

        teteListe = ele
        queueListe = ele

        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                ele = list1
                list1 = list1.next
            else:
                ele = list2
                list2 = list2.next
            ele.next = None
            queueListe.next = ele
            queueListe = ele

        if list1 is not None:
            queueListe.next = list1
        elif list2 is not None:
            queueListe.next = list2

        return teteListe



def main():
    # Test case 1 : les deux listes contiennent des valeurs
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    sol = Solution()
    result = sol.mergeTwoLists(l1, l2)
    print_nodes(result)  # Affiche : 1 -> 1 -> 2 -> 3 -> 4 -> 4

    # Test case 2 : une des listes est vide
    l1 = None
    l2 = ListNode(0)
    result = sol.mergeTwoLists(l1, l2)
    print_nodes(result)  # Affiche : 0

    # Test case 3 : les deux listes sont vides
    l1 = None
    l2 = None
    result = sol.mergeTwoLists(l1, l2)
    print_nodes(result)  # Ne devrait rien afficher

def print_nodes(node: ListNode) -> None:
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next

if __name__ == "__main__":
    main()
