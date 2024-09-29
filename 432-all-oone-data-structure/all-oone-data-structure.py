class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node_map = {} 

    def _add_node(self, prev_node, freq):
        new_node = Node(freq)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node
        return new_node

    def _remove_node_if_empty(self, node):
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.key_node_map:
            current_node = self.key_node_map[key]
            current_node.keys.remove(key)

            next_freq = current_node.freq + 1
            next_node = current_node.next

            if next_node == self.tail or next_node.freq != next_freq:
                next_node = self._add_node(current_node, next_freq)

            next_node.keys.add(key)
            self.key_node_map[key] = next_node
            self._remove_node_if_empty(current_node)
        else:
            first_node = self.head.next
            if first_node == self.tail or first_node.freq != 1:
                first_node = self._add_node(self.head, 1)
            first_node.keys.add(key)
            self.key_node_map[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.key_node_map:
            return

        current_node = self.key_node_map[key]
        current_node.keys.remove(key)

        if current_node.freq == 1:
            del self.key_node_map[key]
        else:
            prev_freq = current_node.freq - 1
            prev_node = current_node.prev

            if prev_node == self.head or prev_node.freq != prev_freq:
                prev_node = self._add_node(current_node.prev, prev_freq)

            prev_node.keys.add(key)
            self.key_node_map[key] = prev_node

        self._remove_node_if_empty(current_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))
    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))