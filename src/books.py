from datetime import datetime
import uuid
from typing import Dict, Optional, List
from src import data

def create_book_entry(title: str, author: str, genre: str, pages: int) -> Dict:
    """Creates a new book dictionary with default values."""
    return {
        "id": str(uuid.uuid4()),
        "title": title,
        "author": author,
        "genre": genre,
        "pages": pages,
        "status": "todo",  # todo, reading, done
        "current_page": 0,
        "rating": None,
        "added_at": datetime.now().isoformat(),
        "finished_at": None
    }

def add_new_book(title: str, author: str, genre: str, pages: int) -> Dict:
    """High-level function to clean input and add book to DB."""
    book = create_book_entry(title.strip(), author.strip(), genre.strip(), pages)
    data.add_book_to_db(book)
    return book

def get_all_books() -> List[Dict]:
    return data.get_books()

def set_book_status(book_id: str, status: str):
    """Updates the reading status of a book."""
    book = data.find_book_by_id(book_id)
    if not book:
        return
    
    valid_statuses = ["todo", "reading", "done"]
    if status not in valid_statuses:
        raise ValueError(f"Status must be one of {valid_statuses}")
        
    book["status"] = status
    if status == "done":
        book["finished_at"] = datetime.now().isoformat()
        book["current_page"] = book["pages"] # Auto-complete pages
    elif status == "reading" and book["current_page"] == 0:
        book["current_page"] = 1 # Start at page 1 if just starting
        
    data.update_book_in_db(book)

def update_reading_progress(book_id: str, current_page: int):
    """Updates the current page of a book."""
    book = data.find_book_by_id(book_id)
    if not book:
        return
        
    if current_page < 0 or current_page > book["pages"]:
        raise ValueError(f"Page must be between 0 and {book['pages']}")
        
    book["current_page"] = current_page
    if current_page == book["pages"]:
        book["status"] = "done"
        book["finished_at"] = datetime.now().isoformat()
    elif current_page > 0 and book["status"] == "todo":
        book["status"] = "reading"
        
    data.update_book_in_db(book)

def rate_book(book_id: str, rating: int):
    """Updates the rating of a book."""
    book = data.find_book_by_id(book_id)
    if not book:
        return
    
    if not 1 <= rating <= 5:
        raise ValueError("Rating must be between 1 and 5")
        
    book["rating"] = rating
    # If rating, imply done
    if book["status"] != "done":
        book["status"] = "done"
        book["finished_at"] = datetime.now().isoformat()
        book["current_page"] = book["pages"]
        
    data.update_book_in_db(book)

def remove_book(book_id: str):
    data.delete_book_from_db(book_id)
    

def update_book(book_id: str, author: str, titolo:str, genere:str,pages:int):
    remove_book(book_id)
    add_new_book(titolo,author,genere,pages)

def get_genre_books(genre:str):
    return data.find_book_by_genre(genre)