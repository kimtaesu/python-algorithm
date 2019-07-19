# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printTree(self):
        print(self.val)
        if self.left:
            self.left.printTree()

        if self.right:
            self.right.printTree()


class Codec:
    def serialize(self, root):
        preorder = ''
        if not root:
            preorder += ',None'
            return preorder
        preorder += ',' + str(root.val)
        preorder += self.serialize(root.left)
        preorder += self.serialize(root.right)
        return preorder

    def deserialize(self, encode_data):
        pos = -1
        data = encode_data[1:].split(',')
        for i in range(len(data)):
            if data[i] == 'None':
                data[i] = None
            else:
                data[i] = int(data[i])
        root, count = self.buildTree(data, pos)
        return root

    def buildTree(self, data, pos):
        pos += 1
        if pos >= len(data) or data[pos] == None:
            return None, pos

        root = TreeNode(data[pos])
        root.left, pos = self.buildTree(data, pos)
        root.right, pos = self.buildTree(data, pos)
        return root, pos

# Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.deserialize(codec.serialize(root))
root = codec.deserialize("1,2,3,null,null,4,5")
codec.serialize(root)
