class Stack:
    def __init__(self):
        self.stack = []
        self.undo_stack = []
    def put(self,value):
        self.stack.append(value)
    def remove(self):
        if not self.isEmpty():
            val = self.stack.pop()
            self.undo_stack.append(val)
            return val
        
        else:
            print("Stack is Empty")
            return None
    def peek_item(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            print("Stack is Empty no item")
            return None 
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    def len_stack(self):
        return len(self.stack)
    def display(self):
        print("Stack is in this format:-")
        for i in self.stack:
            print(i)
    def undo(self):
        if self.undo_stack:
            val = self.undo_stack.pop()
            self.stack.append(val)
            print(f"Undo: Restored {val}")
        else:
            print("Nothing to undo")
    
if __name__ == "__main__":
    s = Stack()
    for i in range(10,100,10):
        s.put(i)
    print(s.remove())
    print(s.remove())
    print(s.peek_item())
    print(s.undo())
    print(s.len_stack())
    print(s.display())


        
