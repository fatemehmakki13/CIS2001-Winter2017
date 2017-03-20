class _Node:
    def __init__(self, value, next = None, previous = None):
        self.Value = value
        self.Next = next
        self.Previous = previous

class DoublyLinkedList():
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.Value

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not ( self == other )
    
    def __init__(self):
        self._head = _Node(None)
        self._head.Previous = self._head
        self._head.Next = self._head
        self._size = 0

    def __len__(self):
        return self._size

    def IsEmpty(self):
        return self._size == 0

    def Add(self, item, index = None):
        if index == None:
            new_node = _Node(item, self._head, self._head.Previous)
            self._head.Previous = new_node
            new_node.Previous.Next = new_node
        
        elif index > self._size or index < 0:
            raise IndexError()
        
        else:
            current_node = self._head
            for current_index in range(index):
                current_node = current_node.Next

            new_node = _Node(item,current_node.Next, current_node)
            new_node.Previous.Next = new_node
            new_node.Next.Previous = new_node

        self._size += 1

    def Get(self, index):
        if index >= self._size or index < 0:
            raise IndexError()

        current_node = self._head.Next
        for current_index in range(index):
            current_node = current_node.Next
        return current_node.Value


    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be a Position Type')
        if p._container is not self:
            raise ValueError('p does not beong to this container')
        if p._node.Next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        if node is self._head:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        return self._make_position(self._head.Next)

    def last(self):
        return self._make_position(self._head.Previous)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.Previous)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.Next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def add_first(self, e):
        self.Add(e, 0)
        return self._make_position(self._head.Next)

    def add_last(self, e):
        self.Add(e)
        return self._make_position(self._head.Previous)

    def add_before(self, p, e):
        original = self._validate(p)
        self._insert_between(e, original.Previous, original)
        return self._make_position(original.Previous)

    def add_after(self, p, e):
        original = self._validate(p)
        self._insert_between(e, original, original.Next)
        return self._make_position(original.Next)

    def delete(self, p):
        original = self._validate(p)
        original.Previous.Next = original.Next
        original.Next.Previous = original.Previous
        self._size -= 1
        value = original.Value
        original.Value = None
        original.Previous = None
        original.Next = None
        return value

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original.Value
        original.Value = e
        return old_value

    def _insert_between(self, e, previous, next):
        new_node = _Node(e, next, previous)
        previous.Next = new_node
        next.Previous = new_node
        self._size += 1


list = DoublyLinkedList()

list.Add(10)
list.Add(20)
list.Add(30)



current = list.first()
for number in range(11,20):
    current = list.add_after(current, number)


for item in list:
    print(item)

current = list.first()
while current is not None:
    print(current.element())
    current = list.after(current)
