class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print("Book not found.")

    def view_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

    def find_book_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if not found_books:
            print(f"No books found with title '{title}'.")
        else:
            for book in found_books:
                print(book)

    def find_book_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if not found_books:
            print(f"No books found by author '{author}'.")
        else:
            for book in found_books:
                print(book)


# Example usage of the Library Management System
if __name__ == "__main__":
    # Create a Library instance
    my_library = Library()

    # Create some Book instances
    book1 = Book("The Catcher in the Rye", "J.D. Salinger", "9780316769488")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")
    book3 = Book("1984", "George Orwell", "9780451524935")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # View all books in the library
    print("\nCurrent books in the library:")
    my_library.view_books()

    # Find a book by title
    print("\nSearching for a book by title:")
    my_library.find_book_by_title("1984")

    # Find books by author
    print("\nSearching for books by author:")
    my_library.find_book_by_author("Harper Lee")

    # Remove a book
    print("\nRemoving a book from the library:")
    my_library.remove_book("9780316769488")

    # View all books in the library after removal
    print("\nBooks in the library after removal:")
    my_library.view_books()
