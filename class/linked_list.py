class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
    def printlist(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

    def push(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
    def insertAfter(self,data,p_node):
        new_node  = node(data)
        tmp = self.head
        while(tmp):
            if tmp.data == p_node:
                break
            tmp = tmp.next
        new_node.next = tmp.next
        tmp.next = new_node

    def append(self,data):
        if self.head == None:
            self.head = node(data)
            return
        new_node = node(data)
        tmp = self.head
        while(tmp.next):
            tmp = tmp.next
        tmp.next = new_node

    def insertBefore(self,data,b_node):
        tmp = self.head
        count = 0
        while(tmp):
            if tmp.data == b_node:
                break
            count+=1
            tmp = tmp.next
        new_node = node(data)
        tmp1 = self.head
        i = 1 
        while(i<count):
            tmp1 = tmp1.next
            i+=1
        new_node.next = tmp1.next
        tmp1.next = new_node





l = linked_list()
l.push(6)
l.push(4)
l.insertAfter(5,4)
l.push(3)
l.append(7)
l.append(8)
l.push(2)
l.push(1)
l.append(9)
l.insertBefore(2.5,3)
l.insertBefore(4.5,5)
l.printlist()

