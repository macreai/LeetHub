class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue:

    def __init__(self):
        self.first = None
        self.last = None

    def push(self, x: int) -> None:
        new_node = Node(x)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def pop(self) -> int:
        temp = self.first
        self.first = self.first.next
        temp.next = None
        return temp.value

    def peek(self) -> int:
        return self.first.value

    def empty(self) -> bool:
        if self.first is None:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()