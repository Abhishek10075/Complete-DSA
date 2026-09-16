#Pre Order Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        result=[]
        def preorder(node):
            if node is None:
                return 
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return result

'''
TC=o(n) where n is number of nodes in tree
SC=o(h) where h is height of tree
'''

#In order Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        result=[]
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)

        return result
        