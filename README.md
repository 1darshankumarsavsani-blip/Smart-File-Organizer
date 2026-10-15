# Smart-File-Organizer
A Python-based smart file management system that automatically organizes files, detects duplicate files, and cleans the Downloads folder for better storage management.
## Prerequisites

Before running this project, make sure the following software is installed:

### Python Installation

1. Download Python from:

https://www.python.org/downloads/

2. Run the installer.

3. IMPORTANT:
   Check the following option before installation:

   ✅ Add Python to PATH

4. Click Install Now.

### Verify Installation

Open Command Prompt and run:

```cmd
python --version
```

Expected Output:

```text
Python 3.x.x
```

You can also check:

```cmd
pip --version
```

---

## Project Setup

Download or Clone this repository:

```cmd
git clone https://github.com/YOUR_USERNAME/Smart-File-Organizer.git
```

Navigate to project folder:

```cmd
cd Smart-File-Organizer
```

Project Structure:

```text
Smart_File_Organizer
│
├── main.py
├── organizer.py
├── duplicate_finder.py
├── downloads_cleaner.py
├── README.md
└── requirements.txt
```

Run the project:

```cmd
python main.py
```

---

## Generate EXE File

Install PyInstaller:

```cmd
pip install pyinstaller
```

Move to project folder:

```cmd
cd Smart_File_Organizer
```

Build EXE:

```cmd
python -m PyInstaller --onefile main.py
```

Generated EXE Location:

```text
dist/main.exe
```

Run EXE:

```cmd
cd dist
main.exe
```

Or simply double-click:

```text
dist/main.exe
```

---

## Folder Created Automatically

When using File Organizer, these folders may be created automatically:

```text
Images
Videos
Documents
Audio
Programs
Others
```

When using Downloads Cleaner:

```text
PDF
JPG
PNG
MP4
MP3
DOCX
TXT
EXE
```

Folders are created only when required.

---

## Required Files

Mandatory Files:

✅ main.py

✅ organizer.py

✅ duplicate_finder.py

✅ downloads_cleaner.py

Optional Files:

✅ README.md

✅ requirements.txt

✅ .gitignore

Generated Automatically:

✅ build/

✅ dist/

✅ main.spec

These generated files do not need to be uploaded to GitHub.

---

## Supported File Types

Images:

```text
jpg
jpeg
png
gif
bmp
```

Videos:

```text
mp4
avi
mkv
mov
```

Documents:

```text
pdf
docx
txt
pptx
xlsx
```

Audio:

```text
mp3
wav
aac
```

Programs:

```text
exe
msi
```
