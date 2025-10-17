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
```

2. Create a Python virtual environment (Windows PowerShell):
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # or use activate.bat in cmd
```  

3. Install dependencies:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Run the app:
```bash
python app/visitors.py
```

## Files & how they work
### Visitors.py — Main application / GUI
  Purpose: Launches the Tkinter registration GUI, handles user input, validation, database I/O, badge generation and focus/UX logic.
    Notes:
  - Resource files (background, logo, font) are referenced with hardcoded relative paths (Resources/bg.jpg, etc.). Ensure those files exist in that location.
  - Don't forget to extract the font from its zip, download and mention its path at line 172.
  - Printing (win32api) was removed here — badge generation uses helper.generate_badge() which writes to local disk. If you enable printing, pywin32 is required and it is Windows-only. The printer should be connected and set to default.
  - The visitor_count is not persisted; restarting app resets it. If you want persistent counts, store in DB or a file.

    Changes to be done:
    - Name your own database file and table name at line 8 and 9.
    - To enable printing function, comment-out line 88 and uncomment 89 and 90.
    - Logo image path at line 188 and background image path at line 165.
    - Should this app be called in a local environment, then the terminal/ powershell path must be inside the parent folder, App.

### widgets.py — SearchableComboBox widget
  Purpose: A custom widget that behaves like an autocomplete/searchable combobox implemented as a tk.Frame with an Entry and a floating Toplevel + Listbox dropdown.

### helper.py — helpers for cleaning, truncation and PDF generation
  Purpose: Shared utility functions used by the main app: name cleaning, truncation logic, and badge PDF generation.

   Changes to be made:
   - set correct path to your folder, where the badges/ pdfs will be saved at line 67.



 Make sure all the files are in the same parent folder, App.
