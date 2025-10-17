# Registration-Management-System

# Tkinter Badge Printer

Desktop registration app (Tkinter) for event badge creation and printing.
This repo contains the attendee registration GUI and badge PDF generation.

## Features
- Keyboard-first Tkinter GUI
- SQLite database (auto-create)
- PDF badge generation using ReportLab
- Print via `win32api.ShellExecute` (Windows)
  
---

## Quick start (Windows)

1. Clone repo:
```bash
git clone https://github.com/WAHVZ/Registration-Management-System.git
cd Registration-Management-System

2. Create a Python virtual environment (Windows PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1  # or use activate.bat in cmd

3. Install dependencies:
pip install --upgrade pip
pip install -r requirements.txt

4. Run the app:
python app/visitors.py

