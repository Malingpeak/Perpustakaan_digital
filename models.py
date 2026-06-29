# =========================
# BOOK
# =========================
class Book:
    def __init__(self, isbn, judul, pengarang, tahun, genre, stok):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.tahun = tahun
        self.genre = genre
        self.stok = stok

# =========================
# MEMBER
# =========================
class Member:
    def __init__(self, member_id, nama):
        self.member_id = member_id
        self.nama = nama


# =========================
# BORROW REQUEST
# =========================
class BorrowRequest:
    def __init__(self, member, book):
        self.member = member
        self.book = book
