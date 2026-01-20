# syllabus-sync API

Backend API for **syllabus-sync**, responsible for parsing uploaded syllabi, extracting deadlines using LLMs, and returning structured data to the mobile app.

## Status

✅ **Complete for current use**

The API fully supports the current production workflow:
- Extracting deadlines from syllabus PDFs
- Using **window-based text extraction** to reduce token usage
- Sending extracted chunks to an LLM via API call for structured parsing

The architecture is intentionally flexible and may evolve to support additional features in the future.

---

## Overview

This API is built with **FastAPI** and integrates **LLMs (LLaMA 3.x via Groq API)** to extract academic deadlines from syllabus PDFs.  
It is designed to be consumed by the `syllabus-sync` mobile app (Expo / React Native).

---

## Features (Current & Planned)

- 📄 PDF syllabus upload
- 🧠 LLM-powered text extraction & deadline parsing
- 🗓️ Structured deadline output (JSON)
- 🔳 Window Extraction 
- ⚡ FastAPI async architecture

---

## Deadline Extraction Strategy

To avoid unnecessary token usage, deadline extraction is done in two stages:

1. **Local window extraction**
   - The PDF text is scanned for date-like patterns
   - A fixed-size text window is extracted around each detected date

2. **LLM processing**
   - Only the extracted text windows are sent to the LLM
   - The LLM converts these windows into structured deadline objects

This approach significantly reduces cost

---

## Tech Stack

- **Python**
- **FastAPI**
- **Groq API (LLaMA 3.x)**
- **PyPDF / PDF text extraction**
- **Uvicorn**

---

## API Structure (Planned)

```text
api/
├── main.py
├── models.py
├── utils/
│   └── prompt.py
└── services/
    ├── pdf_parser.py
    ├── window_extractor.py
    └── llm.py

