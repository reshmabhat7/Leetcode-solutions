class MyQueue(object):

    def __init__(self):
        self.stack_in = []   # Stack to handle incoming elements
        self.stack_out = []  # Stack to reverse order for dequeue

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        self.move()
        return self.stack_out.pop()

    def peek(self):
        self.move()
        return self.stack_out[-1]

    def empty(self):
        return not self.stack_in and not self.stack_out

    def move(self):
        # Transfer from stack_in to stack_out only if stack_out is empty
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())   # Output: 1
print(myQueue.pop())    # Output: 1
print(myQueue.empty())  # Output: False

