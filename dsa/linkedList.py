class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self) -> str:
        return f'data: {self.data} next_node {self.next}--->>'

class LinkedList:
    def __init__(self,head: Node):
        self.head = head

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def size(self):
        temp = self.head
        counter = 0
        while temp:
            counter+=1
            temp = temp.next
        return counter