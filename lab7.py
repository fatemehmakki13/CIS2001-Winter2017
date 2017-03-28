class _Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
        self.size = 0

    def Add(self, element):
        if self.root is None:
            self.root = _Node(element)
        else:
            if element < self.root.value:
                leftTree = BinarySearchTree(self.root.left)
                leftTree.Add(element)
                self.root.left = leftTree.root
            elif element > self.root.value:
                rightTree = BinarySearchTree(self.root.right)
                rightTree.Add(element)
                self.root.right = rightTree.root
            else:
                raise ValueError("element already in tree")
        self.size += 1


    def Remove(self, element):
        if element == self.root.value:
            if self.root.left is None:
                self.root = self.root.right
            elif self.root.right is None:
                self.root = self.root.left
            else:
                new_root = self.root.right
                old_left = self.root.left
                farthest_left = new_root
                while farthest_left.left != None:
                    farthest_left = farthest_left.left
                farthest_left.left = old_left
                self.root.value = None
                self.root = new_root
                self.size -= 1
                return element
        elif element < self.root.value:
            leftTree = BinarySearchTree(self.root.left)
            removed = leftTree.Remove(element)
            self.root.left = leftTree.root
            if removed != None:
                self.size -= 1
            return removed
        else:
            rightTree = BinarySearchTree(self.root.right)
            removed = rightTree.Remove(element)
            self.root.right = rightTree.root
            if removed != None:
                self.size -= 1
            return removed

    def PrintInOrder(self):
        if self.root != None:
            leftTree = BinarySearchTree(self.root.left)
            leftTree.PrintPreOrder()
            print(self.root.value)
            rightTree = BinarySearchTree(self.root.right)
            rightTree.PrintPreOrder()



bst = BinarySearchTree()
bst.Add(20)

bst.Add(10)
bst.Add(30)

bst.Add(5)
bst.Add(15)
bst.Add(40)

bst.Add(16)
bst.Add(50)

bst.Add(60)

print(bst.Remove(60))
print(bst.Remove(10))

#bst.PrintInOrder()
