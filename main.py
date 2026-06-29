# imrpovement print("=" * 40)
from library_system import LibrarySystem

library = LibrarySystem()


def pause():
    print("=" * 40)
    input("Tekan ENTER untuk melanjutkan...")


# ==================================================
# SAMPLE DATA
# ==================================================

library.add_book("B001", "Harry Potter", "J.K. Rowling", 1997, "Fantasy", 2)
library.add_book("B002", "Clean Code", "Robert Martin", 2008, "Programming", 1)
library.add_book("B003", "Atomic Habits", "James Clear", 2018, "Self Help", 3)
library.add_member("M001", "Wawan")
library.add_member("M002", "Budi")

# ==================================================
# MAIN MENU
# ==================================================

while True:
    print("\n========== DIGITAL LIBRARY ==========")
    print("1. Menu Buku")
    print("2. Menu Member")
    print("3. Pinjam Buku")
    print("4. Pengembalian buku")
    print("5. Antrian Peminjaman")
    print("6. History")
    print("0. Exit")
    choice = input("Pilih: ")

    # ==================================================
    # BOOK MENU
    # ==================================================
    if choice == "1":
        while True:
            print("\n===== Menu Buku =====")
            print("1. Tambah Buku")
            print("2. Cari Buku")
            print("3. Edit Buku")
            print("4. Hapus Buku")
            print("5. Tampilkan Buku")
            print("6. Cari dari (Author / Tahun / Genre)")
            print("0. Kembali")

            book_choice = input("Pilih: ")

            if book_choice == "1":

                isbn = input("ISBN : ")
                judul = input("Judul : ")
                author = input("Penulis : ")
                year = int(input("Tahun : "))
                genre = input("Genre : ")
                stock = int(input("Stock : "))

                if isbn.isdigit():
                    isbn = f"B{int(isbn):03d}"

                library.add_book(isbn, judul, author, year, genre, stock)

                pause()
            elif book_choice == "2":

                title = input("Judul : ")
                result = library.search_book(title)
                if result:
                    print("\n===== BUKU DITEMUKAN =====")
                    print(f"ISBN       : {result.book.isbn}")
                    print(f"Judul      : {result.book.judul}")
                    print(f"Penulis    : {result.book.pengarang}")
                    print(f"Tahun      : {result.book.tahun}")
                    print(f"Genre      : {result.book.genre}")
                    print(f"Stock      : {result.book.stok}")
                    pause()
                else:
                    print("Buku tidak di temukan.")
                    pause()

            elif book_choice == "3":
                title = input("Judul Buku : ")

                valid = library.helper(None, title)
                if valid:
                    print("Buku Ditemukan")
                    author = input("Penulis Baru : ")
                    year = int(input("Tahun Baru : "))
                    genre = input("Genre Baru : ")
                    stock = int(input("Stock Baru : "))

                    if library.edit_book(title, author, year, genre, stock):
                        print("Buku berhasil di perbaharui.")
                else:
                    print("Buku tidak di temukan.")
                pause()

            elif book_choice == "4":
                title = input("Judul : ")
                library.delete_book(title)
                pause()

            elif book_choice == "5":
                library.display_books()
                pause()

            elif book_choice == "6":
                keyword = input("Cari (Penulis / Tahun / Genre): ")
                books = library.search_by_all(keyword)
                if books:
                    print("\n===== Hasil Pencarian =====")
                    for book in books:
                        print(f"- {book.judul}")
                else:
                    print("Tidak ditemukan buku yang sesuai.")
                pause()

            elif book_choice == "0":
                break
            else:
                print("Salah Ketik ?")
                pause()

    # ==================================================
    # MEMBER MENU
    # ==================================================
    elif choice == "2":

        while True:
            print("\n===== MEMBER MENU =====")
            print("1. Tambah Member")
            print("2. Cari Member")
            print("3. Edit Member")
            print("4. Hapus Member")
            print("5. Tampilkan Members")
            print("0. Kembali")

            member_choice = input("Pilih: ")

            if member_choice == "1":
                member_id = input("ID : ").strip().upper()
                if member_id.isdigit():
                    member_id = f"M{int(member_id):03d}"
                valid = library.helper(member_id)

                if valid:
                    print("Member sudah ada.")
                else:
                    name = input("Nama : ")
                    library.add_member(member_id, name)
                    pause()

            elif member_choice == "2":
                member_id = input("ID : ")
                if member_id.isdigit():
                    member_id = f"M{int(member_id):03d}"
                member = library.search_member(member_id)
                if member:
                    print("\n===== MEMBER FOUND =====")
                    print(f"ID         : {member.member.member_id}")
                    print(f"Nama       : {member.member.nama}")
                    pause()
                else:
                    print("Member tidak ditemukan.")
                    pause()

            elif member_choice == "3":
                member_id = input("ID : ")
                if member_id.isdigit():
                    member_id = f"M{int(member_id):03d}"
                valid = library.helper(member_id)
                if valid:
                    print("Member ditemukan")
                    name = input("Nama Baru : ")
                    library.edit_member(member_id, name)
                    print("Data member berhasil diperbaharui")
                else:
                    print("Member tidak ditemukan")

                pause()

            elif member_choice == "4":
                member_id = input("ID : ")
                if member_id.isdigit():
                    member_id = f"M{int(member_id):03d}"
                library.delete_member(member_id)
                pause()

            elif member_choice == "5":
                library.display_members()
                pause()

            elif member_choice == "0":
                break
            else:
                print("Salah ketik?")
                pause()

    # ==================================================
    # BORROW BOOK
    # ==================================================
    elif choice == "3":
        member_id = input("Member ID : ").strip().upper()
        if member_id.isdigit():
            member_id = f"M{int(member_id):03d}"
        title = input("Judul Buku : ")
        library.borrow_book(member_id, title)
        pause()

    # ==================================================
    # RETURN BOOK
    # ==================================================
    elif choice == "4":

        member_id = input("Member ID : ").strip().upper()
        if member_id.isdigit():
            member_id = f"M{int(member_id):03d}"
        title = input("Judul Buku : ")
        library.return_book(member_id, title)
        pause()

    # ==================================================
    # VIEW QUEUE
    # ==================================================
    elif choice == "5":
        library.borrow_queue.display()
        pause()

    # ==================================================
    # HISTORY
    # ==================================================
    elif choice == "6":
        library.show_history()
        pause()

    # ==================================================
    # EXIT
    # ==================================================
    elif choice == "0":
        print("Thank you.")
        break

    else:
        print("Salah Ketik?")
        pause()
