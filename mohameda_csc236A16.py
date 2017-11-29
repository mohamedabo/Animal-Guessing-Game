# Abdirahman Mohamed CSC 236 A16
# Credits: Alex Sharron
import sys

class BST:
    """Initializes the Binary Tree"""
    def __init__(self):
        self.data= None
        self.left = None
        self.right =None

def make_a_question(node,file):
    """Reads the file and distinguishes between question and guess """
    line = file.readline() # reads the line
    if line=="Question:\n":
        line = file.readline()
        node = BST() # bst class object
        node.data = line
        node.left = make_a_question(node.left,file) # recursive call to insert question to left
        node.right = make_a_question(node.right,file) # recursive call to insert question to right
        return node
    else: # if it is a guess
        node = BST()
        line = file.readline()
        node.data = line
        return node

def preorder(head):
    """Arranges the data in preorder"""
    if head  == None:
        return
    preorder(head.left) #recursive call to left
    preorder(head.right) #recursive call to right

def animalguess(node):
    """The animal guess game. It asks user input and if it is yes it will start over and
    if it is no it will ask for the question and guess and added it to the original tree"""
    a = input(node.data)
    if a=="yes":
    #if the user says yes
        if node.right.right==None and node.right.left==None: # The base case for the right node
            ans = input("is it" + node.right.data + "?") #Aska question to the user and he inputs yes or no
            if ans=="yes": # if the answer is yes
                print("I knew it! Hahahahahahah!")
            # if they answer no
            else:
                questionNode = BST() # new bst object for the new question
                animalNode = BST() #new bst object for the new guess
                questionNode.data = input("What is the question that would distinguish that animal?")
                animalNode.data = input("What is the animal you were thinking of?")
                node.right = questionNode # the right node will point to the question
                node.right.right = animalNode # the child of the right node would be the animal
        else:

            animalguess(node.right) # if the right node is not none we recursivly call the right node

        #When the user says no
    else:
        if node.left.right==None and node.left.left==None: # The base case for the  left node
            ans = input("is it" + node.left.data + "?") #Aska question to the user and he inputs yes or no
            if ans=="yes": # if the answer is yes
                print("I knew it! Hahahahahahah!")

            # if they answer no
            else:
                questionNode = BST()
                animalNode = BST()
                questionNode.data = input("What is the question that would distinguish that animal?")
                animalNode.data = input("What is the animal you were thinking of?")
                node.left = questionNode # the left node would be the new question
                node.left.left = animalNode # the child of the left node would be the animal
        else:
            animalguess(node.left) # if the left node is not none we recursivly call the left node
def write_newtree(node,text):
    """Writes the tree to a new file"""
    if node.left!=None: # if the left node is not equal to none
        text.write("Question:\n") # write the question
        text.write(node.data) # write the data
        write_newtree(node.left,text) # recursivly call to insert question to the left node
        write_newtree(node.right,text) # recursivly call to insert question to the right node
        return node # updating node

    else: # if the left node is equal to none
        text.write("Guess:\n") # write the guess
        text.write(node.data) # write the data
        return node # updating node

def main():
    """The animal guess game. It asks user input and if it is yes it will start over and
    if it is no it will ask for the question and guess and added it to the original tree. User can play again of exit
    if the player exits, it will save the tree to a new file"""
    node = None
    file = open("animals.txt","r") # opening the file
    text = open("output.txt","w") # writing to a new file
    node = make_a_question(node,file) # node equals the insert function
    preorder(node)
    playagain = input("Do you want to play? Enter yes or exit") # makes the user play the game
    while playagain=="yes": # if the user wants to play
        animalguess(node) # play the game
        write_newtree(node,text) # write the new tree
        playagain = input("Do you want to play? Enter yes or exit") # ask if play again or exit
    print("The tree was saved to a new file") # the print statement if he exits
    sys.exit(0) # the exit

if __name__ == '__main__':
    main()







