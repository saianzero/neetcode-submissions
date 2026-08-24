class LRUCache:
    class Node: # DLL
        def __init__(self, key, value):
            self.key =  key
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key --> Node

        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node: "Node") -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
    
    def add_node_to_front(self, node: "Node") -> None:
        front_node = self.head.next

        node.next = front_node
        node.prev = self.head

        self.head.next = node
        front_node.prev = node

        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]

        self.remove_node(node)
        self.add_node_to_front(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove_node(node)
            self.add_node_to_front(node)
            return
        
        if len(self.cache) == self.capacity:
            lru_node = self.tail.prev
            self.remove_node(lru_node)
            del self.cache[lru_node.key]
        
        new_node = self.Node(key, value)
        self.add_node_to_front(new_node)
        self.cache[key] = new_node






















        
