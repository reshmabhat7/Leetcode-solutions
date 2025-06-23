from collections import deque

class MyStack(object):

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        self.queue2.append(x)  # Push to the second queue
        while self.queue1:
            self.queue2.append(self.queue1.popleft())  # Move all elements to queue2
        self.queue1, self.queue2 = self.queue2, self.queue1  # Swap queues

    def pop(self):
        return self.queue1.popleft() if self.queue1 else None

    def top(self):
        return self.queue1[0] if self.queue1 else None

    def empty(self):
        return not self.queue1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())    # Output: 2
print(myStack.pop())    # Output: 2
print(myStack.empty())  # Output: False

