class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  

class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None   
        self.size = 0      

    def is_empty(self):
        """Check if the queue is empty"""
        return self.front is None

    def enqueue(self, data):
        """Add an item to the queue"""
        new_node = Node(data)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """Remove an item from the queue"""
        if self.is_empty():
            print("Queue is empty!")
            return None
        else:
            dequeued_node = self.front
            self.front = self.front.next
            self.size -= 1
            return dequeued_node.data

    def peek(self):
        """View the front item without removing it"""
        if self.is_empty():
            return None
        return self.front.data

    def get_size(self):
        """Return the size of the queue"""
        return self.size

    def display(self):
        """Display all the elements of the queue"""
        if self.is_empty():
            print("Queue is empty!")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        
if __name__ == "__main__":
    q = Queue()

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue after enqueues:")
    q.display()  # Should display: 10 -> 20 -> 30 -> None

    print(f"Dequeued: {q.dequeue()}")  # Should return 10
    print(f"Front item: {q.peek()}")  # Should return 20

    print(f"Queue size: {q.get_size()}")  # Should return 2

    q.display()  # Should display: 20 -> 30 -> None