# 📚 Digital Library Management System

A simple **Digital Library Management System** developed in **Python** as a second-semester Data Structures project.

The project demonstrates the implementation of several fundamental data structures without using external libraries for the core data structures.

---

## Features

### Book Management

* Add Book
* Search Book
* Edit Book
* Delete Book
* Display All Books
* Search by Author
* Search by Year
* Search by Genre

### Member Management

* Add Member
* Search Member
* Edit Member
* Delete Member
* Display Members

### Borrowing System

* Borrow Book
* Return Book
* Borrow Queue (FIFO)
* Borrow History

---

## Data Structures Used

| Data Structure                 | Purpose                                            |
| ------------------------------ | -------------------------------------------------- |
| Binary Search Tree (BST)       | Store and manage book data                         |
| Hash Table (Separate Chaining) | Store and search member data                       |
| Queue (Linked List)            | Manage borrowing queue when books are out of stock |

---

## Project Structure

```text
Digital-Library/
│
├── main.py
├── library_system.py
├── models.py
├── bst.py
├── hashtable.py
├── queue_system.py
└── README.md
```

---

## Requirements

* Python 3.10 or newer

---

## How to Run

Clone the repository

```bash
git clone https://github.com/yourusername/Digital-Library.git
```

Move into the project folder

```bash
cd Digital-Library
```

Run the program

```bash
python main.py
```

---

## Example Menu

```text
========== DIGITAL LIBRARY ==========

1. Book Menu
2. Member Menu
3. Borrow Book
4. Return Book
5. Borrow Queue
6. History
0. Exit
```

---

## Authors

Second Semester Data Structures Project

INSTITUT DIGITAL EKONOMI LPKIA ...
