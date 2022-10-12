# Implementing Linked List 

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = Node()
        
    def append(self,value):
        newnode = Node(value)
        currentnode = self.head
        while currentnode.next != None:
            currentnode = currentnode.next
        currentnode.next = newnode
        
    def getlength(self):
        currentnode = self.head
        total = 0
        while currentnode.next != None:
            currentnode = currentnode.next
            total+=1
        return total
    
    def display(self):
        currentnode = self.head
        arr = []
        while currentnode.next != None:
            currentnode = currentnode.next
            arr.append(currentnode.data)
        print(arr)

    def get(self,wantedindex):
        currentnode = self.head
        currentindex = 0
        while currentnode.next != None:
            currentnode = currentnode.next
            if currentindex == wantedindex:
                return currentnode.data
            else:
                currentindex += 1
    
    def erase(self,wantedindex):
        currentnode = self.head
        currentindex = 0
        while currentnode.next != None:
            lastnode = currentnode
            currentnode = currentnode.next
            if currentindex == wantedindex:
                lastnode.next = currentnode.next
                return
            else: 
                currentindex += 1
            
                

      



try1 = LinkedList()
for i in range(5):
    try1.append(i)
try1.display()
try1.erase(1)
try1.display()






        



