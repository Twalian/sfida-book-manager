import os
import sys

# Ensure we can import from src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src import data, ui, books, ai, stats

def handle_book_actions(book_id):
    while True:
        book = data.find_book_by_id(book_id)
        if not book:
            ui.print_error("Libro non trovato!")
            break
            
        ui.print_book_details(book)
        choice = ui.get_input("Scelta:").upper()
        
        if choice == 'I':
            break
        elif choice == 'C':
            confirm = ui.get_input("Sei sicuro? (s/n):")
            if confirm.lower() == 's':
                books.remove_book(book_id)
                ui.print_success("Libro cancellato.")
            break
        elif choice == 'M':
            print("1. Da Leggere")
            print("2. In Lettura")
            print("3. Completato")
            status_choice = ui.get_input("Nuovo stato:")
            
            try:
                if status_choice == '1':
                    books.set_book_status(book_id, "todo")
                elif status_choice == '2':
                    books.set_book_status(book_id, "reading")
                    page = int(ui.get_input("A che pagina sei arrivato?"))
                    books.update_reading_progress(book_id, page)
                elif status_choice == '3':
                    books.set_book_status(book_id, "done")
                    rating = ui.get_input("Vuoi dare un voto (1-5)? (invio per saltare)")
                    if rating:
                        books.rate_book(book_id, int(rating))
                ui.print_success("Aggiornato!")
            except ValueError as e:
                ui.print_error(str(e))
                
        elif choice == 'V':
            if book['status'] != 'done':
                 # Auto complete if rating
                 pass
            try:
                rating = int(ui.get_input("Voto (1-5):"))
                books.rate_book(book_id, rating)
                ui.print_success("Valutazione salvata!")
            except ValueError as e:
                ui.print_error(str(e))

def main():
    data.init_db()
    
    # Check for API KEY
    if not os.getenv("GEMINI_API_KEY"):
        ui.print_message("⚠️  GEMINI_API_KEY non trovata. Le funzioni AI non funzioneranno completamente.")

    ui.print_header()
    
    while True:
        ui.print_menu()
        choice = ui.get_input("Scegli un'opzione:")
        
        if choice == '0':
            print("👋 Ciao e buona lettura!")
            break
            
        elif choice == '1': # Add book
            t, a, g, p = ui.ask_book_details()
            books.add_new_book(t, a, g, p)
            ui.print_success("Libro aggiunto!")
            
        elif choice == '2': # Listing all
            all_books = books.get_all_books()
            ui.print_book_list(all_books, "I miei libri")
            
        elif choice == '3': # Todo
            bks = [b for b in books.get_all_books() if b['status'] == 'todo']
            ui.print_book_list(bks, "Da Leggere")
            
        elif choice == '4': # Reading
            bks = [b for b in books.get_all_books() if b['status'] == 'reading']
            ui.print_book_list(bks, "In Lettura")
            
        elif choice == '5': # Done
            bks = [b for b in books.get_all_books() if b['status'] == 'done']
            ui.print_book_list(bks, "Completati")
            
        elif choice == '6': # Manage
            all_books = books.get_all_books()
            if not all_books:
                ui.print_message("Nessun libro da gestire.")
                continue
                
            ui.print_book_list(all_books)
            idx_str = ui.get_input("Inserisci il NUMERO del libro da gestire (0 per annullare):")
            try:
                idx = int(idx_str)
                if idx > 0 and idx <= len(all_books):
                    selected_book = all_books[idx-1]
                    handle_book_actions(selected_book["id"])
            except ValueError:
                ui.print_error("Numero non valido.")

        elif choice == '7': # AI Suggestions
            ui.print_message("Sto chiedendo a Gemini...")
            all_books = books.get_all_books()
            sugg = ai.get_suggestions(all_books)
            print("\n✨ --- SUGGERIMENTI AI --- ✨")
            print(sugg)
            print("--------------------------\n")
            
        elif choice == '8': # AI Genre
            genre = ui.get_input("Che genere ti interessa?")
            ui.print_message(f"Sto chiedendo consigli per '{genre}'...")
            sugg = ai.get_genre_suggestions(genre)
            print(f"\n✨ --- SUGGERIMENTI PER {genre.upper()} --- ✨")
            print(sugg)
            print("--------------------------\n")
            
        elif choice == '9': # Stats
            s = stats.calculate_stats(books.get_all_books())
            print("\n📊 --- STATISTICHE ---")
            print(f"Totale libri: {s['total_books']}")
            print(f"Da leggere: {s['by_status']['todo']}")
            print(f"In lettura: {s['by_status']['reading']}")
            print(f"Completati: {s['by_status']['done']}")
            print(f"Totale pagine lette: {s['total_pages_read']}")
            print(f"Voto medio: {s['average_rating']:.2f}/5")
            print("--------------------\n")
            
        else:
            ui.print_error("Scelta non valida.")

if __name__ == "__main__":
    main()
