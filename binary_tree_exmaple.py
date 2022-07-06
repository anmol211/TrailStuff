from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root: Node):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def preorder(root: Node):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)


def postorder(root: Node):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)


def height(root: Node):
    if root is None:
        return 0
    else:
        return 1 + max(height(root.left), height(root.right))


def print_node_at_k_level(root: Node, k):
    if root is None:
        return
    if k == 0:
        print(root.data)
    print_node_at_k_level(root.left, k - 1)
    print_node_at_k_level(root.right, k - 1)


def level_order(root):
    if root is None: return
    q = Queue()
    q.put(root)
    while not q.empty():
        curr: Node = q.get()
        print(curr.data)
        if curr.left:
            q.put(curr.left)
        if curr.right:
            q.put(curr.right)


def size(root):
    if root is None:
        return 0
    return 1 + size(root.left) + size(root.right)


def getMax(root: Node):
    if root is None:
        return -1
    return max(root.data, max(getMax(root.left), getMax(root.right)))


def print_left_view(root: Node):
    if root is None: return
    q = Queue()
    q.put(root)
    while not q.empty():
        count = q.qsize()
        for i in range(count):
            curr: Node = q.get()
            if i == 0:
                print(curr.data)
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)


def spiral_form(root: Node):
    if root is None: return
    q = Queue()
    q.put(root)
    while not q.empty():
        count = q.qsize()
        for i in range(count):
            curr: Node = q.get()
            print(curr.data)
            if i % 2 ==0:
                if curr.right:
                    q.put(curr.right)
                if curr.left:
                    q.put(curr.left)
            else:
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)


max_level = 0


def print_left_view_recur(root: Node, level):
    global max_level
    if root is None: return
    if max_level < level:
        print(root.data)
        max_level = level
    print_left_view_recur(root.left, level + 1)
    print_left_view_recur(root.right, level + 1)


def children_sum_property(root: Node):
    if root is None: return
    if root.left is None and root.right is None: return True
    children_sum = 0
    if root.left: children_sum += root.left.data
    if root.right: children_sum += root.right.data
    return root.data == children_sum \
           and children_sum_property(root.left) \
           and children_sum_property(root.right)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    # print("#####Inorder")
    # inorder(root)
    # print("#####Preorder")
    # preorder(root)
    # print("####PostOrder")
    # postorder(root)
    # print("###Height")
    # print(height(root))
    # print_node_at_k_level(root, 2)
    # print("######Level order")
    # level_order(root)
    # print_left_view_recur(root, 1)
    # print_left_view(root)
    #print(children_sum_property(root))
    spiral_form(root)
    '''
            8
        9       7
    2               1
    '''
