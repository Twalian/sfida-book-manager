import json
import os
from typing import List, Dict, Optional

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'db', 'db.json')

def init_db():
    """Ensures the db file exists and is a valid JSON."""
    if not os.path.exists(DB_PATH):
        save_data({"books": []})
    else:
        try:
            with open(DB_PATH, 'r') as f:
                json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            save_data({"books": []})

def load_data() -> Dict:
    """Loads the entire database."""
    init_db()
    with open(DB_PATH, 'r') as f:
        return json.load(f)

def save_data(data: Dict):
    """Saves the entire database."""
    with open(DB_PATH, 'w') as f:
        json.dump(data, f, indent=2)

def get_books() -> List[Dict]:
    """Returns the list of all books."""
    data = load_data()
    return data.get("books", [])

def add_book_to_db(book: Dict):
    """Adds a single book to the database."""
    data = load_data()
    data["books"].append(book)
    save_data(data)

def update_book_in_db(updated_book: Dict):
    """Updates a book in the database matching by ID."""
    data = load_data()
    for i, book in enumerate(data["books"]):
        if book["id"] == updated_book["id"]:
            data["books"][i] = updated_book
            break
    save_data(data)

def delete_book_from_db(book_id: str):
    """Deletes a book by ID."""
    data = load_data()
    data["books"] = [b for b in data["books"] if b["id"] != book_id]
    save_data(data)

def find_book_by_id(book_id: str) -> Optional[Dict]:
    """Finds a book by ID."""
    books = get_books()
    for book in books:
        if book["id"] == book_id:
            return book
    return None

def find_book_by_genre(genre: str) -> Optional[Dict]:
    """Finds a book by ID."""
    books = get_books()
    for book in books:
        if book["genre"] == genre:
            return book
    return None
