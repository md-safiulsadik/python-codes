class Node:

    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        count = 0
        current = self.head
        
        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return f"{current.data} found !"
            else:
                current = current.next_node
        return f"'{key}' not in data !"

    
    def insert(self, data, index):
        if index == 0:
            self.add(data)

        if index > 0:
            new_data = Node(data)
            position = index
            current = self.head


            while position > 1:
                current = current.next_node
                position -= 1
            
            previous = current
            Next = current.next_node

            previous.next_node = new_data
            new_data.next_node = Next

    def remove(self, key):
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

    # This is newly added
    
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
        current = self.head
        nodes = []

        while current:
            if current == self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node == None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
            current = current.next_node
                
        return f"{' -> '.join(nodes)}"
        

# l = LinkedList()

# l.add(1)
# l.add(2)
# l.add(3)
# l.add(4)
# l.add(5)
# l.add(6)

# l.insert("data", 3)
# result = l.search(48)

# print(l)
# # l.remove(1)
# l.remove(6)
# print(l)

# # print(result)