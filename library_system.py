from models import Book
from models import Member
from models import BorrowRequest

from bst import BST
from hash_table import HashTable
from queue_system import Queue


class LibrarySystem:

    def __init__(self):
        self.books = BST()
        self.members = HashTable()
        self.borrow_queue = Queue()
        # Borrow history
        self.history = []
        self.current_borrow = []

    # ==================================================
    # Helper
    # ==================================================

    def helper(self, member_id=None, judul=None):
        if member_id != None:
            if self.members.search(member_id):
                return True
        elif judul != None:
            if self.books.search(judul):
                return True
        else:
            return False

    # ==================================================
    # BOOK
    # ==================================================

    def add_book(self, isbn, judul, pengarang, tahun, genre, stok):
        book = Book(isbn, judul, pengarang, tahun, genre, stok)
        if self.books.search(judul):
            print("Buku sudah ada.")
            return
        self.books.insert(book)
        print("Buku berhasil ditambahkan.")

    def search_book(self, judul):
        return self.books.search(judul)

    def edit_book(self, judul, pengarang=None, tahun=None, genre=None, stok=None):
        return self.books.edit(judul, pengarang, tahun, genre, stok)

    def delete_book(self, judul):
        if not self.books.search(judul):
            print("Buku tidak ada.")
            return
        print("Buku Ada.")
        text = input("Konfirmasi Penghapusan Buku (Y/N): ").strip().lower()
        if text in ("y", "yes"):
            self.books.delete(judul)
            print("Buku Berhasil di Hapus")
        else:
            print("Buku Batal Di Hapus")

    def display_books(self):
        self.books.display()

    # ==================================================
    # MEMBER
    # ==================================================

    def add_member(self, member_id, nama):
        member = Member(member_id, nama)
        if self.members.search(member_id):
            print("Id atau member sudah ada")
            return
        self.members.add(member)
        print("Member berhasil di tambahkan.")

    def search_member(self, member_id):
        return self.members.search(member_id)

    def edit_member(self, member_id, new_name):
        if self.members.search(member_id):
            return self.members.edit(member_id, new_name)

    # def delete_member(self, member_id):
    #     self.members.delete(member_id)
    #     print("Member berhasil di hapus.")

    def delete_member(self, member_id):
        if not self.members.search(member_id):
            print("Member tidak ditemukan.")
            return
        print("Member ditemukan")
        text = input("Konfirmasi Penghapusan Member (Y/N): ").strip().lower()
        if text in ("y", "yes"):
            self.members.delete(member_id)
            print("Member Berhasil di Hapus")
        else:
            print("Member Batal Di Hapus")

    def display_members(self):
        self.members.display()

    # ==================================================
    # BORROW BOOK
    # ==================================================

    def borrow_book(self, member_id, judul):
        member_node = self.members.search(member_id)
        if member_node is None:
            print("Member tidak ditemukan.")
            return

        book_node = self.books.search(judul)

        if book_node is None:
            print("Buku tidak ditemukan.")
            return

        # Book available
        if book_node.book.stok > 0:
            book_node.book.stok -= 1
            self.history.append(
                f"[Peminjaman] {member_node.member.nama} meminjam '{book_node.book.judul}'"
            )
            self.current_borrow.append(
                (
                    member_node.member.member_id,
                    member_node.member.nama,
                    book_node.book.judul,
                )
            )

            print("Buku Berhasil dipinjamkan.")
            print(f"Stock tersisa : {book_node.book.stok}")
            return

        # Book out of stock
        request = BorrowRequest(member_node.member, book_node.book)
        self.borrow_queue.enqueue(request)
        print("Buku tidak tersedia.")
        print("Menambahkan ke antrian peminjaman.")

    # ==================================================
    # RETURN BOOK
    # ==================================================

    def return_book(self, member_id, judul):
        book_node = self.books.search(judul)
        if book_node is None:
            print("Buku tidak ditemukan.")
            return
        # Check whether this book is actually borrowed
        borrowed = None
        for data in self.current_borrow:
            if data[0] == member_id and data[2] == judul:
                borrowed = data
                break
        if borrowed is None:
            print("Buku ini sedang tidak di pinjamkan.")
            return
        # Remove from current borrow list
        self.current_borrow.remove(borrowed)
        # Increase stock
        book_node.book.stok += 1
        # Save history
        self.history.append(f"[Pengembalian] {borrowed[1]} mengembalikan '{judul}'")
        print("Buku telah dikembalikan.")
        print(f"Sisa Stock : {book_node.book.stok}")
        # Check waiting queue
        next_request = self.borrow_queue.peek()
        if next_request is None:
            return
        if next_request.book.judul == judul:
            next_request = self.borrow_queue.dequeue()
            book_node.book.stok -= 1
            self.current_borrow.append(
                (
                    next_request.member.member_id,
                    next_request.member.nama,
                    next_request.book.judul,
                )
            )
            self.history.append(
                f"[Peminjaman] : {next_request.member.nama} -> {next_request.book.judul}"
            )
            print(f"{next_request.member.nama} Otomatis meminjam buku tersebut.")
            print(f"Sisa Stock : {book_node.book.stok}")

    # ==================================================
    # HISTORY
    # ==================================================

    def show_history(self):
        print("\n===== HISTORY =====")

        if len(self.history) == 0:
            print("tidak ada history.")
            return

        number = 1
        for item in self.history:
            print(f"{number}. {item}")
            number += 1

    # ==================================================
    # MULTI SEARCH
    # ==================================================

    def search_by_all(self, keyword):
        result = []
        # Search author
        result.extend(self.books.search_author(keyword))
        # Search genre
        result.extend(self.books.search_genre(keyword))
        # Search year
        if keyword.isdigit():
            result.extend(self.books.search_year(int(keyword)))
        return result
