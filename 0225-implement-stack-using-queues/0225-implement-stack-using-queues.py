class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyStack:

    def __init__(self):
        self.last = None

    def push(self, x: int) -> None:
        new_node = Node(x)
        if self.last is None:
            self.last = new_node
        else:
            new_node.next = self.last
            self.last = new_node

    def pop(self) -> int:
        temp = self.last
        self.last = self.last.next
        temp.next = None
        return temp.value


    def top(self) -> int:
        return self.last.value

    def empty(self) -> bool:
        if self.last is None:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()