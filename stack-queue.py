class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        return len(self.stack)

    def display(self):
        return self.stack


class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            raise IndexError("Peek from an empty queue")

    def size(self):
        return len(self.queue)

    def display(self):
        return self.queue


def show_menu():
    print("1. Stack")
    print("2. Queue")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))
    return choice

def stack_operations():
    stack = Stack()
    while True:
        print("\n--- Stack Operations ---")
        print("1. Push (Insert)")
        print("2. Pop (Delete)")
        print("3. Peek (Read Top Element)")
        print("4. Display Stack")
        print("5. Exit to Main Menu")
        option = int(input("Enter your choice: "))

        if option == 1:
            item = input("Enter item to push: ")
            stack.push(item)
            print(f"'{item}' pushed onto the stack.")
        elif option == 2:
            if not stack.is_empty():
                popped_item = stack.pop()
                print(f"Popped item: {popped_item}")
            else:
                print("Stack is empty!")
        elif option == 3:
            if not stack.is_empty():
                print(f"Top item: {stack.peek()}")
            else:
                print("Stack is empty!")
        elif option == 4:
            print(f"Stack content: {stack.display()}")
        elif option == 5:
            break
        else:
            print("Invalid option. Please try again.")


def queue_operations():
    queue = Queue()
    while True:
        print("\n--- Queue Operations ---")
        print("1. Enqueue (Insert)")
        print("2. Dequeue (Delete)")
        print("3. Peek (Read Front Element)")
        print("4. Display Queue")
        print("5. Exit to Main Menu")
        option = int(input("Enter your choice: "))

        if option == 1:
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
            print(f"'{item}' added to the queue.")
        elif option == 2:
            if not queue.is_empty():
                dequeued_item = queue.dequeue()
                print(f"Dequeued item: {dequeued_item}")
            else:
                print("Queue is empty!")
        elif option == 3:
            if not queue.is_empty():
                print(f"Front item: {queue.peek()}")
            else:
                print("Queue is empty!")
        elif option == 4:
            print(f"Queue content: {queue.display()}")
        elif option == 5:
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    while True:
        choice = show_menu()

        if choice == 1:
            stack_operations()
        elif choice == 2:
            queue_operations()
        elif choice == 3:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
