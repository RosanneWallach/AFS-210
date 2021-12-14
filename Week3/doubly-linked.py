class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count


    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.count += 1

    def addLast(self, data) -> None:
        # Add a node at the end of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1 
  

    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        
        
        # Not adding data if the index if out of bounds
        if index > self.count:
            return
        # Add to the last if index is equal to count
        if index == self.count:
            return self.addLast(data)
        # Add to the first if index is 0
        if index == 0:
            return self.addFirst(data)
        # create the new node
        new_node = Node(data)
        # Find the node at index
        idx = 0
        tmp = self.head
        while idx < index and tmp != None:
            tmp = tmp.next
            idx += 1
        tmp.prev.next = new_node
        new_node.next = tmp
        new_node.prev = tmp.prev
        tmp.prev = new_node
        self.count += 1


    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1    
        # init the index with 0
        idx = 0
        # Iterate over the nodes of the list
        for node_data in self.iter():
            # Check if the data is equal to the data from the node
            if node_data == data:
                return idx
            # increment the index at the end of each iteration
            idx += 1
        return -1

    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        curr = self.head
        prev = self.head

        for n in range(index):
            prev = curr
            curr = curr.next
            
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1

        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr


words = DoublyLinkedList()
words.add("May")
words.add("the")
words.add("Force")
words.add("be")
words.add("with")
words.add("you")
words.add("!")

print(words)

print(words.indexOf("with"))

words[5] = "us"

words.addAtIndex("all", 6)
print(words)