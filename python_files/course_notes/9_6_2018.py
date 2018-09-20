# a is a node that contains data and points too another node
# that also contains data
# first is the head and last node is the tail
# all nodes contain both a data part and pointer to the next node


# Linklists
#-------------------------------------------------------------------------------

# Great for connecting multiple datasources
class LinkedNode():
    def __init__(self, payload, nextnode=None):
        self._dataload = payload
        self._nextnode = nextnode

node1 = LinkedNode('Chris')
node2 = LinkedNode('Steve')
node3 = LinkedNode('Tom')
node4 = LinkedNode('teaches')
node5 = LinkedNode('python')

node1._nextnode = node2
node2._nextnode = node3
node3._nextnode = node4
node4._nextnode = node5

current_node = node1
while True:
    print(current_node._dataload, '->', end=' ')
    if current_node._nextnode is None:
        print('None')
        break
    current_node = current_node._nextnode

# Re-doing the above in a better way
class LinkedNode():
    def __init__(self, payload, nextnode=None):
        self._dataload = payload
        self._nextnode = nextnode

class LinkedList():
    def __init__(self, head=None):
        self._head = head

    def insert(self, payload):
        node = LinkedNode(payload)
        if self._head is None:
            self._head = node
            return
        current_node = self._head

        while True:
            if current_node._nextnode is None:
                current_node._nextnode = node
                break
            current_node = current_node._nextnode

    def print_linked_list(self):
        current_node = self._head
        while current_node is not None:
            print(current_node._dataload)
            current_node = current_node._nextnode
        print('None')

n1 = LinkedList()
n1.insert('Chris')
n1.insert('Tom')
n1.insert('Phil')
n1.insert('Pete')
n1.insert(3)

n1.print_linked_list()

print(n1._head._dataload)
