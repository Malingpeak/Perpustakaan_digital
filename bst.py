# from models import Book


class NodeBook:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


# ==========================
# BINARY SEARCH TREE
# ==========================
class BST:
    def __init__(self):
        self.root = None

    # ======================
    # CREATE
    # ======================
    def insert(self, book):
        newNode = NodeBook(book)
        # First book becomes root
        if self.root is None:
            self.root = newNode
            return
        current = self.root

        while True:
            # Smaller title -> Left
            if book.judul < current.book.judul:
                if current.left is None:
                    current.left = newNode
                    return
                current = current.left
            # Bigger title -> Right
            else:
                if current.right is None:
                    current.right = newNode
                    return
                current = current.right

    # ======================
    # READ
    # ======================
    def search(self, judul):
        current = self.root
        while current is not None:
            if judul == current.book.judul:
                return current
            elif judul < current.book.judul:
                current = current.left
            else:
                current = current.right
        return None

    # ======================
    # UPDATE
    # ======================
    def edit(self, judul, pengarang=None, tahun=None, genre=None, stok=None):
        node = self.search(judul)
        if node is None:
            return False
        if pengarang is not None:
            node.book.pengarang = pengarang
        if tahun is not None:
            node.book.tahun = tahun
        if genre is not None:
            node.book.genre = genre
        if stok is not None:
            node.book.stok = stok
        return True

    # ======================
    # DELETE
    # ======================
    def delete(self, judul):
        self.root = self._delete(self.root, judul)

    def _delete(self, node, judul):
        if node is None:
            return None
        if judul < node.book.judul:
            node.left = self._delete(node.left, judul)
        elif judul > node.book.judul:
            node.right = self._delete(node.right, judul)
        else:
            # No left child
            if node.left is None:
                return node.right
            # No right child
            if node.right is None:
                return node.left
            # Two children
            successor = self.find_min(node.right)
            node.book = successor.book
            node.right = self._delete(node.right, successor.book.judul)
        return node

    # ======================
    # Find smallest node
    # ======================
    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ======================
    # Display (Inorder)
    # ======================
    def display(self):
        self._display(self.root)

    def _display(self, node):
        if node is None:
            return
        self._display(node.left)
        print("--------------------------------")
        print("ISBN      :", node.book.isbn)
        print("Judul     :", node.book.judul)
        print("Penulis   :", node.book.pengarang)
        print("Tahun     :", node.book.tahun)
        print("Genre     :", node.book.genre)
        print("Stock     :", node.book.stok)
        self._display(node.right)

    # ======================
    # Search by Author
    # ======================
    def search_author(self, author):
        result = []
        self._search_author(self.root, author, result)
        return result

    def _search_author(self, node, author, result):
        if node is None:
            return
        self._search_author(node.left, author, result)
        if node.book.pengarang.lower() == author.lower():
            result.append(node.book)
        self._search_author(node.right, author, result)

    # ======================
    # Search by Year
    # ======================
    def search_year(self, year):
        result = []
        self._search_year(self.root, year, result)
        return result

    def _search_year(self, node, year, result):
        if node is None:
            return
        self._search_year(node.left, year, result)
        if node.book.tahun == year:
            result.append(node.book)
        self._search_year(node.right, year, result)

    # ======================
    # Search by Genre
    # ======================
    def search_genre(self, genre):
        result = []
        self._search_genre(self.root, genre, result)
        return result

    def _search_genre(self, node, genre, result):
        if node is None:
            return
        self._search_genre(node.left, genre, result)
        if node.book.genre.lower() == genre.lower():
            result.append(node.book)
        self._search_genre(node.right, genre, result)
