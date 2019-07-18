# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        root = TreeNode(S[0])
        depth = 0
        index = 1
        self.preorderTree(S, index, depth, root)
        # Print the Tree
        self.printTree(root)

    def printTree(self, node):
        if node.left:
            self.printTree(node.left)
        print(node.val)
        if node.right:
            self.printTree(node.right)

    def preorderTree(self, S: str, index, depth, root: TreeNode):
        childDepth = 0
        while S[index] == '-':
            index += 1
            childDepth += 1

        if depth > childDepth or childDepth == 0:
            return index

        node = TreeNode(S[index])
        if not root.left:
            root.left = node
        else:
            root.right = node
        index += 1
        self.preorderTree(S, index, childDepth, node)
        self.preorderTree(S, index, childDepth, node)


Solution().recoverFromPreorder("1-2--3--4-5--6--7")
