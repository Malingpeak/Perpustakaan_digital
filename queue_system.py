from models import BorrowRequest


# ==========================
# NODE
# ==========================
class QueueNode:
    def __init__(self, request):
        self.request = request
        self.next = None


# ==========================
# QUEUE
# ==========================
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # ======================
    # ENQUEUE
    # ======================
    def enqueue(self, request):
        newNode = QueueNode(request)
        # Queue is empty
        if self.front is None:
            self.front = newNode
            self.rear = newNode
            return
        # Add new node at the back
        self.rear.next = newNode
        self.rear = newNode

    # ======================
    # DEQUEUE
    # ======================
    def dequeue(self):
        # Queue is empty
        if self.front is None:
            return None
        removed = self.front.request
        # Move front forward
        self.front = self.front.next
        # Queue becomes empty
        if self.front is None:
            self.rear = None
        return removed

    # ======================
    # PEEK
    # ======================
    def peek(self):
        if self.front is None:
            return None
        return self.front.request

    # ======================
    # DISPLAY QUEUE
    # ======================
    def display(self):
        print("\n===== BORROW QUEUE =====")
        if self.front is None:
            print("Antrian Kosong.")
            return
        current = self.front
        number = 1
        while current is not None:
            print(f"\nAntrian #{number}")
            print(f"Member : {current.request.member.nama}")
            print(f"Buku   : {current.request.book.judul}")
            current = current.next
            number += 1

    # ======================
    # CHECK EMPTY
    # ======================
    def is_empty(self):
        return self.front is None
