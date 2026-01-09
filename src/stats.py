from typing import List, Dict

def calculate_stats(books: List[Dict]) -> Dict:
    """Calculates statistics for the library."""
    total_books = len(books)
    status_counts = {"todo": 0, "reading": 0, "done": 0}
    total_pages_read = 0
    total_ratings = 0
    rated_books_count = 0

    for book in books:
        status = book.get("status", "todo")
        if status in status_counts:
            status_counts[status] += 1
            
        # Count pages read
        current_page = book.get("current_page", 0)
        total_pages_read += current_page
        
        # Calculate average rating
        if status == "done" and book.get("rating"):
            total_ratings += book["rating"]
            rated_books_count += 1

    avg_rating = 0
    if rated_books_count > 0:
        avg_rating = total_ratings / rated_books_count

    return {
        "total_books": total_books,
        "by_status": status_counts,
        "total_pages_read": total_pages_read,
        "average_rating": avg_rating
    }
