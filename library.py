from abc import ABC, abstractmethod
import json


# =========================
# ABSTRACT CLASS: LIBRARY ITEM
# =========================

class LibraryItem(ABC):

    def __init__(self, item_id):
        self.item_id = item_id

    @abstractmethod
    def display_info(self):
        pass


# =========================
# BOOK CLASS - INHERITANCE
# =========================

class Book(LibraryItem):

    def __init__(self, book_id, title, author, available=True):
        super().__init__(book_id)

        # Private attributes - Encapsulation
        self.__title = title
        self.__author = author
        self.__available = available

    def display_info(self):
        status = "Available" if self.__available else "Issued"
        print(f"ID: {self.item_id} | Title: {self.__title} | "
              f"Author: {self.__author} | Status: {status}")

    def get_data(self):
        return {
            "id": self.item_id,
            "title": self.__title,
            "author": self.__author,
            "available": self.__available
        }

    def get_title(self):
        return self.__title

    def is_available(self):
        return self.__available

    def issue_book(self):
        if self.__available:
            self.__available = False
            return True
        return False

    def return_book(self):
        self.__available = True


# =========================
# ABSTRACT CLASS: MEMBER
# =========================

class Member(ABC):

    def __init__(self, member_id, name, email):
        # Private attributes - Encapsulation
        self.__member_id = member_id
        self.__name = name
        self.__email = email

    @abstractmethod
    def get_member_type(self):
        pass

    def get_member_data(self):
        return {
            "id": self.__member_id,
            "name": self.__name,
            "email": self.__email,
            "type": self.get_member_type()
        }

    def get_member_id(self):
        return self.__member_id

    def get_name(self):
        return self.__name


# =========================
# STUDENT MEMBER - INHERITANCE
# =========================

class StudentMember(Member):

    def get_member_type(self):
        return "Student"


# =========================
# FACULTY MEMBER - INHERITANCE
# =========================

class FacultyMember(Member):

    def get_member_type(self):
        return "Faculty"


# =========================
# LIBRARY SYSTEM CLASS
# =========================

class Library:

    def __init__(self):
        self.__books = []
        self.__members = []
        self.__issued_books = {}

        self.load_data()

    # -------------------------
    # ADD BOOK
    # -------------------------

    def add_book(self, book):
        self.__books.append(book)
        self.save_data()
        print("Book added successfully!")

    # -------------------------
    # DISPLAY BOOKS
    # -------------------------

    def display_books(self):

        if not self.__books:
            print("No books available.")
            return

        print("\n========== BOOK LIST ==========")

        for book in self.__books:
            book.display_info()

    # -------------------------
    # SEARCH BOOK
    # -------------------------

    def search_book(self, title):

        found = False

        for book in self.__books:
            if title.lower() in book.get_title().lower():
                book.display_info()
                found = True

        if not found:
            print("Book not found.")

    # -------------------------
    # REGISTER MEMBER
    # -------------------------

    def add_member(self, member):

        self.__members.append(member)
        self.save_data()

        print("Member registered successfully!")

    # -------------------------
    # DISPLAY MEMBERS
    # -------------------------

    def display_members(self):

        if not self.__members:
            print("No members registered.")
            return

        print("\n========== MEMBER LIST ==========")

        for member in self.__members:

            data = member.get_member_data()

            print(
                f"ID: {data['id']} | "
                f"Name: {data['name']} | "
                f"Email: {data['email']} | "
                f"Type: {data['type']}"
            )

    # -------------------------
    # ISSUE BOOK
    # -------------------------

    def issue_book(self, book_id, member_id):

        for book in self.__books:

            if book.item_id == book_id:

                if not book.is_available():
                    print("Book is already issued.")
                    return

                member_exists = False

                for member in self.__members:
                    if member.get_member_id() == member_id:
                        member_exists = True
                        break

                if not member_exists:
                    print("Member not found.")
                    return

                book.issue_book()

                self.__issued_books[str(book_id)] = member_id

                self.save_data()

                print("Book issued successfully!")
                return

        print("Book not found.")

    # -------------------------
    # RETURN BOOK
    # -------------------------

    def return_book(self, book_id):

        for book in self.__books:

            if book.item_id == book_id:

                if book.is_available():
                    print("This book has not been issued.")
                    return

                book.return_book()

                if str(book_id) in self.__issued_books:
                    del self.__issued_books[str(book_id)]

                self.save_data()

                print("Book returned successfully!")
                return

        print("Book not found.")

    # =========================
    # SAVE DATA TO JSON
    # =========================

    def save_data(self):

        data = {
            "books": [book.get_data() for book in self.__books],
            "members": [member.get_member_data()
                        for member in self.__members],
            "issued_books": self.__issued_books
        }

        try:

            with open("library_data.json", "w") as file:
                json.dump(data, file, indent=4)

        except IOError:
            print("Error: Unable to save data.")

    # =========================
    # LOAD DATA FROM JSON
    # =========================

    def load_data(self):

        try:

            with open("library_data.json", "r") as file:
                data = json.load(file)

            # Load books
            for book_data in data.get("books", []):

                book = Book(
                    book_data["id"],
                    book_data["title"],
                    book_data["author"],
                    book_data["available"]
                )

                self.__books.append(book)

            # Load members
            for member_data in data.get("members", []):

                if member_data["type"] == "Student":

                    member = StudentMember(
                        member_data["id"],
                        member_data["name"],
                        member_data["email"]
                    )

                else:

                    member = FacultyMember(
                        member_data["id"],
                        member_data["name"],
                        member_data["email"]
                    )

                self.__members.append(member)

            self.__issued_books = data.get("issued_books", {})

        except FileNotFoundError:
            # First time running the program
            pass

        except (json.JSONDecodeError, KeyError):
            print("Error: Invalid data file.")