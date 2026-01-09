# Book Manager CLI - Appunti

## Cosa vogliamo fare

- Un'app da terminale per gestire la propria libreria personale, in Python
- I libri vengono aggiunti manualmente da terminale
- Usiamo Gemini per suggerire nuovi libri basandosi su quelli già letti
- I dati li salviamo in `db.json` nella stessa cartella dello script

## API da usare

- **Gemini** — per generare suggerimenti di lettura basati sui libri letti

## Concetti principali

- **Libro** — un libro con titolo, autore, genere, etc.
- **Stato** — lo stato di lettura: "da leggere", "in lettura", "completato"
- **Valutazione** — voto da 1 a 5 stelle per libri completati

## Cosa deve fare

### Libri
- aggiungere un libro (titolo, autore, genere, pagine)
- vedere tutti i libri
- vedere dettaglio di un libro
- modificare un libro
- cancellare un libro

### Stato lettura
- segnare libro come "da leggere"
- segnare libro come "in lettura" (con pagina corrente)
- segnare libro come "completato" (con valutazione)
- aggiornare pagina corrente

### AI Features
- chiedere a Gemini suggerimenti di nuovi libri basati su quelli letti
- chiedere a Gemini suggerimenti basati su un genere preferito

### Statistiche
- totale libri in libreria
- libri per stato (da leggere, in lettura, completati)
- pagine totali lette
- media valutazioni

## Struttura dati

```json
{
  "books": [
    {
      "id": "uuid",
      "title": "1984",
      "author": "George Orwell",
      "genre": "Distopico",
      "pages": 328,
      "status": "done",
      "current_page": 328,
      "rating": 5,
      "added_at": "2025-01-09T10:30:00",
      "finished_at": "2025-01-15T00:00:00"
    }
  ]
}
```

## Note

- Se `db.json` non esiste, crearlo vuoto al primo avvio
- Status validi: "todo", "reading", "done"
- Rating da 1 a 5 (solo per libri completati)
- Il prompt a Gemini deve includere titoli, autori, generi e valutazioni dei libri letti per dare suggerimenti sensati
- Output leggibile con emoji:
  - 📚 lista libri
  - 📖 in lettura
  - ✅ completato
  - 📋 da leggere
  - ⭐ rating
- Mostrare progresso lettura (es: "pag. 145/328 - 44%")
- Messaggi chiari per errori (libro non trovato, rating non valido, etc.)
