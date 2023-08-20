# Directory Scanner 

This Python script allows you to list the files and folders in a given directory, including subdirectories, and save the directory structure to a text file and an XML file (Experimental). A standalone executable file for Windows is also available for convenience.

## Features

- Recursively lists files and folders in a specified directory.
- Outputs the listing to both a text file and an XML file.
- Handles cases where the user doesn't have sufficient permissions to write to the specified output directory.
- Experimental feature: Restart the program with administrator privileges if permission error occurs.

## Usage

1. Clone or download this repository to your local machine.
2. Make sure you have Python installed.
3. Run the script in a terminal or command prompt.

### Standalone Executable (Windows)

If you're using Windows, you can also use the standalone executable file provided in the repository. Follow these steps:

1. Go to the (https://github.com/BLINDPEOPLEDONTSEECSHARP/FolderScanner/blob/main/FolderScanner.exe) section of the repository.
2. Download the `.exe` file from the latest release.
3. Double-click the `.exe` file to run the script.

### Requirements Python

- Python 3.x
- tkinter (for the GUI folder selection)
- xml.etree.ElementTree (for XML creation)

### Instructions

1. Run the script.
2. A GUI dialog will appear for you to select the root directory.
3. The script will then list the files and folders in the selected directory.
4. The results will be saved in both a text file and an XML file.

### Experimental Feature: Administrator Permissions

In some cases, you might encounter a permission error when trying to save the output in a specific directory. The script includes an experimental feature that attempts to restart the program with administrator privileges if a permission error occurs. This can be especially useful on Windows systems.

### Output Format

The script generates a hierarchical representation of the directory structure in the following format:

FOLDER: Root Directory
FOLDER: Subfolder
- FILE: File1.txt
- FILE: File2.txt
FILE: FileA.txt
FILE: FileB.txt


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
