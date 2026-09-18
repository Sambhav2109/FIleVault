# FileVault

FileVault is a lightweight Python desktop application that automatically organizes files in a selected folder into categorized subfolders.

## Features

- Simple desktop GUI built with Tkinter
- Select any folder using a file dialog
- Automatically categorizes files by extension
- Supports Images, Documents, Videos, Audio, Presentations, Archives, Spreadsheets, and Others
- Prevents accidental overwriting when duplicate filenames exist
- Displays the selected folder and operation status
- Only moves files inside the folder selected by the user

## Tech Stack

- Python
- Tkinter
- os
- shutil

## How to Run

1. Install Python 3.
2. Clone the repository:
   ```bash
   git clone https://github.com/Sambhav2109/FIleVault.git
   cd FIleVault
   ```
3. Run the application:
   ```bash
   python filevault.py
   ```

## Project Structure

```
FIleVault/
├── filevault.py
└── README.md
```

## Example

A folder containing mixed files can be organized into:

```text
Images/
Documents/
Videos/
Audio/
Presentations/
Archives/
Spreadsheets/
Others/
```

## Future Improvements

- Drag-and-drop folder selection
- Custom category rules
- Undo support
- Organization history
- Packaging as a standalone executable

## Author

**Sambhav Pathak**

GitHub: https://github.com/Sambhav2109
