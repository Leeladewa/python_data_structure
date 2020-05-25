class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class singlylinkedlist():
    def __init__(self):
        self.head = None


    def print_list(self):
        curr_node = self.head
        while curr_node != None:
            print(curr_node.data)
            curr_node = curr_node.next


    def insert(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return


        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next

        curr_node.next = new_node

    def insert_at_position(self,data, pos):
        new_node = Node(data)
        curr_node = self.head
        if pos==0:
            new_node.next = curr_node
            self.head = new_node
            return
        if pos != 0:
            pos1 = 0
            
            curr_node = self.head
            while pos1 != pos:
                prev_node = curr_node
                pos1=pos1+1
                
                if curr_node == None:
                    print("Not possible to add node with none value")
                    return
                else:
                    curr_node = curr_node.next
            prev_node.next = new_node
            new_node.next = curr_node
        
            
    def insert_at_last(self, data):
        new_node = Node(data)
        curr_node = self.head
        while curr_node != None:
            prev_node = curr_node
            curr_node = curr_node.next

        prev_node.next= new_node
        new_node.next = curr_node
             
    def deletenode(self, data):
        curr_node = self.head
        while curr_node.data != data:
            prev_node = curr_node
            
            curr_node = curr_node.next

        prev_node.next = curr_node.next    
        
        
li = singlylinkedlist()
li.insert(2)
li.insert(4)
li.insert("C")
li.insert_at_position(1,0)
li.insert_at_position(3, 4)
li.insert_at_position("D",5)
li.insert_at_position(6,8)
print("linked list before deletion")
li.print_list()
li.deletenode(8)
print("linked list after deletion")
li.print_list()
