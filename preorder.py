"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None:
            return res
        res.append(root.val)
        for _,next in enumerate(root.children):
            res.extend(self.preorder(next))
        
        return res

#runtime 47ms Memory 15.58MB