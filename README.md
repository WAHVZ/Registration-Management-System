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

<img width="1919" height="1019" alt="Image" src="https://github.com/user-attachments/assets/ad297ad9-a433-4bc5-bd06-8aeb746830dc" />

## Quick start (Windows)

You can run the registration system either in a virtual environment (recommended) or directly on your system.

### Option 1 — Virtual Environment
Keeps dependencies isolated from other Python projects.
```bash
git clone https://github.com/WAHVZ/Registration-Management-System.git
cd RMS
python -m venv venv
venv\Scripts\activate   # (Windows)
 #or source venv/bin/activate  (macOS/Linux)
pip install -r requirements.txt
python Visitors.py
```

### Option 2 — Run Locally (for normal users)
If you just want to run it directly:
```bash
git clone https://github.com/WAHVZ/Registration-Management-System.git
cd RMS
pip install -r requirements.txt
python Visitors.py
```

💡 Tip: On Windows, you can also open the folder in VS Code, open the terminal (Ctrl+), and run python Visitors.py`.
✅ Requirements
- Python 3.13 or later,
- Internet connection (for first-time dependency installation),
- The Resources folder (background, logo, etc.) must exist in the same directory.

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
