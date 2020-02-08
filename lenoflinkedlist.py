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


    def len_cal(self):
        curr_node = self.head
        count = 0

        while curr_node != None:
            count +=1
            curr_node = curr_node.next

        return count    

    def len_cal_recursive(self, node):
       if node ==None:
           return 0
       else:
           return 1+self.len_cal_recursive(node.next)


        
            
li=Singlylinkedlist()
li.append("A")
li.append("B")
li.append("C")
li.append("D")

li.printlist()

print("lenth of linked list is = ", li.len_cal())

print("length calculated through recursive method =", li.len_cal_recursive(li.head))
