import tkinter as tk
from tkinter import messagebox, ttk

class SearchableComboBox(tk.Frame):
    """Entry + floating Toplevel Listbox searchable dropdown.
       - Filters while typing (substring match)
       - Backspace works
       - Arrow/down enters listbox; Enter selects; Escape hides
       - On focus-out, exact matches are kept; otherwise fallback to 'Others' (if present)
    """
    def __init__(self, master, options, width=28, font=None, listbox_height=6):
        super().__init__(master)
        self.options = list(options)
        self.filtered = self.options.copy()
        self._font = font
        self._listbox_height = listbox_height

        # StringVar + Entry (visible widget)
        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var, width=width, font=self._font, bd=3, relief="groove")
        self.entry.pack(fill="x")

        # Bindings for typing and navigation
        self.entry.bind("<KeyRelease>", self._on_keyrelease)
        self.entry.bind("<Down>", lambda e: self._focus_listbox())
        self.entry.bind("<FocusIn>", self._on_focusin)
        self.entry.bind("<FocusOut>", self._on_focusout)

        # Dropdown Toplevel & Listbox (created lazily)
        self._dropdown = None
        self._listbox = None
        self._after_id = None

    def _create_dropdown(self):
        if self._dropdown:
            return
        self._dropdown = tk.Toplevel(self)
        self._dropdown.wm_overrideredirect(True)
        self._dropdown.wm_attributes("-topmost", True)
        # frame holds listbox + scrollbar
        frame = tk.Frame(self._dropdown, bd=1, relief="solid")
        frame.pack(fill="both", expand=True)
        self._listbox = tk.Listbox(frame, height=self._listbox_height, font=self._font, activestyle="none")
        sb = tk.Scrollbar(frame, orient="vertical", command=self._listbox.yview)
        self._listbox.config(yscrollcommand=sb.set)
        sb.pack(side="right", fill="y")
        self._listbox.pack(side="left", fill="both", expand=True)

        # Listbox bindings
        self._listbox.bind("<<ListboxSelect>>", self._on_listbox_select)
        self._listbox.bind("<Return>", lambda e: (self._on_listbox_select(), "break"))
        self._listbox.bind("<Escape>", lambda e: self.hide_dropdown())
        self._listbox.bind("<FocusOut>", lambda e: self._schedule_hide())
        # Arrow key navigation inside listbox
        self._listbox.bind("<Down>", self._on_arrow_down)
        self._listbox.bind("<Up>", self._on_arrow_up)


    def _on_keyrelease(self, event):
        key = event.keysym
        # let navigation keys pass to listbox / navigation logic
        if key in ("Up", "Down", "Return", "Escape", "Tab"):
            if key == "Down":
                self._focus_listbox()
            return

        typed = self.var.get().strip().lower()
        if typed == "":
            self.filtered = self.options.copy()
        else:
            # substring match (case-insensitive)
            self.filtered = [opt for opt in self.options if typed in opt.lower()]
        self.show_dropdown()

    def show_dropdown(self):
        # create dropdown UI if needed
        self._create_dropdown()
        # populate listbox
        self._listbox.delete(0, tk.END)
        for opt in self.filtered:
            self._listbox.insert(tk.END, opt)

        # if no match and 'Others' exists, show it as choice
        if not self.filtered and any(o.lower() == "others" for o in self.options):
            self._listbox.insert(tk.END, [o for o in self.options if o.lower() == "others"][0])

        # position the dropdown Toplevel under the entry (screen coords)
        self.update_idletasks()
        x = self.entry.winfo_rootx()
        y = self.entry.winfo_rooty() + self.entry.winfo_height()
        width = self.entry.winfo_width()
        # ensure listbox requested height
        self._listbox.update_idletasks()
        height = self._listbox.winfo_reqheight()
        self._dropdown.geometry(f"{width}x{height}+{x}+{y}")
        self._dropdown.deiconify()
        self._dropdown.lift()
        # cancel any pending hide
        if self._after_id:
            self.after_cancel(self._after_id)
            self._after_id = None

    def hide_dropdown(self):
        if self._dropdown:
            self._dropdown.withdraw()

    def _focus_listbox(self):
        if not self._listbox:
            return
        if self._listbox.size() == 0:
            return
        self._listbox.focus_set()
        self._listbox.selection_clear(0, tk.END)
        self._listbox.selection_set(0)
        self._listbox.activate(0)

    def _on_listbox_select(self, event=None):
        if not self._listbox:
            return
        sel = self._listbox.curselection()
        if not sel:
            return
        value = self._listbox.get(sel[0])

        # Set value into entry
        self.set(value)

        # Schedule dropdown hide slightly later to ensure no focus conflict
        self.after(100, self.hide_dropdown)

        # Return focus to entry
        self.entry.focus_set()


    def _on_focusin(self, event=None):
        # show all options when field gets focus
        self.filtered = self.options.copy()
        self.show_dropdown()

    def _on_focusout(self, event=None):
        """Handle focus leaving the Entry."""
        # If focus is moving into the dropdown or its listbox — don't hide
        next_widget = self.entry.tk_focusNext()
        current_focus = self.entry.focus_get()
        if self._dropdown and self._dropdown.winfo_exists():
            if current_focus in (self._dropdown, self._listbox):
                return  # don't hide if focus is inside dropdown

        # Otherwise, schedule normal hiding
        self._schedule_hide()


    def _schedule_hide(self):
        # small delay to allow listbox click to register
        if self._after_id:
            self.after_cancel(self._after_id)
        self._after_id = self.after(150, self._finalize_focusout)

    def _finalize_focusout(self):
        self._after_id = None
        text = self.get().strip()
        if text == "":
            self.hide_dropdown()
            return
        # exact match?
        matches = [o for o in self.options if o.lower() == text.lower()]
        if matches:
            self.set(matches[0])   # normalize capitalization
        else:
            # fallback to 'Others' if present
            for o in self.options:
                if o.lower() == "others":
                    self.set(o)
                    break
        self.hide_dropdown()

    # convenience methods like an Entry
    def get(self):
        return self.var.get()

    def set(self, value):
        self.var.set(value)

    def delete(self, start, end=None):
        self.entry.delete(start, end)

    def _on_arrow_down(self, event):
        if not self._listbox:
            return
        cur = self._listbox.curselection()
        if not cur:
            idx = 0
        else:
            idx = min(cur[0] + 1, self._listbox.size() - 1)
        self._listbox.selection_clear(0, tk.END)
        self._listbox.selection_set(idx)
        self._listbox.activate(idx)
        self._listbox.see(idx)
        return "break"  # prevent default bell sound

    def _on_arrow_up(self, event):
        if not self._listbox:
            return
        cur = self._listbox.curselection()
        if not cur:
            idx = 0
        else:
            idx = max(cur[0] - 1, 0)
        self._listbox.selection_clear(0, tk.END)
        self._listbox.selection_set(idx)
        self._listbox.activate(idx)
        self._listbox.see(idx)
        return "break"