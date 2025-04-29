
class Node:
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self) -> str:
        return f"<Node data: {self.data}>"

class LinkedList:
    """
    Singly linked list
    """
    def __init__(self) -> None:
        self.head = None
    
    def add(self, data):
        """
        Adds a new node at the head of the list
        Takes O(1)
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Return the number of nodes in the list
        Takes O(n) time
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Return the node or 'None' if not found

        Takes O(n) time
        """

        current = self.head

        while current:
            if current.data == key:
                return f"{current}"
            else:
                current = current.next_node
        
        return f"'{key}' not in the list"

    def insert(self, data, index):
        """
        Inserts a new Node containing data at the index posiotion
        Insertion thakes O(1) time 
        but finding the node at the insertoin point takes O(n)

        So, overall takes O(n)
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new_node = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = current.next_node
                position -= 1

            previous = current
            next_node = current.next_node

            previous.next_node = new_node
            new_node.next_node = next_node

        return current
    
    def remove(self, key):
        """
        Remove Node containing data that mathches the key
        Returns the node or None if key doesn,t exsit
        Takes O(n) time
        """

        current = self.head
        previous = None

        while current:
            if current.data == key:
                if previous:
                    previous.next_node = current.next_node
                else:
                    self.head = current.next_node
                    
                return current

            previous = current
            current = current.next_node


    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1
                
            return current


    def __repr__(self) -> str:
        """
        Returns a string representation of the list
        Takes O(n) time
        """

        nodes = []
        current = self.head

        while current:

            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
            
            current = current.next_node

        return f"{'-> '.join(nodes)}"

        

# l = LinkedList()

# l.add(1)
# l.add(2)
# l.add(3)
# l.add(4)
# l.add(5)
# l.add(6)

# l.insert(3.5, 4)

# result = l.search(45)
# print(result)

# print(l)
# l.remove(3)
# print(l)

