class Node:
    '''
        singlely linked list node
    '''
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

# node_one = Node(1, None)
# # print(node_one)
# # manually inserting nodes
# node_two = Node(2, None)
# node_one.next = node_two
# print(f'first node: {node_one} second node: {node_one.next}')

class LinkedList:
    '''
        singlely linked list manager class
    '''
    def __init__(self):
        # lists start out empty
        self.head = None
        self.tail = None
        # how many nodes exists in the list
        self.size = 0

    def __len__(self):
        # len(list) -> size of the list
        return self.size
    
    def __str__(self):
        # return a meaningful string representation of our list
        # iterate over the list, concatenate every node's value into a string
        # if the list if empty, we will just return empty
        if len(self) == 0:
            return '[]'
        
        # the current node
        current_node = self.head
        string = str(current_node)
        # while the current node has a next value
        while current_node.next:
            # business logic of the loop -- adding current node's value to our return string
            string += f' -> {str(current_node.next)}'
            # the current node to be the current node's next
            current_node = current_node.next
        
        return f'[ {string} ]'

    def insert_front(self, data):
        '''
            create a new node and place it at the front of the list
        '''
        # if this is the first thing in the list
        if len(self) == 0:
            # set the new node to be both the head and the tail of the list
            self.head = Node(data, None)
            self.tail = self.head
        # replace the head with the new node
        else:
            new_node = Node(data, self.head)
            self.head = new_node
        # increment the size of our list
        self.size += 1

    def insert_end(self, data):
        '''
            create a new node and place it at the end of the list
        '''
        if self.size == 0:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            end = self.tail
            self.tail = Node(data, None)
            end.next = self.tail
        self.size += 1

    def insert_after(self, data, node_data):
        '''
            search for a node, and insert a new node after it
        '''
        after_node = None
        current = self.head
        while current:
            if current.data == node_data:
                after_node = current
                break
            current = current.next
        if after_node == None:
            return 'check your node_data, we couldn\'t find it!'
        newNode = Node(data, after_node.next)
        after_node.next = newNode
        self.size += 1

    

my_list = LinkedList()
my_list.insert_front(5)
my_list.insert_front(4)
my_list.insert_front(3)
my_list.insert_front(2)
my_list.insert_front(1)
my_list.insert_end(6)
my_list.insert_after(7, 6)
my_list.insert_after(8, 7)
print(f'head: {my_list.head}, tail: {my_list.tail}, head.next: {my_list.head.next}')
print(my_list)
print(len(my_list))