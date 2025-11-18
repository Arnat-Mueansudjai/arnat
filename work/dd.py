import statistics

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, root):
        values = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                values.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        left  = min(values)
        right = max(values)
        val   = statistics.median(values)

        return f"\tRoot: {val}\nLeft: {left}\t\tRight: {right}"

p = TreeNode(1, TreeNode(2), TreeNode(3))

i = Solution()
print(i.isSameTree(p))
