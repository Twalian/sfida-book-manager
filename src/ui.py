from typing import List, Dict

def print_header():
    print("\n" + "="*40)
    print(" 📚  BOOK MANAGER CLI  📚 ")
    print("="*40 + "\n")

def print_menu():
    print("------- MENU -------")
    print("1. ➕ Aggiungi un libro")
    print("2. 📚 I miei libri (Tutti)")
    print("3. 📋 Da Leggere")
    print("4. 📖 In Lettura")
    print("5. ✅ Completati")
    print("6. 🔍 Cerca/Gestisci libro (dettagli, modifica, cancella)")
    print("7. ✨ Suggerimenti AI (dalle letture)")
    print("8. 🎭 Suggerimenti AI (per genere)")
    print("9. 📊 Statistiche")
    print("0. 👋 Esci")
    print("--------------------")

def get_input(prompt: str) -> str:
    return input(prompt + " ")

def print_error(message: str):
    print(f"\n❌ ERRORE: {message}\n")

def print_success(message: str):
    print(f"\n✅ {message}\n")

def print_message(message: str):
    print(f"\nℹ️  {message}\n")

def format_book_oneline(book: Dict) -> str:
    status_emoji = {
        "todo": "📋",
        "reading": "📖",
        "done": "✅"
    }
    emoji = status_emoji.get(book["status"], "❓")
    rating = f"{'⭐' * book['rating']}" if book['rating'] else ""
    return f"{emoji} {book['title']} - {book['author']} {rating}"

def print_book_list(books: List[Dict], title: str = "Lista Libri"):
    if not books:
        print_message(f"{title}: Nessun libro trovato.")
        return

    print(f"\n--- {title} ({len(books)}) ---")
    for i, book in enumerate(books):
        print(f"{i+1}. {format_book_oneline(book)}")
    print("")

def print_book_details(book: Dict):
    print("\n--------------------------------")
    print(f"📖 TITOLO: {book['title']}")
    print(f"✍️  AUTORE: {book['author']}")
    print(f"🎭 GENERE: {book['genre']}")
    print(f"📄 PAGINE: {book['current_page']} / {book['pages']}")
    
    # Progress bar
    if book['pages'] > 0:
        percent = int((book['current_page'] / book['pages']) * 100)
        bar_len = 20
        filled = int(bar_len * percent / 100)
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"   [{bar}] {percent}%")
    
    status_map = {"todo": "Da leggere", "reading": "In lettura", "done": "Completato"}
    print(f"📌 STATO: {status_map.get(book['status'], book['status'])}")
    
    if book['rating']:
        print(f"⭐ RATING: {book['rating']}/5")
        
    print(f"📅 AGGIUNTO IL: {book['added_at']}")
    if book['finished_at']:
        print(f"🏁 FINITO IL: {book['finished_at']}")
    print("--------------------------------\n")
    print("OPZIONI:")
    print("M. Modifica stato/pagina")
    print("C. Cancella libro")
    print("V. Valuta (solo se completato)")
    print("I. Indietro")

def ask_book_details():
    print("\n--- NUOVO LIBRO ---")
    title = input("Titolo: ")
    author = input("Autore: ")
    genre = input("Genere: ")
    while True:
        try:
            pages = int(input("Numero pagine: "))
            if pages > 0:
                break
            print("Le pagine devono essere maggiori di 0.")
        except ValueError:
            print("Inserisci un numero valido.")
    return title, author, genre, pages
