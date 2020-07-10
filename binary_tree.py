class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order_printing_oneline(root):
    if root is not None:
        que = []
        que.append(root)

        while(len(que)>0):
            tmp = None
            curr = que.pop(0)
            print(curr.data, end=" ")
            if curr.left is not None:
                que.append(curr.left)
            if curr.right is not None:
                que.append(curr.right)



root = Node(1)
root.left =  Node(2)
root.right =  Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(9)
root.left.left.left = Node(8)

print("level order printing in one line\n")
level_order_printing_oneline(root)

def level_order_printing_levelwise(root):
    if root is not None:
        que = []
        que.append(root)

        while(que):
            count = len(que)
            while count>0:
                curr = que.pop(0)
                print(curr.data, end = " ")
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)
                count = count - 1
            print(" ")

print("\n")
print("level order printing levelwise \n")
level_order_printing_levelwise(root)
         
def maximum_depth(root):
    if root is None:
        return 0
    else:
        lheight = maximum_depth(root.left)
        rheight = maximum_depth(root.right)

        return 1+max(lheight, rheight)


def minimum_depth(root):
    
    if root is None:
        return 0
    else:
        lheight = minimum_depth(root.left)
        rheight = minimum_depth(root.right)

        return 1+min(lheight, rheight)

print("maximum depth of binary tree ", maximum_depth(root))
print("\n")
print("minimum depth of binary tree ", minimum_depth(root))


def top_view(root):
    dict1 = {}
    node_dict = {}
    que = []
    que.append(root)
    node_dict[root.data] = 0
    while(len(que)>0):
        tmp = []
        curr = que.pop(0)
        if curr is not None:
            level = node_dict[curr.data]
            if level not in dict1:
                tmp.append(curr.data)
                dict1[level] = tmp

            if curr.left is not None:
                left_node = curr.left
                que.append(left_node)
                node_dict[left_node.data]=node_dict[curr.data]-1

            if curr.right is not None:
                right_node = curr.right
                que.append(right_node)
                node_dict[right_node.data]= node_dict[curr.data]+1
    print(dict1)
print("\n")
print("Top View of a Binary Tree ")
top_view(root)

def get_mirror(root):
    if root is None:
        return

    get_mirror(root.left)
    get_mirror(root.right)
    tmp = root.left
    root.left = root.right
    root.right = tmp
    
def inorder(root):
    if root == None:
        return
    else:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

print("inorder print of binary tree" , inorder(root))
print("\n")
get_mirror(root)
print("mirror view of binary tree", inorder(root))


def kth_distance(root, distance):
    if root is not None:
        if distance is 1:
            print(root.data, end=" ")
        else:
            kth_distance(root.left, distance-1)
            kth_distance(root.right, distance-1)


print('\n')
print("nodes at kth distance from root are ", kth_distance(root, 1))



def diagonal_view(root):
    if root is not None:
        que = []
        que.append(root)
        node_dict = dict()
        dict1 = dict()
        node_dict[root.data] = 0
        while(len(que)>0):
            tmp = []
            curr = que.pop(0)
            if curr is not None:
                level = node_dict[curr.data]
                if level  in dict1:
                    tmp = dict1.get(level)
                    tmp.append(curr.data)
                else:
                    tmp.append(curr.data)
                    dict1[level]=tmp

                if curr.left is not None:
                    left_node = curr.left
                    que.append(left_node)
                    node_dict[left_node.data]=node_dict[curr.data]+1

                if curr.right is not None:
                    right_node = curr.right
                    que.append(right_node)
                    node_dict[right_node.data]=node_dict[curr.data]

        print(dict1)


print("\n")
print("diagonal view of binary tree")
diagonal_view(root)

def vertical_order_traversal(root):
    if root is not None:
        que = []
        que.append(root)
        node_dict = dict()
        dict1 = dict()
        node_dict[root.data] = 0
        while(len(que)>0):
            tmp = []
            curr = que.pop(0)
            if curr is not None:
                level = node_dict[curr.data]
                if level  in dict1:
                    tmp = dict1.get(level)
                    tmp.append(curr.data)
                else:
                    tmp.append(curr.data)
                    dict1[level]=tmp

                if curr.left is not None:
                    left_node = curr.left
                    que.append(left_node)
                    node_dict[left_node.data]=node_dict[curr.data]-11

                if curr.right is not None:
                    right_node = curr.right
                    que.append(right_node)
                    node_dict[right_node.data]=node_dict[curr.data]+1

        print(dict1)

print("\n\n\n")
print("vertical order traversal of binary tree")
vertical_order_traversal(root)
            
def preorder(root):
    if root is None:
        return 
    else:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
 
print("\n\n\n")
print("preorder traversal of binary tree")
preorder(root)
  
def postorder(root):
   if root is None:
        return 
    else:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")
        
print("\n\n\n")
print("postorder traversal of binary tree")
postorder(root)        
 
