class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def preorder(self, data):
        if data:
            print(data.data)
            self.preorder(data.left)
            self.preorder(data.right)

    def inorder(self, data):
        if data:
            self.inorder(data.left)
            print(data.data)
            self.inorder(data.right)

    def postorder(self, data):
        if data:
            self.postorder(data.left)
            self.postorder(data.right)
            print(data.data)

def main():

    data = Node(27)
    data.insert(14)
    data.insert(35)
    data.insert(10)
    data.insert(19)
    data.insert(31)
    data.insert(42)
    data.preorder(data)
    print("")
    data.inorder(data)
    print("")
    data.postorder(data)

main()