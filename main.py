import customtkinter
import os
import hashlib
from tkinter import filedialog

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set appearance mode to dark
        self._set_appearance_mode("dark")

        # Window title and size
        self.title("File Sniper")
        self.geometry("550x650")

        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Prevent resizing of the window, because I am lazy.
        self.resizable(0,0)

        # Set application icon
        self.iconbitmap('icon.ico')

        # Initialize path and file list
        self.folder_path = ""
        self.files_and_dirs = []

        # Frame for folder section
        self.folder_frame = customtkinter.CTkFrame(self)
        self.folder_frame.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="nsw")

        # Entry widget to display the folder path
        self.folder_entry = customtkinter.CTkEntry(self.folder_frame, width=350)
        self.folder_entry.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Button to open folder selection dialog
        self.folder_button = customtkinter.CTkButton(self.folder_frame, text="Choose a folder", corner_radius=30, command=self.open_folder)
        self.folder_button.grid(row=0, column=0, padx=(370,0), pady=10)

        # Textbox to display output messages
        self.output_textbox = customtkinter.CTkTextbox(self.folder_frame, width=500, height=250, wrap="none")
        self.output_textbox.grid(row=2, column=0, padx=15, pady=(70, 0), sticky="ns")

        # Button to start the process of finding and removing duplicate files
        self.remove_button = customtkinter.CTkButton(self.folder_frame, text="Remove duplicates", corner_radius=30, command=self.getfiles)
        self.remove_button.grid(row=3, column=0, padx=10, pady=(100, 100), sticky="ew")


    def open_folder(self):
        # Open a dialog to select a folder and set the folder path
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path = folder_path
            self.folder_entry.delete(0, customtkinter.END) # Clears the entry widget
            self.folder_entry.insert(0, folder_path) # Insert the selected folder path


    def getfiles(self):
        # Checks if the directory is empty
        if not os.listdir(self.folder_path):
            self.output_textbox.insert(customtkinter.END, "Output: Sorry, there are no files in found in this directory.\n\n")
        else:
            # Get a list of files in the directory
            self.files_and_dirs = [f for f in os.listdir(self.folder_path) if os.path.isfile(os.path.join(self.folder_path, f))]
            # Call method to find and delete duplicate files
            self.deletecopies()
    

    def get_file_hashes(self, file_path):
        # Compute MD5 hash for a given file
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    

    def deletecopies(self):
        # Dictionary to keep track of seen file hashes
        seen_hashes = {}
        for file in self.files_and_dirs:
            file_path = os.path.join(self.folder_path, file)
            file_hash = self.get_file_hashes(file_path)

            # If a file with the same hash is found, it's a duplicate
            if file_hash in seen_hashes:
                if os.path.exists(file_path):
                    os.remove(file_path) # Remove the duplicate file
                    self.output_textbox.insert(customtkinter.END, f"Output: Deleted duplicate file: {file_path}\n\n")
            else:
                seen_hashes[file_hash] = file_path

# Create and run the application
app = App()
app.mainloop()