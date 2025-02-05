import os
import hashlib
import subprocess
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel

SERVER_URL = "http://localhost/patcher/"
CLIENT_FOLDER = "Z:/SAPPHIRE2 - Rebellion of Kingdoms/Client/"
SECRET_TOKEN = "REIZONR1"

class FileUploader(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("File Uploader")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Select files to upload to the server", self)
        self.btn_select_files = QPushButton("Select Files", self)
        self.btn_upload_files = QPushButton("Upload Files", self)
        self.btn_generate_patch = QPushButton("Generate Delta Patch", self)  # New button

        self.btn_select_files.clicked.connect(self.select_files)
        self.btn_upload_files.clicked.connect(self.upload_files)
        self.btn_generate_patch.clicked.connect(self.generate_patch)  # New button action

        self.selected_files = []

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.btn_select_files)
        layout.addWidget(self.btn_upload_files)
        layout.addWidget(self.btn_generate_patch)  # Add the new button to layout
        self.setLayout(layout)

    def select_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Files", CLIENT_FOLDER, "All Files (*)")
        if files:
            self.selected_files = files
            self.label.setText(f"Selected {len(files)} files")

    def generate_md5(self, file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get_relative_path(self, file_path):
        normalized_path = os.path.normpath(file_path)
        relative_path = os.path.relpath(normalized_path, CLIENT_FOLDER)
        return relative_path

    def create_file_list(self, current_file_list):
        new_file_list = current_file_list.copy()

        for file_path in self.selected_files:
            relative_path = self.get_relative_path(file_path)
            md5_hash = self.generate_md5(file_path)

            if not any(relative_path == existing_file.split(",")[0] for existing_file in current_file_list):
                new_file_list.append(f"{relative_path},{md5_hash}")

        return "\n".join(new_file_list)

    def upload_files(self):
        if not self.selected_files:
            self.label.setText("No files selected for upload.")
            print("No files selected.")
            return

        current_file_list = self.get_current_file_list()

        file_list_content = self.create_file_list(current_file_list)

        self.upload_file_list(file_list_content)

        for file_path in self.selected_files:
            relative_path = self.get_relative_path(file_path)
            folder_name = self.get_folder_name(relative_path)
            self.upload_single_file(file_path, folder_name)

        self.label.setText("Files uploaded successfully")
        self.selected_files = []
        self.btn_select_files.setText("Select Files")
        self.btn_upload_files.setText("Upload Files")

    def get_current_file_list(self):
        try:
            headers = {
                "Authorization": f"Bearer {SECRET_TOKEN}"
            }

            response = requests.get(SERVER_URL + "file_list.txt", headers=headers)
            if response.status_code == 200:
                return response.text.splitlines()
            else:
                self.label.setText(f"Failed to fetch current file list. Status code: {response.status_code}")
                print(f"Failed to fetch current file list. Status code: {response.status_code}")
                return []
        except requests.exceptions.RequestException as e:
            self.label.setText(f"Error fetching current file list: {str(e)}")
            print(f"Error fetching current file list: {str(e)}")
            return []

    def upload_file_list(self, file_list_content):
        try:
            headers = {
                "Authorization": f"Bearer {SECRET_TOKEN}"
            }

            response = requests.post(
                SERVER_URL + "upload_file_list.php",
                data={'file_list': file_list_content},
                headers=headers
            )

            if response.status_code == 200:
                print(f"File list uploaded successfully: {response.json()}")
            else:
                print(f"Failed to upload file list. Status code: {response.status_code} Response: {response.json()}")
        except requests.exceptions.RequestException as e:
            print(f"Error uploading file list: {str(e)}")

    def upload_single_file(self, file_path, folder_name):
        try:
            if not os.path.exists(file_path):
                print(f"File not found: {os.path.basename(file_path)}")
                return

            relative_path = self.get_relative_path(file_path)
            print(f"Uploading file: {relative_path}")

            if folder_name != ".":
                folder_name = folder_name.strip('/')
            file_name = os.path.basename(file_path)

            with open(file_path, 'rb') as file:
                files = {'file': (file_name, file)}

                headers = {
                    "Authorization": f"Bearer {SECRET_TOKEN}"
                }

                response = requests.post(
                    SERVER_URL + f"upload_file.php?folder={folder_name}",
                    files=files,
                    headers=headers
                )

                print(f"Server response (raw): {response.text}")

                if response.status_code == 200:
                    try:
                        print(f"File uploaded successfully: {response.json()}")
                    except ValueError as e:
                        print(f"Error decoding JSON: {e}")
                        print(f"Response content: {response.text}")
                else:
                    print(f"Failed to upload file: {relative_path}. Status code: {response.status_code} Response: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Error uploading {os.path.basename(file_path)}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error uploading {os.path.basename(file_path)}: {str(e)}")

    def get_folder_name(self, relative_path):
        if os.path.basename(relative_path) == relative_path:
            return '.'
        folder_name = os.path.dirname(relative_path)
        return folder_name

    def generate_patch(self):
        if len(self.selected_files) != 2:
            self.label.setText("Please select exactly two files (original and updated).")
            return

        original_file = self.selected_files[0]
        updated_file = self.selected_files[1]

        try:
            # Generate patch file name
            patch_file = os.path.join(CLIENT_FOLDER, "patch.xdelta")

            # Call xdelta3 to generate the patch
            self.label.setText(f"Generating delta patch for {original_file} -> {updated_file}...")
            self.create_xdelta_patch(original_file, updated_file, patch_file)

            self.label.setText(f"Delta patch created successfully: {patch_file}")

        except Exception as e:
            self.label.setText(f"Error generating patch: {str(e)}")
            print(f"Error generating patch: {str(e)}")

    def create_xdelta_patch(self, original_file, updated_file, patch_file):
        command = [
            "xdelta3",  # Assuming xdelta3 is installed and available in PATH
            "-e",       # Encoding (create a patch)
            "-s", original_file,  # Source file (original)
            updated_file,  # Target file (updated)
            patch_file  # Output patch file
        ]
        subprocess.run(command, check=True)


if __name__ == '__main__':
    app = QApplication([])
    uploader = FileUploader()
    uploader.show()
    app.exec_()
