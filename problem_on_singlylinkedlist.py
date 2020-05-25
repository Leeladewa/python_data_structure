#################PROBLEM == 1 #########################
######INSERT A NODE AT TAIL OF GIVEN LINKED LIST#######

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    curr_node = head
    if head == None:
        head = new_node
        return head
    
    curr_node = head
    while curr_node.next != None:
        curr_node = curr_node.next
    curr_node.next = new_node           
    return head

if __name__ == '__main__':
    fptr = open("hackerrank_test.txt", 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()


#############################PROBLEM ==2#####################
######## INSERT A NODE AT HEAD OF GIVEN LINKED LIST##########
    
import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function beloW
def insertNodeAtHead(llist, data):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    if llist == None:
        llist = new_node
        return llist
    
    curr_node = llist
    if curr_node != None:
        new_node.next = curr_node
        llist = new_node
        return llist    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    
    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')
    
    fptr.close()

###########################PROBLEM == 3 ####################
########INSERT A NODE AT SPECIFIC POSITION IN GIVEN LINKED LIST ###########
    
# Complete the insertNodeAtPosition function below
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)
    if position == 0:
        new_node.next = head
        head = new_node
        return head

    
    
    if position != 0:
            pos1 = 0
            
            curr_node = head
            while pos1 != position:
                prev_node = curr_node
                pos1=pos1+1
                
                if curr_node == None:
                    print("Not possible to add node with none value")
                    return
                else:
                    curr_node = curr_node.next
            prev_node.next = new_node
            new_node.next = curr_node
            return head
          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())



###################PROBLEM == 4################################
#######DELETE A NODE AT GIVEN POSITION OF LINKED LIST##########


# Complete the deleteNode function below.

def deleteNode(head, position):
    curr_node = head
    if position == 0:
        head = curr_node.next
        curr_node = None
        return head
    if position != 0:
        pos = 0
        while pos != position:
            prev_node = curr_node
            pos = pos+1
            curr_node = curr_node.next
        prev_node.next = curr_node.next
        curr_node = None
        return head    


if __name__ == '__main__':

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
##################PROBLEM == 5 ############################
#########PRINT REVERSE ORDER OF LINKED LIST ###############    
def reversePrint(head):
    curr_node = head
    x = []
    if curr_node == None:
        print("")
    else:
        while curr_node != None:
            x.append(curr_node.data)
            curr_node = curr_node.next
        for i in range(-1, -(len(x)+1), -1):
            print(x[i], end="\n")


if __name__ == '__main__':
    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        reversePrint(llist.head)


################################ PROBLEM == 6 ##############################
############## PRINT NODE VALUE FROM GIVEN TAIL POSITION ######################

def getNode(head, positionFromTail):
    curr_node = head
    curr_node1 = curr_node
    x= 0
    while curr_node1:
        x += 1
        curr_node1 = curr_node1.next
    pos = x- positionFromTail
    
    if pos == 0 or pos == 1:
        print(curr_node.data)
    
    else :
        pos1 = 1
        while pos1 != pos:
            pos1 += 1 
            curr_node = curr_node.next
         print(curr_node.data)


#################### PROBLEM == 7 ###################################
################ COMPARE TWO LINKED LIST #######################


import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below

def compare_lists(llist1, llist2):
    curr_node1 = llist1
    curr_node2 = llist2
    list1 = []
    list2 = []
    count  = 0
    while curr_node1:
        list1.append(curr_node1.data)
        curr_node1 = curr_node1.next

    while curr_node2:
        list2.append(curr_node2.data)
        curr_node2 = curr_node2.next

    if len(list1)!=len(list2):
        return 0
    if len(list1)==len(list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return 0 
                break
            else :
                count += 1
    if count == len(list1):
        return 1
    else : 
        return 0            

########################### PROBLEM == 8 ###################
################## REVERSE THE LINKED LIST #################

ef reverse(head):
    curr_node = head
    prev = None
    while curr_node :
        
        nxt = curr_node.next
        curr_node.next = prev
        prev = curr_node
        curr_node = nxt

    head = prev
    return head 
