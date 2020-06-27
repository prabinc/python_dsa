class DoubleNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DLinkedList:
    def __init__(self):
        self.head = DoubleNode(0, 0)
        self.tail = DoubleNode(0, 0)

    def append_left(self, node):
        if self.head is None:
            self.head = node
            self.tail = self.head
            return
        self.head.prev = node
        self.head.prev.next = self.head
        self.head = self.head.prev

    def pop(self, node):
        if self.head is None:
            return
        self.tail.prev = self.tail.next

    def move_to_front(self, node):
        # if its head- return
        if node.prev is None:
            return
        # if its middle node, remove the node and add as head.
        elif node.prev != None and node.next != None:
            node.prev.next = node.next
            self.head.prev = node
            node.next = self.head
            self.head = node
        # if its tail, remove and add as head
        else:
            self.tail.prev.next = None

    # def delete(self, node):
    #     if node.prev is None:


class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.cache = dict()
        self.tracker = DLinkedList()
        self.size = 0

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            # bring the node to the front of the list
            node = self.cache[key]
            self.tracker.move_to_front(node)
            return node.value

        # if item not present return -1
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.size < self.capacity:
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                self.tracker.move_to_front(node)
                return node.value
            else:
                node = DoubleNode(key, value)
                self.cache[key] = node
                self.tracker.append_left(node)
                self.size += 1
        # if capacity full, find the last node and delete it from the cache and the linkedlist
        last_node = self.tracker.tail
        last_node_key = self.tracker.tail.key
        self.cache.pop(last_node_key)
        self.tracker.pop(last_node)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)  # returns 1
our_cache.get(2)  # returns 2
our_cache.get(3)  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(
    3
)  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
