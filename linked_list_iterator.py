

class LinkedList:
    def __init__(self, collection=None):
        self.head = None
        if collection:
            for item in reversed(collection):
                self.insert(item)
    
    def __str__(self):

        out = ""

        # for value in self:
        current = self.head
        while current:
            out += f"{{ {current.value} }} -> "
            current = current.next

        return out + "None"

    
    def __iter__(self):
        def value_generator():
            current = self.head

            while current:
                yield current.value
                current = current.next
        
        return value_generator()

    def __len__(self):
        return len(list(iter(self)))

    def __getitem__(self, index):
        if index < 0:
            raise IndexError

        for i, item in enumerate(self):
            if i == index:
                return item
        
        raise IndexError
    
    def insert(self, value):
        self.head = Node(value, self.head)

    def __eq__(self, other):
        return list(self) == list(other)

    

class Node:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next = next_

