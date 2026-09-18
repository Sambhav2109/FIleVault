import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox


FILE_CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov", ".wmv"},
    "Audio": {".mp3", ".wav", ".aac", ".flac", ".ogg"},
    "Presentations": {".ppt", ".pptx"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Spreadsheets": {".xls", ".xlsx", ".csv"},
}


def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def unique_destination(folder, category, filename):
    category_folder = os.path.join(folder, category)
    os.makedirs(category_folder, exist_ok=True)

    destination = os.path.join(category_folder, filename)
    if not os.path.exists(destination):
        return destination

    name, extension = os.path.splitext(filename)
    counter = 1
    while True:
        candidate = os.path.join(category_folder, f"{name}_{counter}{extension}")
        if not os.path.exists(candidate):
            return candidate
        counter += 1


def organize_files():
    folder = selected_folder.get().strip()

    if not folder:
        messagebox.showwarning("FileVault", "Please select a folder first.")
        return

    moved = 0
    skipped = 0

    try:
        for filename in os.listdir(folder):
            source = os.path.join(folder, filename)

            if not os.path.isfile(source):
                continue

            category = get_category(filename)
            destination = unique_destination(folder, category, filename)
            shutil.move(source, destination)
            moved += 1

        status_label.config(
            text=f"Organized {moved} file(s)"
        )
        messagebox.showinfo(
            "FileVault",
            f"Done! {moved} file(s) organized."
            + (f"\n{skipped} file(s) skipped." if skipped else "")
        )

    except OSError as error:
        status_label.config(text="Could not complete the operation.")
        messagebox.showerror(
            "FileVault Error",
            f"An error occurred while organizing the folder:\n{error}"
        )


def select_folder():
    folder = filedialog.askdirectory(title="Choose a folder to organize")
    if folder:
        selected_folder.set(folder)
        folder_label.config(text=folder)
        status_label.config(text="Folder selected. Ready to organize.")


root = tk.Tk()
root.title("FileVault — File Organizer")
root.geometry("680x420")
root.resizable(False, False)
root.configure(bg="#F5F7FA")

selected_folder = tk.StringVar()

header = tk.Frame(root, bg="#17324D", height=105)
header.pack(fill="x")

tk.Label(
    header,
    text="FileVault",
    font=("Segoe UI", 27, "bold"),
    fg="white",
    bg="#17324D"
).pack(pady=(18, 1))

tk.Label(
    header,
    text="Organize files into smart categories in seconds",
    font=("Segoe UI", 10),
    fg="#D8E4EE",
    bg="#17324D"
).pack()

content = tk.Frame(root, bg="#F5F7FA")
content.pack(fill="both", expand=True, padx=36, pady=25)

tk.Label(
    content,
    text="Selected folder",
    font=("Segoe UI", 11, "bold"),
    fg="#263746",
    bg="#F5F7FA"
).pack(anchor="w")

folder_card = tk.Frame(content, bg="white", highlightbackground="#D6DEE6", highlightthickness=1)
folder_card.pack(fill="x", pady=(8, 18), ipady=8)

folder_label = tk.Label(
    folder_card,
    text="No folder selected",
    font=("Segoe UI", 9),
    fg="#66737F",
    bg="white",
    anchor="w",
    justify="left",
    wraplength=580
)
folder_label.pack(fill="x", padx=13)

button_row = tk.Frame(content, bg="#F5F7FA")
button_row.pack(fill="x")

tk.Button(
    button_row,
    text="Select Folder",
    command=select_folder,
    font=("Segoe UI", 10, "bold"),
    bg="#2F6F9F",
    fg="white",
    activebackground="#285F88",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=18,
    pady=9
).pack(side="left")

tk.Button(
    button_row,
    text="Organize Files",
    command=organize_files,
    font=("Segoe UI", 10, "bold"),
    bg="#17324D",
    fg="white",
    activebackground="#102638",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=18,
    pady=9
).pack(side="left", padx=12)

tk.Label(
    content,
    text="Categories: Images • Documents • Videos • Audio • Presentations • Archives • Spreadsheets • Others",
    font=("Segoe UI", 8.5),
    fg="#687681",
    bg="#F5F7FA"
).pack(anchor="w", pady=(24, 6))

status_label = tk.Label(
    content,
    text="Ready",
    font=("Segoe UI", 9, "bold"),
    fg="#2F6F9F",
    bg="#F5F7FA"
)
status_label.pack(anchor="w")

tk.Label(
    content,
    text="Files are moved only within the folder you choose.",
    font=("Segoe UI", 8),
    fg="#8A949D",
    bg="#F5F7FA"
).pack(anchor="w", pady=(7, 0))

root.mainloop()
