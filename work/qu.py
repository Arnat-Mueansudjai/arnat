class link:
    def __init__(self,data):
        self.data=data
        self.next=None

class qu:
    def __init__(self):
        self.head = None

    def ins(self,val):
        new_node = link(val)
        if self.head is None:
            self.head = new_node

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self):
        if self.head is None:
            print("List is empty.")

        if self.head.next is None:
            print(f"Deleted {self.head.data} from end.")
            self.head = None

        temp = self.head
        while temp.next:
            temp = temp.next

        print(f"Deleted {temp.next} from end.")
        temp.next = None