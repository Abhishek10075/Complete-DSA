#LeetCode 102 — Binary Tree Level Order Traversal 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        result=[]
        que=deque([])
        if root is None:
            return result
        que.append(root)
        while len(que)!=0:
            level=[]
            for _ in range(len(que)):
                e=que.popleft()
                level.append(e.val)
                if e.left is not None:
                    que.append(e.left)
                if e.right is not None:
                    que.append(e.right)
            result.append(level)
        return result

#Solve on geeksforgeeks

''' Structure of Binary Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def levelOrder(self, root):
        # code 
        result=[]
        que=deque([])
        if root is None:
            return result
        
        que.append(root)
        while len(que)!=0:
            e=que.popleft()
            result.append(e.data)
            
            if e.left is not None:
                que.append(e.left)
            if e.right is not None:
                que.append(e.right)
            
        return result