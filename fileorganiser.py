import os
import datetime
import shutil

class FileOrganiser:
    def __init__(self, folder):
        # Initialize with folder contents and empty list for file types
        self.folder = list(os.listdir(folder))
        self.file_type_list = []

    def get_file_type(self, files):
        # Check if the given path is a file, then get file extension
        if os.path.isfile(os.path.join("Downloads", files)):
            file_type = os.path.splitext(files)[1]
            return file_type
        else:
            print("File type not file")

    def get_source_path(self, files):
        # Create full path for the source file in Downloads directory
        s = os.path.join("Downloads", files)
        source_path = os.path.abspath(s)
        print("source path", " ", source_path)
        return source_path

    def get_creation_time(self, files):
        # Get file creation time and format it as 'dd Mon, yyyy'
        
        creation_time = datetime.date.fromtimestamp(os.stat(os.path.join("Downloads", files))[9])
        creation_time = creation_time.strftime("%d %b, %Y")
        print(f'The file {files} is created on {creation_time}')
        return creation_time

    def get_folder_name(self, file_type):
        # Append file type to list and prepare folder name by removing the dot
        self.file_type_list.append(file_type)
        print(self.file_type_list)
        folder_name = file_type.upper().replace(".", "")
        print(f'Folder Name is {folder_name}')
        return folder_name

    def start_organiser(self):
        # Loop through all items in the folder
        for files in self.folder:
            if os.path.isfile(os.path.join("Downloads", files)):
                # Get the creation time and source path of the file
                creation_time = self.get_creation_time(files)
                source_path = self.get_source_path(files)
                
                # Determine file type (extension)
                file_type = self.get_file_type(files)
                print("File Type is", " ", file_type)

                # Check if file type is unique and non-empty, then create a folder name
                if file_type not in self.file_type_list and file_type != "":
                    folder_name = self.get_folder_name(file_type)
                    print("folder_name", " ", folder_name)

                # Handling cases where file type is None or empty
                if file_type == None:
                    print("No file Type Found")
                elif file_type != "None":
                    # Create the main folder path for the file type
                    folder_name = file_type.upper().replace(".", "")
                    folder_path = os.path.join("Downloads", folder_name)
                    
                    # Re-define folder_path and create a date-based subfolder
                    folder_path = os.path.join("Downloads", file_type.upper().replace(".", ""))
                    date_file_path = os.path.join(folder_path, creation_time)

                    # Create the main folder if it doesn't exist
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                        print("path created")
                        print(folder_path)

                    # Create the date-based folder if it doesn't exist
                    if not os.path.exists(date_file_path):
                        os.makedirs(date_file_path)
                        print("path created")
                        print(f'this is the date file path {date_file_path}')

                    # Display the folder name for debugging
                    print("folder name", " ", folder_name)

                    # Define the final destination path within the date-based folder
                    destination_path = os.path.join("Downloads", folder_name, creation_time)
                    print("Destination_path", " ", destination_path)

                    # Move the file to the destination path
                    self.move_path(source_path, destination_path)

    def move_path(self, source, destination):
        # Attempt to move file from source to destination, with exception handling
        try:
            shutil.move(source, destination)
        except Exception as e:
            print(e)
