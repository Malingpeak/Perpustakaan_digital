# from models import Member

# ==========================
# NODE
# ==========================
class NodeMember:
    def __init__(self, member):
        self.member = member
        self.next = None


# ==========================
# HASH TABLE
# ==========================
class HashTable:
    def __init__(self, size=10):
        self.size = size
        # Create empty buckets
        self.table = [None] * size

    def hash_function(self, member_id):
        number = ""
        for char in member_id:
            if char.isdigit():
                number += char
        return int(number) % self.size

    # ======================
    # CREATE
    # ======================
    def add(self, member):
        index = self.hash_function(member.member_id)
        newNode = NodeMember(member)
        # Empty bucket
        if self.table[index] is None:
            self.table[index] = newNode
            return

        # Collision
        current = self.table[index]

        while current.next is not None:
            current = current.next
        current.next = newNode

    # ======================
    # READ
    # ======================
    def search(self, member_id):
        index = self.hash_function(member_id)
        current = self.table[index]
        while current is not None:
            if current.member.member_id == member_id:
                return current
            current = current.next
        return None

    # ======================
    # UPDATE
    # ======================
    def edit(self, member_id, new_name):
        node = self.search(member_id)
        if node is None:
            return False
        node.member.nama = new_name
        return True

    # ======================
    # DELETE
    # ======================
    def delete(self, member_id):
        index = self.hash_function(member_id)
        current = self.table[index]
        previous = None
        while current is not None:
            if current.member.member_id == member_id:
                # First node
                if previous is None:
                    self.table[index] = current.next
                # Middle / Last node
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

    # ======================
    # DISPLAY
    # ======================
    def display(self):
        print("\n===== MEMBER LIST =====")
        found = False
        for bucket in self.table:
            current = bucket
            while current is not None:
                found = True
                print(f"ID   : {current.member.member_id}")
                print(f"Nama : {current.member.nama}")
                print("--------------------")
                current = current.next
        if not found:
            print("Tidak ada Member.")
