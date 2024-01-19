class Library:
    def __init__(self, books):
        self.available_books = books

    def displayAvailableBooks(self):
        print("Available Books:")
        for book in self.available_books:
            print(book)

    def borrowBook(self, book_title):
        if book_title in self.available_books:
            print(f"You have successfully borrowed '{book_title}'.")
            self.available_books.remove(book_title)
        else:
            print(f"Sorry, '{book_title}' is not available for borrowing.")

    def returnBook(self, book_title):
        self.available_books.append(book_title)
        print(f"Thanks for returning '{book_title}'. We hope you enjoyed reading it!")


class Student:
    def requestBook(self):
        return input("Enter the title of the book you want to borrow: ")

    def returnBook(self):
        return input("Enter the title of the book you want to return: ")


if __name__ == "__main__":
    # Initialize Library
    library_books = ["Introduction to Python", "Data Science Essentials", "Algorithm Design"]
    library = Library(library_books)

    # Create Student
    student = Student()

    while True:
        print("\nLibrary Menu:")
        print("1. List all books")
        print("2. Request a book")
        print("3. Return a book")
        print("4. Exit the Library")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            library.displayAvailableBooks()
        elif choice == "2":
            book_to_borrow = student.requestBook()
            library.borrowBook(book_to_borrow)
        elif choice == "3":
            book_to_return = student.returnBook()
            library.returnBook(book_to_return)
        elif choice == "4":
            print("Exiting the Library. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
