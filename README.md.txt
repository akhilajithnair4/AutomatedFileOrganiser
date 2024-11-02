File Organiser
This Python script organizes files in a specified folder (in this case, the "Downloads" directory) by their file type and creation date. It automatically creates folders based on the file type and subfolders based on the file creation date, then moves each file to its respective folder.

How It Works
The FileOrganiser class in this script:

Retrieves Files: Lists all files in the specified folder.
Determines File Type: Identifies the file extension (e.g., .pdf, .jpg).
Checks Creation Date: Retrieves the file’s creation date and formats it as dd Mon, yyyy.
Creates Folders:
Main folders are created based on the file type (e.g., PDF for .pdf files).
Subfolders are created based on the file's creation date (e.g., 02 Nov, 2024).
Moves Files: Each file is moved to the appropriate date-based subfolder within its file type folder.
Folder Structure Example
If a file named example.pdf was created on 02 Nov, 2024, the script organizes it in the following structure within Downloads:

markdown
Copy code
Downloads/
│
└── PDF/
    └── 02 Nov, 2024/
        └── example.pdf
How to Use
Ensure Your Folder Path: By default, this script is set up to organize files in the Downloads directory. You can change this by modifying the path in the script.

Run the Script:

Ensure Python is installed on your system.
Place the script in the directory of your choice.
Run the script from the command line:
bash
Copy code
python your_script_name.py
Check Results: After running, files in the specified folder will be organized into subfolders based on their type and creation date.

Code Breakdown
Class Initialization
python
Copy code
def __init__(self, folder):
    self.folder = list(os.listdir(folder))
    self.file_type_list = []
Initializes the FileOrganiser class by listing files in the specified folder and setting up an empty list to track file types.

Methods
get_file_type: Determines the file extension.
get_source_path: Gets the full path of each file.
get_creation_time: Retrieves and formats the creation date of each file.
get_folder_name: Creates a folder name based on file type.
start_organiser: Main function that loops through files, organizes them, and calls move_path.
move_path: Moves the file to the specified destination.
Example Output
Running the script outputs messages to the console showing the source path, file type, folder names, destination paths, and any paths created.

Error Handling
The move_path function is wrapped in a try-except block to handle any issues during file movement, such as permission errors or missing files.

Notes
Customization: You can modify the path in the script if you want to organize files in a folder other than Downloads.
File Types: This script skips items that are not files (like folders) and only organizes files with extensions.