import os
from tkinter import filedialog as fd
import tkinter as tk
import sys
import ctypes



def get_available_filename(output_directory, base_filename):
    count = 1
    while True:
        filename = f"{base_filename}_{count}.txt"
        filepath = os.path.join(output_directory, filename)
        if not os.path.exists(filepath):
            return filepath
        count += 1

def list_files_and_folders(root_path, output_directory):
    def process_folder(folder_path, depth):
        indent = "-" * depth
        entries = os.listdir(folder_path)
        
        for entry in entries:
            full_path = os.path.join(folder_path, entry)
            if os.path.isdir(full_path):
                with open(output_file, "a") as f:
                    f.write(f"{indent} FOLDER: {entry}\n")
                process_folder(full_path, depth + 1)
            elif os.path.isfile(full_path):
                with open(output_file, "a") as f:
                    f.write(f"{indent} FILE: {entry}\n")
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    output_file = get_available_filename(output_directory, "output")
    
    with open(output_file, "w") as f:
        f.write(f"Root: {root_path}\n")
    
    process_folder(root_path, 0)
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    folder_path = fd.askdirectory()
    if folder_path:
        source_folder = folder_path
    else:
        print("No Folder was selected")
    output_directory = os.path.expanduser(os.path.join("~", "Downloads", "Output"))

    if not os.path.exists(source_folder):
        print("Source folder does not exist.")
        input("Press Enter to exit.")
    else:
        try:
            list_files_and_folders(source_folder, output_directory)
        except PermissionError:
            print("You don't have permission to write to the specified directory.")
            print("Restarting the program with administrator privileges...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        print(f"Output saved to {output_directory}")
        input("Press Enter to exit.")
