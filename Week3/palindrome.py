

class Stack:
    
    def __init__(self):
        """No-Args Constructor, initialize the internal data with empty list
        """
        self.data = []
    
    def push(self, elem):
        """Adds the element to the top of the stack

        Args:
            elem ([type]): Element
        """
        self.data.append(elem)
    
    def pop(self):
        """Deletes the top most element of the stack and return it

        Returns:
            [type]: Removed element
        """
        if self.isEmpty():
            return None
        elem = self.data[-1]
        del self.data[-1]
        return elem
    
    def size(self):
        """Returns the size of the stack

        Returns:
            int: Stack's size
        """
        return len(self.data)
    
    def isEmpty(self):
        """Returns whether the stack is empty

        Returns:
            boolean: True if the stack is empty, False otherwise.
        """
        if self.size() == 0:
            return True
        else:
            return False
    
    def peek(self):
        """Returns a reference to the top most element of the stack value. Does not remove the element.

        Returns:
            [type]: Returns a ref to the item on top
        """
        if self.isEmpty():
            return None
        else:
            return self.data[-1]


class Queue:
    def __init__(self):
        """No-Args Constructor, initialize the internal data with empty list
        """
        self.data = []
    
    def enqueue(self, elem):
        """Adds the element 'e' to the queue.

        Args:
            elem ([type]): Element
        """
        self.data.append(elem)
    
    def dequeue(self):
        """Removes an item from the queue and return it.

        Returns:
            [type]: Removed element
        """
        if self.isEmpty():
            return None
        else:
            elem = self.data[0]
            del self.data[0]
            return elem
    
    def size(self):
        """Returns the size of the queue

        Returns:
            [type]: The size of the queue
        """
        return len(self.data)
    
    def isEmpty(self):
        """Returns whether the queue is empty

        Returns:
            boolean: True if the queue is empty, False otherwise.
        """
        if self.size() == 0:
            return True
        else:
            return False
    
    def peek(self):
        """Returns a reference to the front item in the queue. Does not remove the element.

        Returns:
            [type]: Return first element
        """
        if self.isEmpty():
            return None
        else:
            return self.data[0]
    
def isPalindrome(text: str):
    # Return True if the text is empty
    if (len(text) == 0):
        return True
    # Create empty stack and queue
    s = Stack()
    q = Queue()
    # Add all chars to the stack and queue
    for ch in text:
        s.push(ch)
        q.enqueue(ch)
    # Pop and dequeue from the stack and the queue respectively, 1 char at a time
    # Return False if any two elements in the same iteration are different
    for i in range(len(text)):
        if s.pop() != q.dequeue():
            return False
    # Return True if all chars are equal
    return True
 
# =============================================

print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))


"""
stk = Stack()
stk.push(2)
stk.push(1)
stk.push(2)
stk.push(5)

print(stk.data)
r = stk.pop()
print(r)
print(stk.data)
print("size: ", stk.size())

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.data)
r = q.dequeue()
print(r)
print(q.data)
"""

