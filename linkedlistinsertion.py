class node:
    def __init__(self, data):
        self.data = data
        self.next = None



class Singlylinkedlist:
    def __init__(self):
        self.head = None


    def printlist(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next



    def append(self, data):
        new_node = node(data)


        if self.head ==None:
            self.head = new_node
            return


        last_node = self.head
        while last_node.next!=None:
            last_node = last_node.next

        last_node.next = new_node

    def preend(self, data):
        new_node = node(data)

        new_node.next = self.head
        self.head= new_node


    def insert_at_node(self, prev_node, data):
        new_node = node(data)

        if not prev_node:
            print("such node not exist")

        new_node.next = prev_node.next
        prev_node.next = new_node
            
li=Singlylinkedlist()
li.append("A")
li.append("B")
li.append("C")
li.append("D")
li.insert_at_node(li.head.next, "X")

li.preend("3")

li.printlist()
