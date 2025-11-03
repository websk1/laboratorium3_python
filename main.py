from library import *
def main():
    library = Library()

    while True:
        # Wyświetlanie menu
        print("\nWybierz akcję")
        print("1. Dodaj książkę")
        print("2. Wyświetl książki")
        print("3. Wyszukaj książkę po tytule")
        print("4. Wypożycz książkę")
        print("5. Zwróć książkę")
        print("6. Zakończ\n")

        choice = input("Wybierz opcję (1–6): ").strip()

        # Tworzenie obiektu książki i dodanie do biblioteki
        if choice == "1":
            title = input("Tytuł: ").strip()
            author = input("Autor: ").strip()
            year = input("Rok wydania: ").strip()
            if not year.isdigit():
                print("Rok musi być liczbą!")
                continue
            book = Book(title, author, int(year))
            print(library.add_book(book))

        # Wypisanie książek
        elif choice == "2":
            books = library.list_books()
            if not books:
                print("Brak książek w bibliotece.")
            else:
                print("\nLista książek:")
                i = 0
                for book in books:
                    i += 1
                    print(f"{i}. {book}")

        #Szukanie książki po tytule
        elif choice == "3":
            title = input("Podaj tytuł książki: ").strip()
            book = library.find_by_title(title)
            if book:
                print(f"Znaleziono: {book}")
            else:
                print("Nie znaleziono takiej książki.")

        # Wypożyczanie ksiązki po tytule
        elif choice == "4":
            title = input("Podaj tytuł książki do wypożyczenia: ").strip()
            print(library.borrow_book(title))

        # Zwrot ksiązki po tytule
        elif choice == "5":
            title = input("Podaj tytuł książki do zwrotu: ").strip()
            print(library.return_book(title))

        # Koniec
        elif choice == "6":
            print("Zakończono.")
            break

        else:
            print(f"Akcja {choice} nie istnieje. Spróbuj ponownie.")

        input('\nWciśnij Enter, aby kontunuować')



if __name__ == "__main__":
    main()