class Book:  # Initialize book variables
    def __init__(self, title, author, ISBN, available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.available_copies = available_copies

    def display_details(self):  # Display details of the book
        print(
            f'Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nAvailable Copies: {self.available_copies}')

    def check_availability(self):  # Check if the book is available
        if self.available_copies > 0:
            return True
        else:
            return False


class Member:  # Initialize member variables
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_borrowed = []

    def borrow_book(self, book):  # Member can borrow book
        if book.check_availability():
            self.books_borrowed.append(book)
            book.available_copies -= 1
        else:
            print('Book is currently unavailable.')  # If there is none left it will execute this

    def return_book(self, book):  # Borrow back to return
        self.books_borrowed.remove(book)
        book.available_copies += 1  # Add in the library memory bank again (how many)


class Library(Book):  # Initialize library variables
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, ISBN, available_copies):  # Add a book in the library memory bank
        self.books.append(Book(title, author, ISBN, available_copies))  # A book has four elements
        print(f'Added {title} to the library.')

    def search_book(self, book_title):  # Search for a book in the library
        for book in self.books:
            if book.title.lower() == book_title.lower(): # Do not have to type the uppercase characters for book title
                return book
        print('Book not found.')  # If there is no book in the memory bank the system will tell you
        return None

    def add_member(self, name, member_id):  # Add a new member in the library management
        self.members.append(Member(name, member_id))  # Must have the member name and the id number
        print(f'Added {name} to the library.')

    def display_members(self):  # Displays the details of all library members.
        for member in self.members:
            print(f'Name: {member.name}\nID: {member.member_id}')

    def display_books(self):  # Displays the details of all books in the library
        for book in self.books:
            book.display_details()