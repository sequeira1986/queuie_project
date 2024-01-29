class Queue:
    def __init__(self, capacity=None):
        if capacity is None:
            capacity = 10
        self.queue = []
        self.capacity = capacity

    def IsEmpty(self):
        return len(self.queue) == 0

    def IsFull(self):
        return len(self.queue) == self.capacity

    def Enqueue(self, item):
        if not self.IsFull():
            self.queue.append(item)
        else:
            print("Error: Queue is full")

    def Dequeue(self):
        if not self.IsEmpty():
            return self.queue.pop(0)
        else:
            print("Error: Queue is empty")

    def Show(self):
        if not self.IsEmpty():
            for item in self.queue:
                print(item, end=' ')
            print()
        else:
            print("Queue is empty")


def menu():
    print("1. Is Empty")
    print("2. Is Full")
    print("3. Enqueue")
    print("4. Dequeue")
    print("5. Show")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    return choice


q = Queue()
while True:
    choice = menu()

    if choice == 1:
        print(q.IsEmpty())
    elif choice == 2:
        print(q.IsFull())
    elif choice == 3:
        item = input("Enter an item to enqueue: ")
        q.Enqueue(item)
    elif choice == 4:
        print(q.Dequeue())
    elif choice == 5:
        q.Show()
    elif choice == 6:
        break
    else:
        print("Invalid choice")

while True:
    try:
        item = input("Enter an item to enqueue")
        q.Enqueue(item)
    except:
        break
