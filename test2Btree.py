class Node:
    def __init__(self, val, left = None ,right = None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def printNode(node):
        if node is None:
            return
        Node.printNode(node.left)
        Node.printNode(node.right)
        print(node.val)
            
    def parseStr(values)
def main():
    node = Node(1, Node(2), Node(3))
    Node.printNode(node)


main()
