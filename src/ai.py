import os
import google.generativeai as genai
from typing import List, Dict

# Try to look for an API key in environment variables
API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

def get_read_books_summary(books: List[Dict]) -> str:
    """Formats a list of read books into a string for the prompt."""
    read_books = [b for b in books if b["status"] == "done"]
    if not read_books:
        return ""
    
    summary = "Ho letto e apprezzato i seguenti libri:\n"
    for b in read_books:
        rating = f"{b['rating']}/5 stars" if b.get('rating') else "No rating"
        summary += f"- '{b['title']}' di {b['author']} ({b['genre']}). Valutazione: {rating}\n"
    return summary

def get_suggestions(books: List[Dict]) -> str:
    """Asks Gemini for book suggestions based on reading history."""
    if not API_KEY:
        return "⚠️ Errore: GEMINI_API_KEY non trovata. Imposta la variabile d'ambiente per usare l'AI."

    model = genai.GenerativeModel("gemini-3-flash-preview")
    
    history_summary = get_read_books_summary(books)
    if not history_summary:
        prompt = "Consigliami 3 libri classici da leggere assolutamente. Dimmi titolo, autore e perché leggerlo."
    else:
        prompt = (
            f"{history_summary}\n"
            "Basandoti su questi gusti, consigliami 3 nuovi libri da leggere. "
            "Per ogni libro includi Titolo, Autore e una breve motivazione del perché potrebbe piacermi "
            "in base ai miei gusti precedenti. Non consigliare libri già in lista."
        )

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Errore durante la richiesta a Gemini: {str(e)}"

def get_genre_suggestions(genre: str) -> str:
    """Asks Gemini for suggestions based on a specific genre."""
    if not API_KEY:
        return "⚠️ Errore: GEMINI_API_KEY non trovata."

    model = genai.GenerativeModel("gemini-3-flash-preview")
    prompt = (
        f"Consigliami 3 libri imperdibili del genere '{genre}'. "
        "Per ogni libro includi Titolo, Autore e breve descrizione."
    )

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Errore durante la richiesta a Gemini: {str(e)}"
