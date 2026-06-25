import customtkinter as ctk
import json 
import os
import shutil
from tkinter import filedialog
from pathlib import Path

usern = os.path.expanduser('~')
path = r"OneDrive\Desktop\Files"
codes = r"OneDrive\Desktop\Files\Codes"
exorbinary = r"OneDrive\Desktop\Files\Exe/Binary"
imgs = r"OneDrive\Desktop\Files\Images"
videos = r"OneDrive\Desktop\Files\Videos"
sci = r"OneDrive\Desktop\Files\Scientific files"
discimg = r"OneDrive\Desktop\Files\Disc images"
docs = r"OneDrive\Desktop\Files\Documents"
codes = os.path.join(usern, codes)
exorbinary = os.path.join(usern, exorbinary)
imgs = os.path.join(usern, imgs)
videos = os.path.join(usern, videos)
sci = os.path.join(usern, sci)
discimg = os.path.join(usern, discimg)
docs = os.path.join(usern, docs)
elses = os.path.join(usern, r"OneDrive\Desktop\Files\Other")

codeextention = [
    ".py", ".cpp", ".c", ".h", ".hpp", ".java", ".js", ".ts", ".rs", ".go", ".rb", ".php",
    ".html", ".css", ".scss", ".less", ".jsx", ".vue", ".sh", ".bash", ".zsh", ".ps1",
    ".md", ".rst", ".tex", ".json", ".yaml", ".yml", ".xml", ".toml", ".ini", ".conf", ".env",
    ".gitignore", ".dockerignore", ".eslintrc", ".babelrc", ".Dockerfile"
]

sysorbinary = [
    ".exe", ".bin", ".elf", ".app", ".msi", ".deb", ".rpm"
]

imgextention = [
    ".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".bmp", ".tiff", ".ico",
    ".psd", ".ai", ".blend"
]

mediavid = [
    ".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv", ".wmv",
]

dataorsci = [
    ".csv", ".tsv", ".xlsx", ".xls", ".parquet", ".avro", ".hdf5", ".npy", ".pkl",
    ".sql", ".sqlite", ".db", ".jsonl"
]

discimg = [
    ".zip", ".tar", ".gz", ".7z", ".rar", ".iso", ".dmg", ".img",
]

docx = [
    ".pdf", ".doc", ".docx", ".txt", ".rtf",
]

# 1. Flatten the lists into one master list automatically
# This is much better than counting to 124 manually!
all_extensions = codeextention + sysorbinary + imgextention + mediavid + dataorsci + discimg + docx

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

with open('app_data.json', 'r') as f:
    data = json.load(f)

bcg_color = data['backgroundc']
print(bcg_color)

typee = data['type']
print(typee)

class ozz:
    def __init__(self, root):
        self.root = root
        self.root.title('ORGA | File Manager - v1.0')
        self.root.geometry('500x200')
        self.root.iconbitmap("Minecraft_Folder_23366.ico")

        self.choosefile()
    
    def choosefile(self):
        self.framee = ctk.CTkFrame(self.root,
                                   fg_color=bcg_color,
                                   width = 500,
                                   height=200)
        self.framee.pack(fill='both', expand=True)
        self.titol1=ctk.CTkLabel(self.framee,
                                 text="ORGA File manager - v1.0",
                                 text_color="#00FF41",
                                 font=('Helvetica', 24, 'bold'))
        self.titol1.pack(pady=20,padx=20)

        choozfile = ctk.CTkButton(self.framee,
                                  text="Choose file!",
                                  text_color="#00FF41",
                                  fg_color=bcg_color,
                                  command=self.choosefileplz)
        choozfile.pack(pady=10 , padx= 20)
        sendfile = ctk.CTkButton(self.framee,
                                 text='Send',
                                 fg_color=bcg_color,
                                 text_color="#00FF41",
                                 command=self.send)
        sendfile.pack(pady=10, padx=20)
        
    def send(self):
        pathobj = Path(self.file)
        extention = pathobj.suffix

        if not extention:
            self.root.destroy()

        if extention not in all_extensions:
            shutil.move(self.file, elses)
            self.root.destroy()

        if extention in codeextention:
            shutil.move(self.file, codes)

        elif extention in sysorbinary:
            shutil.move(self.file, exorbinary)

        elif extention in imgextention:
            shutil.move(self.file, imgs)

        elif extention in mediavid:
            shutil.move(self.file, videos)

        elif extention in discimg:
            shutil.move(self.file, discimg)

        elif extention in docx:
            shutil.move(self.file, docs)

    def choosefileplz(self):
        self.file = filedialog.askopenfilename()
        print(self.file)
        

def main():
    app = ctk.CTk()
    root = ozz(app)
    app.mainloop()

if __name__ == "__main__":
    main()