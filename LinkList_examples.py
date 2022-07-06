class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def push_at_end(self, data):
        node = Node(data)
        temp = self.head
        if not temp:
            self.head = node
        else:
            while temp.next:
                temp = temp.next
            temp.next = node

    def delete_first(self):
        if self.head is None:
            print("List empty")
        temp = self.head
        self.head = temp.next
        temp.next = None

    def delete_last(self):
        if self.head is None:
            print("List empty")
            return
        if self.head.next is None:
            print(f"removed {self.head.data}")
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None

    def print_link_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def insert_at(self, n, data):
        if self.head is None:
            print("List is Empty, Pushing the first element")
            self.push(data)
            return
        node = Node(data)
        place = 1
        temp = self.head
        while place < n and temp:
            temp = temp.next
            place += 1
        node.next = temp.next
        temp.next = node

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev

    def remove_duplicate(self):
        prev = self.head
        curr = self.head.next
        while curr:
            if prev.data == curr.data:
                temp = curr.next
                curr.next = None
                prev.next = temp
                curr = temp
                continue
            prev = curr
            curr = curr.next

    def detect_loop_and_remove(self):
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if slow != fast:
            return
        slow = self.head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None
        
link_list = LinkList()
link_list.push(3)
link_list.push(2)
link_list.push(2)
link_list.push(1)
#link_list.push_at_end(4)
link_list.print_link_list()
# link_list.delete_first()
#link_list.delete_last()
print("###")
#link_list.insert_at(1,5)
#link_list.reverse()
print(link_list.detect_loop())
link_list.print_link_list()
