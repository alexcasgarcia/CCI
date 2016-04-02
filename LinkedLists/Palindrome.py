from LinkedList import Node
import math

def isPalindrome(head,length):
    i = 0
    while (i < int(math.floor(length/2))):
        j=i+1
        innerNode = head.getNextNode()
        while (j < length - 1 - i): 
            innerNode = innerNode.getNextNode()
            j+=1
        if (head.getValue() != innerNode.getValue()):
            return False

        head = head.getNextNode()
        i+=1
    return True

def isPalindrome2(head):
    lengthNode = head
    length = 1
    while (lengthNode.getNextNode()):
        length += 1
        lengthNode = lengthNode.getNextNode()

    i = 0
    while (i < int(math.floor(length/2))):
        j=i+1
        innerNode = head.getNextNode()
        while (j < length - 1 - i): 
            innerNode = innerNode.getNextNode()
            j+=1
        if (head.getValue() != innerNode.getValue()):
            return False

        head = head.getNextNode()
        i+=1
    return True










head = Node("A")
head.appendToTail(Node("B"))
head.appendToTail(Node("C"))
head.appendToTail(Node("B"))
head.appendToTail(Node("A"))

print isPalindrome(head,5)

head = Node("A")
head.appendToTail(Node("B"))
head.appendToTail(Node("C"))
head.appendToTail(Node("D"))
head.appendToTail(Node("E"))
head.appendToTail(Node("E"))
head.appendToTail(Node("D"))
head.appendToTail(Node("C"))
head.appendToTail(Node("B"))
head.appendToTail(Node("A"))
print isPalindrome2(head)
