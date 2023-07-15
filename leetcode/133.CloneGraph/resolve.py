
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return node

        visited={}
        visited_copi={}

        def dfs(node):
            if node.val in visited_copi:
                return visited_copi[node.val]
            newnode = Node(node.val)
            visited[node.val] = node
            visited_copi[newnode.val] = newnode
            for n in node.neighbors:
                newnode.neighbors.append(dfs(n))
            return newnode

        return dfs(node)

def print_graph(node):
    """Print a graph starting from the given node"""
    
    visited = set()
    queue = [node]
    result = []
    while queue:
        node = queue.pop(0)
        if node.val not in visited:
            visited.add(node.val)
            # Add neighbors to the result
            result.append(sorted(neighbor.val for neighbor in node.neighbors))
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
    return result


def main():
    # Initialize a solution object
    sol = Solution()
    
    # Test Case 1: Test a graph with several nodes and connections
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    result1 = sol.cloneGraph(node1)
    # Here you should assert that the cloned graph has the same structure as the original one

    # Test Case 2: Test a graph with one node and no neighbors
    single_node = Node(1)
    result2 = sol.cloneGraph(single_node)
    # The cloned graph should only contain one node with no neighbors

    # Test Case 3: Test an empty graph
    empty_node = None
    result3 = sol.cloneGraph(empty_node)
    # The cloned graph should also be empty

    # Test Case 4: Test a graph where each node is connected to all other nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2]
    result4 = sol.cloneGraph(node1)
    # Here you should assert that the cloned graph has the same structure as the original one

    # Test Case 5: Test a graph with the maximum number of nodes
    nodes = [Node(i) for i in range(1, 101)]
    for i in range(100):
        nodes[i].neighbors = [nodes[j] for j in range(100) if j != i]
    result5 = sol.cloneGraph(nodes[0])
    # The cloned graph should also contain 100 nodes, each connected to all others
    
     # After each cloneGraph call, print the cloned graph
    if result1 is not None:
        print(print_graph(result1))
    if result2 is not None:
        print(print_graph(result2))
    if result3 is not None:
        print(print_graph(result3))
    if result4 is not None:
        print(print_graph(result4))
    """ if result5 is not None:
        print(print_graph(result5)) """


if __name__ == "__main__":
    main()
