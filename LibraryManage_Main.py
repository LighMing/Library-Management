from library_management import Library, Member


def main():
    lib = Library()

    while True:
        print("\nWelcome to the Library management!")
        print("\nYou can search any of book you like and also you can add any of book in library memory bank!")

        print("\n------ Menu ------")  # I make a menu to let the user easily to use
        print("1. Add a book")
        print("2. Add a member")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. Display all books")
        print("6. Display all members")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            ISBN = input("Enter book ISBN: ")
            copies = int(input("Enter number of available copies: "))
            lib.add_book(title, author, ISBN, copies)

        elif choice == '2':
            name = input("Enter member's name: ")
            member_id = input("Enter member's id: ")
            lib.add_member(name, member_id)

        elif choice == '3':
            member_id = input("Enter member's id: ")
            book_name = input("Enter book name you want to borrow: ")
            for member in lib.members:
                if member.member_id == member_id:
                    for book in lib.books:
                        if book.title.lower() == book_name.lower():
                            member.borrow_book(book)

        elif choice == '4':
            member_id = input("Enter member's id: ")
            book_name = input("Enter book name you want to return: ")
            for member in lib.members:
                if member.member_id == member_id:
                    for book in lib.books:
                        if book.title.lower() == book_name.lower():
                            member.return_book(book)

        elif choice == '5':
            print("Showing all books in the library:")
            lib.display_books()

        elif choice == '6':
            print("Showing all members in the library:")
            lib.display_members()

        elif choice == '7':
            print("Exit")

        else:
            print("Invalid choice, please pick a valid option!")


if __name__ == '__main__':
    main()
