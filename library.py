class Book:
    def __init__(self, title: str, author: str, year: int, is_available: bool = True):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

    def borrow_book(self) -> bool:
        # Wypożycza książkę, jeśli jest dostępna
        if self.is_available:
            self.is_available = False
            # Została wypożyczona
            return True
        # Jest już wypożyczona
        return False


    def return_book(self) -> bool:
        # Zwraca książkę, jeśli nie jest dostępna
        if not self.is_available:
            self.is_available = True
            # Została zwrócona
            return True
        # Jest już dostępna
        return False

    def __str__(self) -> str:
        status = "dostępna" if self.is_available else "wypożyczona"
        return f"'{self.title}' – {self.author}, {self.year} ({status})"


class Library:
    def __init__(self):
        self.books: list[Book] = []

    def add_book(self, book: Book) -> str:
        # Dodaje książkę do zbioru
        self.books.append(book)
        return f"Dodano: {book}"

    def list_books(self) -> list[Book]:
        # Zwraca listę wszystkich książek
        return self.books

    def find_by_title(self, title: str) -> Book | None:
        # Wyszukuje książkę po tytule.
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, title: str) -> str:
        # Wypożycza książkę po tytule
        book = self.find_by_title(title)
        if not book:
            return f"Książka o tytule '{title}' nie została znaleziona."
        if book.borrow_book():
            return f"Wypożyczono: {book}"
        else: return f"Książka '{book.title}' jest już wypożyczona."

    def return_book(self, title: str) -> str:
        # Zwraca książkę po tytule
        book = self.find_by_title(title)
        if not book:
            return f"Książka o tytule '{title}' nie została znaleziona."
        if book.return_book():
            return f"Zwrócono: {book}"
        else: return f"Książka {book.title} jest już zwrócona."
