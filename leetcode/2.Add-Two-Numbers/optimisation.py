# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)  # Tête factice pour commencer la liste
        current_node = head  # Pointeur vers le dernier nœud inséré
        carry = 0  # Pour stocker la retenue de l'addition

        while l1 is not None or l2 is not None:
            # Utilisez la valeur du nœud si disponible, sinon utilisez 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculez la somme et la retenue
            sum_val = val1 + val2 + carry
            carry, val = divmod(sum_val, 10)
            
            # Créez un nouveau nœud pour la valeur et ajoutez-le à la fin de la liste
            current_node.next = ListNode(val)
            current_node = current_node.next
            
            # Avancez les pointeurs si possible
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Si il y a encore une retenue à la fin, créez un nouveau nœud
        if carry > 0:
            current_node.next = ListNode(carry)
        
        return head.next  # Renvoyez le premier vrai nœud (pas la tête factice)

def main():
    # Test avec les cas limites
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next

if __name__ == "__main__":
    main()
