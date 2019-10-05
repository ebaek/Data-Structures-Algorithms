# 173: Binary Search Iterator


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.my_iter = self.inorder(root)
        self.next_small = next(self.my_iter)

    def inorder(self, root):
        current = root
        stack = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                yield current.val
                current = current.right
            else:
                yield None

    def next(self) -> int:
        tmp = self.next_small
        self.next_small = next(self.my_iter)
        return tmp

    def hasNext(self) -> bool:
        return True if self.next_small != None else None

     


a = TreeNode(3)
b = TreeNode(7)
b.left = a
e = TreeNode(20)
c = TreeNode(15)
d = TreeNode(9)
b.right = c
c.left = d
c.right = e

iterator = BSTIterator()
stac = iterator.initializeStack(b)
print(stac)




