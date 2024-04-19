class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, item):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        
        self.stack1.append(item)
        
        while self.stack2:
            self.stack1.append(self.stack2.pop())
    
    def dequeue(self):
        if not self.stack1:
            print("Queue is empty")
            return None
        
        return self.stack1.pop()
    
    def display(self):
        if not self.stack1:
            print("Queue is empty")
            return
        
        print("Elements in the queue are:", end=" ")
        for item in self.stack1[::-1]:
            print(item, end=" ")
        print()