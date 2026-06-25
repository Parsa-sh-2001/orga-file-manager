import customtkinter as ctk
import json

with open('app_data.json', 'r') as f:
    dataread = json.load(f)

bgc = dataread['backgroundc']
textc = dataread['textc']

class ooo:
    def __init__(self, root):
        self.app = root
        self.app = ctk.CTk()
        self.app.title("CONFIG OF FILEMOVER")
        self.app.geometry('300x400')
        self.app.iconbitmap('Minecraft_Folder_23366.ico')
        self.frame = ctk.CTkFrame(self.app,
                            fg_color=bgc,
                            width=300,
                            height=400)
        self.frame.pack(fill='both', expand=True)

        self.welcome = ctk.CTkLabel(self.frame,
                            text="CONFIG",
                            text_color=textc,
                            font=("Segoe UI", 24, 'bold'))
        self.welcome.pack(pady=20,padx=20)

        self.choose_copyormove = ctk.CTkButton(self.frame,
                                        text="Copy / Move files",
                                        font=("Segoe UI", 15, 'bold'),
                                        fg_color=bgc)
        self.choose_copyormove.pack(pady=20,padx=20)

def main():
    root = ctk.CTk()
    app = ooo(root)
    root.mainloop()

if __name__ == "__main__":
    main()