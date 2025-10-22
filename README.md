# Visitor Registrations for Exhibitions

## Tkinter Badge Printer

Desktop registration app (Tkinter) for event badge creation and printing.
This repo contains the attendee registration GUI and badge PDF generation.

### Features
- Keyboard-first Tkinter GUI
- SQLite database (auto-create)
- PDF badge generation using ReportLab
- Print via `win32api.ShellExecute` (Windows)
  
---

<img width="1919" height="1019" alt="Image" src="https://github.com/user-attachments/assets/ad297ad9-a433-4bc5-bd06-8aeb746830dc" />

### Quick start (Windows)

You can run the registration system either in a virtual environment (recommended) or directly on your system.
Prerequisites:
- Python/ pip,
- git (if you don't have git, you can download it from here:
  https://git-scm.com/install/windows . If you don't want that, you can, alternately, download the zip file of this app.

#### If working with git:
##### Open Command prompt:
```bash
cd Desktop
python -m pip install --upgrade pip
git clone https://github.com/WAHVZ/Visitor-Registrations-For-Exhibitions.git
cd Visitor-Registrations-For-Exhibitions
```
If you want to run this in Virtual Environment:
Make a virtual environment. Keeps dependencies isolated from other Python projects.
```bash
python -m venv venv
venv\Scripts\activate   # (Windows)
 #or source venv/bin/activate  (macOS/Linux)
```
Continue:
```bash
pip install -r requirements.txt
```
#### If you downloaded the zip file:
- Open the file in the Downloads folder,
- Select it and Cut/ paste it to desktop,
##### Open Command Prompt:
```bash
python -m pip install --upgrade pip
cd Desktop
cd Visitor-Registrations-For-Exhibitions-main
pip install -r requirements.txt
```
Now open App/ Resources, extract the contents of the zip file of the font, contantia. Open the truetype font file and install the font. Alternately, you can set any other font you want. Copy its path.
Now open App/ Visitors.py in any file editor like VS Code etc.
Go to line line 183 and paste the font path there.

After this, open helper.py. Go to line 67 and set this path to the path to your parent folder, App. This is where your badges folder will be created and badges/ pdfs will be saved.

Lastly, go to the parent folder, App. Right-click --> Properties --> Attributes: Uncheck 'Read-only" box. Click Apply. Click OK. 

Finally, run the file Visitors.py:
In VS Code/ CMD:
```bash
python Visitors.py
```

💡 Tip: On Windows, you can also open the folder in VS Code, open the terminal (Ctrl+), and run python Visitors.py`.
✅ Requirements
- Python 3.13 or later,
- Internet connection (for first-time dependency installation),
- The Resources folder (background, logo, etc.) must exist in the same directory.

### Files & how they work
#### Visitors.py — Main application / GUI
  Purpose: Launches the Tkinter registration GUI, handles user input, validation, database I/O, badge generation and focus/UX logic.
    Notes:
  - Resource files (background, logo, font) are referenced with hardcoded relative paths (Resources/bg.jpg, etc.). Ensure those files exist in that location.
  - Don't forget to extract the font from its zip, download and mention its path at line 172.
  - Printing (win32api) was removed here — badge generation uses helper.generate_badge() which writes to local disk. If you enable printing, pywin32 is required and it is Windows-only. The printer should be connected and set to default.
  - The visitor_count is not persisted; restarting app resets it. If you want persistent counts, store in DB or a file.

    Changes to be done:
    - Name your own database file and table name at line 8 and 9.
    - To enable printing function, comment-out line 99 and uncomment 100 and 101.
    - Should this app be called in a local environment, then the terminal/ powershell path must be inside the parent folder, App.

#### widgets.py — SearchableComboBox widget
  Purpose: A custom widget that behaves like an autocomplete/searchable combobox implemented as a tk.Frame with an Entry and a floating Toplevel + Listbox dropdown.

#### helper.py — helpers for cleaning, truncation and PDF generation
  Purpose: Shared utility functions used by the main app: name cleaning, truncation logic, and badge PDF generation.

  Changes to be made:
  - set correct path to your folder, where the badges/ pdfs will be saved at line 67.
  
  Make sure all the files are in the same parent folder, App.
  Make sure to slash  (/) and not the back-slash (\) while setting paths.

