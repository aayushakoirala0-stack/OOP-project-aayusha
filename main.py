from library import Library, Book, StudentMember, FacultyMember


def main():

    library = Library()

    while True:

        print("\n================================")
        print("      LIBRARY MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Register Student Member")
        print("5. Register Faculty Member")
        print("6. Display Members")
        print("7. Issue Book")
        print("8. Return Book")
        print("9. Exit")
        print("================================")

        try:
            choice = int(input("Enter your choice: "))

            # Add Book
            if choice == 1:

                book_id = int(input("Enter book ID: "))
                title = input("Enter book title: ")
                author = input("Enter author name: ")

                book = Book(book_id, title, author)

                library.add_book(book)

            # Display Books
            elif choice == 2:

                library.display_books()

            # Search Book
            elif choice == 3:

                title = input("Enter book title to search: ")

                library.search_book(title)

            # Student Member
            elif choice == 4:

                member_id = int(input("Enter member ID: "))
                name = input("Enter member name: ")
                email = input("Enter email: ")

                member = StudentMember(
                    member_id,
                    name,
                    email
                )

                library.add_member(member)

            # Faculty Member
            elif choice == 5:

                member_id = int(input("Enter member ID: "))
                name = input("Enter member name: ")
                email = input("Enter email: ")

                member = FacultyMember(
                    member_id,
                    name,
                    email
                )

                library.add_member(member)

            # Display Members
            elif choice == 6:

                library.display_members()

            # Issue Book
            elif choice == 7:

                book_id = int(input("Enter book ID: "))
                member_id = int(input("Enter member ID: "))

                library.issue_book(book_id, member_id)

            # Return Book
            elif choice == 8:

                book_id = int(input("Enter book ID: "))

                library.return_book(book_id)

            # Exit
            elif choice == 9:

                print("Thank you for using Library Management System!")
                break

            else:

                print("Invalid choice. Please select 1-9.")

        except ValueError:

            print("Invalid input! Please enter a number.")

        except Exception as e:

            print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()