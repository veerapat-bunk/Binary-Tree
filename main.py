# create node binary tree
class Node:
    def __init__(self, data):
        self.data = data                              # store parameter (data)
        self.left = None                              # store parameter (left)
        self.right = None                             # store parameter (right)

# create store height
class height:
    def __init__(self):
        self.height = 0                              # set parameter height node

# function insert node data
def insert(node, data):
    # if root is None return 0
    if node is None:                                # check Empty root
        return Node(data)                           # return root node

    if data < node.data:                            # input data < node.data (check level 0++)
        node.left = insert(node.left, data)         # node.left and into recursive function insert (left,data) or .left
    elif(data > node.data):
        node.right = insert(node.right, data)       # node.right and into recursive function insert (right,data) or .right
    return node                                     # return node

# function min_valueNode
def min_valueNode(node):
    current = node                                 # set parameter current = node
    while (current.left is not None):
        current = current.left
    return current

# function deleter node
def deleteNode(root, data):
    # if root is None return 0
    if root is None:
        return root
    #check value node.data
    if data < root.data:                               # check node data < node.data
        root.left = deleteNode(root.left, data)        # node.left and into recursive function delete (left,data) or .left
    elif (data > root.data):                           # check node data > node.data
        root.right = deleteNode(root.right, data)      # node.right and into recursive function delete (right,data) or .right
    else:
        if root.left is None:                          # check root.left empty
            temp = root.right                          # set parameter temp = .right
            root = None
            return temp                                # return temp

        elif root.right is None:                       # check root.right empty
            temp = root.left                           # set parameter temp = .left
            root = None
            return temp                                # return temp
        temp = min_valueNode(root.right)               # input root.right into min_valueNode function and return store temp
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data) # input root.right and temp.data into deleteNode function and return root.right
    return root                                        # return root

# function height binary tree
def height(root):
    # if root is None return 0
    if root == None:
        return 0

    hleft = height(root.left)                             # set left subtree height
    hright = height(root.right)                           # set right subtree height

    if hleft > hright:                                    # height_left > height_right
        return hleft + 1                                  # height_left +1
    else:
        return hright + 1                                 # height_right +1

# function check height binary tree
def check_height():
    subtree_left = height(root.left)
    subtree_right = height(root.right)
    result = abs(subtree_right - subtree_left)                          # |height_left - height_right|
    print(f"Left subtree height:  {subtree_left}")                      # show Left subtree height
    print(f"Right subtree height: {subtree_right}")                     # show Right subtree height
    if (result <= 1):                                                   # check balanced tree
        print("\nThis binary Tree is balanced")                         # if balanced tree show text
    else:
        print("\nThis binary Tree isn't balanced")                      # if is not balanced tree show text
    return result                                                       # return height difference numeric value

def getLeafCount(node):
    if node is None:
        return 0
    if(node.left is None and node.right is None):
        return 1
    else:
        return getLeafCount(node.left) + getLeafCount(node.right)

def findParent(node: Node,val: int,parent: int) -> None:
    if (node is None):
        return

    if (node.data == val):
        print(f"Parent of the node {val} is {parent}")
    else:
        findParent(node.left,val, node.data)
        findParent(node.right,val, node.data)

child_list = []
def children(root):
	if root == None:
		return 0

	if root.left != None:
		child_list.append(root.left.data)
	elif root.right != None:
		child_list.append(root.right.data)
	return children(root.left), children(root.right)

sib_node = []
def sibling(root):
	if root == None:
		return 0

	if root.left != None and root.right != None:
		sib_node.append([root.left.data,root.right.data])
	return sibling(root.left), sibling(root.right)
# In-order traversal or Infix
# Left -> Root -> Right
def in_order(root):
    infix = []
    if root:
        infix = in_order(root.left)                                   # append left node
        infix.append(root.data)                                       # append root node
        infix = infix + in_order(root.right)                          # append right node
    return infix                                                      # return array infix

# set root node = none
root = None
# show commands
data_command = ["\nadd     : add node",
                "check   : Check Find",
                "delete  : delete node",
                "print   : show all_data",
                "exit    : exit process\n"]
while (True):                                                     # loop infinity process but input exit = end process
    for i in range(0, len(data_command)):                         # for-loop show data array command
        print(data_command[i])                                    # show command step by step
    command = input("Enter your command: ")
    if(command == 'add'):                                         # add data node
        print("Enter -> (cancel input node)")
        while(True):                                              # infinity add node but don't input = end add process
            n = input("Enter your number : ")                     # input type character
            if (n == ''):
                break
            else:
                n = int(n)                                        # transform data type character to integer
                root = insert(root, n)                            # input data into insert function
    elif(command == 'check'):
        number = int(input("Enter your number check parent: "))
        findParent(root, number, -1)
        print(f"Leaf count of the tree is {getLeafCount(root)}")
        children(root)
        print(f"Children root node : {child_list}")
        sibling(root)
        print(f"Sibing root node : {sib_node}")

    # show all_data {level, height, subtree, before-after node (print inorder travel) }
    elif(command == 'print'):
        print(f"\nBinary_Tree(Inorder Travel): {in_order(root)}")
        print(f"Level Binary: {height(root)-1}")
        print(f"\nHeight: {height(root)}")
        check_height()
        print("------------------------------------------------------\n")

    elif(command == 'delete'):
        number = int(input("Enter your number: "))
        deleteNode(root,number)
        print(f"Binary_Tree(Inorder Travel)(after): {in_order(root)}")
    elif(command == 'exit'):                                    # end all process
        break