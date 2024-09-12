class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()

    def length(self):
        return len(self.stack)

    def display(self):
        return self.stack


class Queue:
    def __init__(self):
        self.queue = []

    def empty(self):
        return len(self.queue) == 0

    def Add(self, item):
        self.queue.append(item)

    def delete(self):
        if not self.empty():
            return self.queue.pop(0)

    def length(self):
        return len(self.queue)

    def display(self):
        return self.queue

def stack():
    stack = Stack()
    while True:
        print("\n--- Stack Operations ---")
        print("1. Push ")
        print("2. Pop")
        print("3. Display Stack")
        print("4. Exit")
        option = int(input("Enter your choice ---> "))

        if option == 1:
            item = input("Enter item to push: ")
            stack.push(item)
            print(f"'{item}' pushed onto stack.")
        elif option == 2:
            if not stack.empty():
                popped_item = stack.pop()
                print(f"Popped item: {popped_item}")
            else:
                print("Stack is empty!")
        elif option == 3:
            print(f"Stack content: {stack.display()}")
        elif option == 4:
            break
        else:
            print("Invalid option. Please try again.")


def queue():
    queue = Queue()
    while True:
        print("\n--- Queue Operations ---")
        print("1. Add ")
        print("2. delete")
        print("3. Display Queue")
        print("4. Exit")
        option = int(input("Enter your choice ----> "))

        if option == 1:
            item = input("Enter item to Add: ")
            queue.Add(item)
            print(f"'{item}' added to the queue.")
        elif option == 2:
            if not queue.empty():
                deleted_item = queue.delete()
                print(f"deleted item: {deleted_item}")
            else:
                print("Queue is empty!")
        elif option == 3:
            print(f"Queue content: {queue.display()}")
        elif option == 4:
            break
        else:
            print("error")

if __name__ == "__main__":
    while True:
        print("1. Stack")
        print("2. Queue")
        print("3. Exit")
        choice = int(input("Enter your choice ---> "))

        if choice == 1:
            stack()
        elif choice == 2:
            queue()
        elif choice == 3:
            break
        else:
            print("Invalid choice")
