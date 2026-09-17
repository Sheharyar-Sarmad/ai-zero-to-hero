import tkinter as tk
from tkinter import filedialog, colorchooser
import tkinter.font as tkFont

# ================= MAIN WINDOW =================

root = tk.Tk()
root.title("Professional Text Editor")
root.geometry("1000x700")
root.configure(bg="#1e1e1e")

current_file = None

# ================= BASE FONT =================

base_font = tkFont.Font(family="Consolas", size=14)

# ================= FUNCTIONS =================

def new_file():
    global current_file
    text.delete(1.0, tk.END)
    current_file = None

def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        filetypes=[("All Files", "*.*")]
    )
    if file_path:
        current_file = file_path
        with open(file_path, "r", encoding="utf-8") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    global current_file
    if current_file:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(text.get(1.0, tk.END))
    else:
        save_as_file()

def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        current_file = file_path
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text.get(1.0, tk.END))

# ================= FORMATTING =================

def make_bold():
    try:
        bold_font = tkFont.Font(text, text.cget("font"))
        bold_font.configure(weight="bold")
        text.tag_configure("bold", font=bold_font)
        text.tag_add("bold", "sel.first", "sel.last")
    except:
        pass

def make_italic():
    try:
        italic_font = tkFont.Font(text, text.cget("font"))
        italic_font.configure(slant="italic")
        text.tag_configure("italic", font=italic_font)
        text.tag_add("italic", "sel.first", "sel.last")
    except:
        pass

def change_color():
    try:
        color = colorchooser.askcolor()[1]
        if color:
            text.tag_configure("color", foreground=color)
            text.tag_add("color", "sel.first", "sel.last")
    except:
        pass

def change_size():
    try:
        size = int(size_entry.get())
        new_font = tkFont.Font(family="Consolas", size=size)
        text.configure(font=new_font)
    except:
        pass

# ================= TOOLBAR =================

toolbar = tk.Frame(root, bg="#2b2b2b")
toolbar.pack(fill=tk.X)

tk.Button(toolbar, text="New", command=new_file).pack(side=tk.LEFT, padx=5)
tk.Button(toolbar, text="Open", command=open_file).pack(side=tk.LEFT)
tk.Button(toolbar, text="Save", command=save_file).pack(side=tk.LEFT)

tk.Button(toolbar, text="B", command=make_bold,
          font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=10)

tk.Button(toolbar, text="I", command=make_italic,
          font=("Arial", 12, "italic")).pack(side=tk.LEFT)

tk.Button(toolbar, text="Color", command=change_color).pack(side=tk.LEFT, padx=10)

size_entry = tk.Entry(toolbar, width=5)
size_entry.pack(side=tk.LEFT)
size_entry.insert(0, "14")

tk.Button(toolbar, text="Set Size", command=change_size).pack(side=tk.LEFT, padx=5)

# ================= TEXT AREA =================

frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text = tk.Text(
    frame,
    wrap=tk.WORD,
    font=base_font,
    bg="#1e1e1e",
    fg="white",
    insertbackground="white",
    yscrollcommand=scrollbar.set,
    undo=True
)

text.pack(expand=True, fill=tk.BOTH)
scrollbar.config(command=text.yview)

# ================= SHORTCUTS =================

root.bind("<Control-s>", lambda e: save_file())
root.bind("<Control-o>", lambda e: open_file())
root.bind("<Control-n>", lambda e: new_file())
root.bind("<Control-z>", lambda e: text.edit_undo())
root.bind("<Control-y>", lambda e: text.edit_redo())

# ================= RUN =================

root.mainloop()