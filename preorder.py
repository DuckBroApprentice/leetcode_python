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

#參考了一個想法很厲害
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root == None:
            return []
        
        #利用堆疊的思想
        stack = [root]
        #第一次處理時stack = [root{val,children[]}]
        #pop: stack = []
        #push: root.children with reverse : stack = [root.children[::-1]
        #先進後出才會正確順序
        res = []

        while stack :
            """
            第一次寫的是：
            res.append(stack.pop().val)
            stack.extend(root.children[::-1])
            這樣會造成記憶體溢出
            原因在於永遠在跑第一個root
            修改：
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])
            用list處理也要記得前進
            """
            root = stack.pop()
            res.append(root.val)
            stack.extend(root.children[::-1])

        return res