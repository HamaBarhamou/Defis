# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Initialisation d'un noeud factice pour le début de la liste.
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attacher le reste de la liste non vide
        current.next = list1 if list1 else list2

        return dummy.next


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
