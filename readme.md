# Gestione Libreria Personale da Terminale (Python)

## Descrizione del progetto

Questo progetto Python consente di gestire la propria **libreria personale direttamente da terminale**.
L’applicazione è pensata per chi desidera tenere traccia dei libri letti, di quelli in corso e di quelli da leggere, con funzionalità di analisi e suggerimento intelligente.

Il sistema utilizza **Gemini** per proporre nuovi libri sulla base delle letture già effettuate, migliorando l’esperienza di scoperta di nuovi titoli.

---

## Prerequisiti

Prima di avviare lo script è necessario eseguire **obbligatoriamente** i seguenti passaggi:

1. Installare le dipendenze del progetto:
   pip install -r requirements.txt

2. Impostare la variabile d’ambiente per l’API di Gemini:
   export GEMINI_API_KEY="your_actual_api_key"

Assicurati di sostituire `your_actual_api_key` con la tua chiave API reale.

---

## Funzionalità principali

Lo script permette di:

* **Aggiungere libri manualmente da terminale**
* **Aggiornare lo stato di lettura** di ciascun libro:

  * Da leggere
  * In lettura
  * Completato
* **Assegnare una valutazione** ai libri letti
* **Ricevere suggerimenti di nuovi libri** tramite Gemini, basati sui titoli già presenti nella libreria

---

## Statistiche disponibili

L’applicazione consente di ottenere statistiche aggregate sulla propria libreria, tra cui:

* Numero totale di libri in libreria
* Distribuzione dei libri per stato di lettura:

  * Da leggere
  * In lettura
  * Completati
* Totale delle pagine lette
* Media delle valutazioni assegnate ai libri

---

## Obiettivo del progetto

L’obiettivo è fornire uno strumento semplice, utilizzabile da terminale, per **organizzare, monitorare e analizzare le proprie abitudini di lettura**, integrando funzionalità di intelligenza artificiale per il supporto alle scelte future.

---

Buona lettura e buona gestione della tua libreria personale!