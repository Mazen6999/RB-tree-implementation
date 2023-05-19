import sys
from tkinter import *

class Node():
    def __init__(self,val):
        self.val = val                                   # Value of Node
        self.parent = None                               # Parent of Node
        self.left = None                                 # Left Child of Node
        self.right = None                                # Right Child of Node
        self.color = 1                                   # Red Node as new node is always inserted as Red Node

# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL
        self.counter=0


    # Insert New Node
    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red

        testparent = None
        testnode = self.root

        while testnode != self.NULL :                           # Find position for new node
            testparent = testnode
            if node.val < testnode.val :
                testnode = testnode.left
            else :
                testnode = testnode.right

        node.parent = testparent
        if testparent == None :
            self.root = node
        elif node.val < testparent.val :                          # Check if it is right Node or Left Node by checking the value
            testparent.left = node
        else :
            testparent.right = node

        if node.parent == None :                         # Root node is always Black
            node.color = 0
            return

        if node.parent.parent == None :                  # If parent of node is Root Node
            return
        self.counter += 1
        self.fixInsert ( node )                          # Else call for Fix Up

    # Code for left rotate
    def LeftRotate (self, node) :
        child = node.right
        node.right = child.left
        if child.left != self.NULL :
            child.left.parent = node

        child.parent = node.parent
        if node.parent == None :
            self.root = child
        elif node == node.parent.left :
            node.parent.left = child
        else :
            node.parent.right = child
        child.left = node
        node.parent = child


    # Code for right rotate
    def RightRotate (self, node) :
        child = node.left
        node.left = child.right
        if child.right != self.NULL :
            child.right.parent = node

        child.parent = node.parent
        if node.parent == None :
            self.root = child
        elif node == node.parent.right :
            node.parent.right = child
        else :
            node.parent.left = child
        child.right = node
        node.parent = child


    # Fix Up Insertion
    def fixInsert(self, node):
        while node.parent.color == 1:                        # While parent is red
            if node.parent == node.parent.parent.right:         # if parent is right child of its parent
                uncle = node.parent.parent.left                  # Left child of grandparent
                if uncle.color == 1:                          # if color of left child of grandparent i.e, uncle node is red
                    uncle.color = 0                           # Set both children of grandparent node as black
                    node.parent.color = 0
                    node.parent.parent.color = 1             # Set grandparent node as Red
                    node = node.parent.parent                   # Repeat the algo with Parent node to check conflicts
                else:
                    if node == node.parent.left:                # If node is left child of it's parent
                        node = node.parent
                        self.RightRotate(node)                        # Call for right rotation
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.LeftRotate(node.parent.parent)
            else:                                         # if parent is left child of its parent
                uncle = node.parent.parent.right                 # Right child of grandparent
                if uncle.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    uncle.color = 0                           # Set color of childs as black
                    node.parent.color = 0
                    node.parent.parent.color = 1             # set color of grandparent as Red
                    node = node.parent.parent                   # Repeat algo on grandparent to remove conflicts
                else:
                    if node == node.parent.right:               # if node is right child of its parent
                        node = node.parent
                        self.LeftRotate(node)                        # Call left rotate on parent of node
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.RightRotate(node.parent.parent)              # Call right rotate on grandparent
            if node == self.root:                            # If node reaches root then break
                break
        self.root.color = 0                               # Set color of root as black
    # Function to transplant nodes

    # Function to print
    def __printCall ( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.val ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Function to call print
    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )

    def search(self, node, target):
        if node == self.NULL:
            return "NotFound"
        elif target == node.val:
            return "Found"
        elif target < node.val:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)

    def size(self):
        return self.counter

    def height(self, node):
        if node is self.NULL:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1
tree = RBTree()
def dictionary():
    file = open("EN-US-Dictionary.txt", "r")
    for i in file:
        i = i.strip('\n')
        tree.insertNode(i)
    file.close()
    tree.print_tree()
    print(tree.size())
    print(tree.height(tree.root))
def Gui_insert():
    start = Tk()
    start.minsize(100, 100)
    start.title("insertion")
    string1=tree.search(tree.root,value.get())
    string2="Found"
    if string1==string2:
        ML1 = Label(start, text="word already in tree") ## to check if the word is already in the tree
        ML1.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
            tree.insertNode(value.get())
            ML1 = Label(start, text="word Inserted")
            ML1.place(relx=0.5, rely=0.5, anchor=CENTER)
            print(tree.size())
            print(tree.height(tree.root))
    start.mainloop()
def Gui_size():
    start = Tk()
    start.minsize(100, 100)
    start.title("size")
    size= tree.size()
    ML1 = Label(start, text=size)
    ML1.place(relx=0.5, rely=0.5, anchor=CENTER)
    start.mainloop()

def Gui_height():
        start = Tk()
        start.minsize(100, 100)
        start.title("Height")
        height = tree.height(tree.root)
        ML2 = Label(start, text=height)
        ML2.place(relx=0.5, rely=0.5, anchor=CENTER)
        start.mainloop()

def Gui_search():
            start = Tk()
            start.minsize(100, 100)
            start.title("Search")
            searchword = tree.search(tree.root, value2.get())
            ML3 = Label(start, text=str(searchword))
            ML3.place(relx=0.5, rely=0.5, anchor=CENTER)
            start.mainloop()


top=Tk()
top.minsize(400, 400)
top.title("RB Trees")
Label1=Label(text="insert word")
Label1.pack()
value=StringVar()
Entry1=Entry(top,textvariable=value)
Entry1.pack()
Button1=Button(text="insert",command=Gui_insert)
Button1.pack()
Label2 = Label(text="Search word")
Label2.pack()
value2=StringVar()
Entry2 = Entry(top,textvariable=value2)
Entry2.pack()
Button2=Button(text="Search",command=Gui_search)
Button2.pack()
Button3=Button(text="Print Size",command=Gui_size)
Button3.pack()
Button4=Button(text="Print Height",command=Gui_height)
Button4.pack()
Button5=Button(text="load dictionary",command= dictionary)
Button5.pack()
top.mainloop()


