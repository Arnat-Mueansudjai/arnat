class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print(f"Node with data {value} inserted at beginning.")

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            print(f"Node with data {value} inserted at end (list was empty).")
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        print(f"Node with data {value} inserted at end.")

    def insert_at_position(self, value, position):
        if position <= 1:
            self.insert_at_beginning(value)
            return

        new_node = Node(value)
        temp = self.head

        for i in range(position - 2):
            if temp is None:
                break
            temp = temp.next

        if temp is None:
            print("Position out of bounds. Inserting at end.")
            self.insert_at_end(value)
            return

        new_node.next = temp.next
        temp.next = new_node
        print(f"Inserted {value} at position {position}.")

    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head
        self.head = self.head.next
        print(f"Deleted {temp.data} from beginning.")

    def delete_from_end(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next is None:
            print(f"Deleted {self.head.data} from end.")
            self.head = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        print(f"Deleted {temp.next.data} from end.")
        temp.next = None

    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == value:
            print(f"Deleted node with value {value} (from beginning).")
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print(f"Value {value} not found.")
            return

        print(f"Deleted node with value {value}.")
        temp.next = temp.next.next

    def display(self):
        temp = self.head
        print("List:", end=" ")
        while temp:
            print(f"{temp.data} ->", end=" ")
            temp = temp.next
        print("None")

ll = LinkedList()

while True:
    print("\n|===== Menu =====|")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at position")
    print("4. Display list")
    print("5. Delete from beginning")
    print("6. Delete from end")
    print("7. Delete node by value")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        ll.insert_at_beginning(value)

    elif choice == 2:
        value = int(input("Enter value: "))
        ll.insert_at_end(value)

    elif choice == 3:
        value = int(input("Enter value: "))
        pos = int(input("Enter position: "))
        ll.insert_at_position(value, pos)

    elif choice == 4:
        ll.display()

    elif choice == 5:
        ll.delete_from_beginning()

    elif choice == 6:
        ll.delete_from_end()

    elif choice == 7:
        value = int(input("Enter value to delete: "))
        ll.delete_by_value(value)

    elif choice == 8:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
