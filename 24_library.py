class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.borrower = None # Atributo para almacenar el usuario que toma prestado el libro
    
    def borrow(self, user):
        if self.is_available:
            self.is_available = False
            self.borrower = user.name # Guardamos el nombre del usuario que tiene el libro
            print(f"El libro '{self.title}' ha sido prestado a {self.borrower}.")
        else:
            print(f"El libro '{self.title}' no está disponible. Lo tiene {self.borrower}.")
    
    def return_book(self):
        self.is_available = True
        print(f"El libro '{self.title}' ha sido devuelto por {self.borrower}.")
        self.borrower = None # Limpiamos el usuario que tenía el libro

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow(self) # Pasamos los atributos de la clase 'User' al método 'borrow' de la clase 'Book'. (name, user_id)
            self.borrowed_books.append(book)
        else:
            print(f"El libro '{book.title}' no está disponible.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro '{book.title}' no está en la lista de préstamos.")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro '{book.title}' ha sido añadido a la biblioteca.")
    
    def add_user(self, user):
        self.users.append(user)
        print(f"El usuario '{user.name}' ha sido añadido a la base de datos.")
    
    def list_books(self):
        print(f"Los libros disponibles son:")
        for book in self.books:
            if book.is_available:
                print(f"{book.title} / {book.author}.")

# Añadimos libros de la biblioteca
book1 = Book("Cien años de soledad", "Gabriel García Márquez")
book2 = Book("1984", "George Orwell")
book3 = Book("El Principito", "Antoine de Saint-Exupéry")

# Añadimos usuarios de la biblioteca
user1 = User("Juan Pérez", 1)
user2 = User("María López", 2)

# Creamos una instancia de la biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_user(user1)
library.add_user(user2)

# Mostramos los libros disponibles
library.list_books()

# Juan Pérez intenta pedir prestado "Cien años de soledad"
user1.borrow_book(book1)

# Mostramos los nuevos libros disponibles
library.list_books()

# Juan Pérez devuelve el libro "Cien años de soledad"
user1.return_book(book1)

# Mostramos los nuevos libros disponibles
library.list_books()