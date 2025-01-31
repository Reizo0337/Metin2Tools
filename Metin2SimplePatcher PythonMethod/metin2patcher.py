import sys
import os
import hashlib
import subprocess
import urllib.request
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QGraphicsDropShadowEffect, QFrame
from PyQt5.QtCore import Qt, QPoint, QSize, QThread, pyqtSignal
from PyQt5.QtGui import QPixmap, QIcon, QColor

# Constants
TESTING = 1
SERVER_NAME = 'sapphire2'
SERVER_URL = "http://localhost/patcher/"
GAME_EXECUTABLE = "Metin2Release.exe"
FILE_LIST_URL = SERVER_URL + "file_list.txt"
if TESTING:
    CLIENT_FOLDER = "./patcher_test/"
    import time

if getattr(sys, 'frozen', False):
    app_path = sys._MEIPASS
else:
    app_path = os.path.dirname(__file__)

PATCHER_BG = os.path.join(app_path, "img", "patcher_bg.png")

class DownloadWorker(QThread):
    progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal(str)

    def __init__(self, file_list, parent=None):
        super().__init__(parent)
        self.file_list = file_list

    def run(self):
        for file_name, server_hash in self.file_list:
            success = self.download_file(file_name)
            if not success:
                self.finished_signal.emit(f"Failed to download {file_name}")
                return
            self.progress_signal.emit(int((self.file_list.index((file_name, server_hash)) + 1) / len(self.file_list) * 100))

        self.finished_signal.emit("Game updated successfully.")

    def download_file(self, file_name):
        if TESTING:
            time.sleep(1)

        try:
            full_url = SERVER_URL + "uploads/" + file_name
            response = urllib.request.urlopen(full_url)

            if response.status == 200:
                file_path = os.path.join(CLIENT_FOLDER, file_name)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)

                with open(file_path, "wb") as file:
                    file.write(response.read())
                return True
            else:
                return False
        except Exception as e:
            return False


class GameLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.is_dragging = False
        self.drag_positions = QPoint()

    def initUI(self):
        self.setWindowTitle("Sapphire2")
        self.setGeometry(100, 100, 1280, 720)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Background setup
        self.background_widget = QWidget(self)
        self.background_widget.setGeometry(0, 0, self.width(), self.height())
        self.update_background()

        # Close Button
        self.close_button = QPushButton(self)
        self.close_button.setIcon(QIcon(os.path.join(app_path, "img", "close.png")))
        self.close_button.setIconSize(QSize(30, 30))
        self.close_button.setStyleSheet("background-color: transparent; border: none;")
        self.dropShadow(self.close_button, 10, 0, 0, 0, 180, 2, 0.5)

        close_layout = QHBoxLayout()
        close_layout.addWidget(self.close_button)
        close_layout.setAlignment(self.close_button, Qt.AlignTop | Qt.AlignRight)
        self.close_button.clicked.connect(self.close)

        # Launch Button
        self.btn_launch = QPushButton(self)
        self.btn_launch.setIcon(QIcon(os.path.join(app_path, "img", "play_btn.png")))
        self.btn_launch.setIconSize(QSize(200, 62))
        self.btn_launch.setStyleSheet("background-color: transparent; border: none; margin-bottom: 5px;")
        self.dropShadow(self.btn_launch, 10, 121, 80, 242, 100, 3, 1)

        self.launch_layout = QHBoxLayout()
        self.launch_layout.addWidget(self.btn_launch)
        self.launch_layout.setAlignment(self.btn_launch, Qt.AlignBottom | Qt.AlignLeft)
        self.btn_launch.clicked.connect(self.launch_game)

        self.label = QLabel("Metin2Sapphire", self)

        # Layout
        layout = QVBoxLayout(self.background_widget)
        layout.addLayout(close_layout)
        layout.addWidget(self.label)
        layout.addLayout(self.launch_layout)
        self.setLayout(layout)

        self.update_game()

    def update_background(self):
        pixmap = QPixmap(PATCHER_BG)
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        background_label = QLabel(self.background_widget)
        background_label.setPixmap(scaled_pixmap)
        background_label.setGeometry(0, 0, self.width(), self.height())

    def update_game(self):
        self.btn_launch.hide()
        updates_needed = self.checkforUpdate()

        if updates_needed:
            self.label.setText("Updating game...")
            self.download_thread = DownloadWorker(updates_needed)
            self.download_thread.progress_signal.connect(self.update_progress)
            self.download_thread.finished_signal.connect(self.on_download_finished)
            self.download_thread.start()
        else:
            self.label.setText("No updates needed.")
            self.btn_launch.show()

    def update_progress(self, progress):
        self.label.setText(f"Downloading... {progress}%")

    def on_download_finished(self, message):
        self.label.setText(message)
        self.btn_launch.show()

    def checkforUpdate(self):
        file_list = self.get_file_list()
        updates_needed = []

        for file_name, server_hash in file_list:
            local_file_path = os.path.join(CLIENT_FOLDER, file_name)

            # If file doesn't exist or hashes don't match, add to the list of updates
            if not os.path.exists(local_file_path) or self.get_file_hash(local_file_path) != server_hash:
                updates_needed.append((file_name, server_hash))

        return updates_needed

    def get_file_hash(self, file_path):
        if not os.path.exists(file_path):
            return None
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def get_file_list(self):
        try:
            with urllib.request.urlopen(FILE_LIST_URL) as response:
                if response.status == 200:
                    file_list = [line.decode('utf-8').strip().split(",") for line in response.readlines()]
                    return file_list
                else:
                    self.label.setText("Failed to get file list...")
                    return []
        except Exception as e:
            self.label.setText(f"Error fetching file list: {str(e)}")
            return []

    def launch_game(self):
        if os.path.exists(GAME_EXECUTABLE):
            self.label.setText("Starting Metin2 Sapphire")
            subprocess.Popen(GAME_EXECUTABLE)
            sys.exit()
        else:
            self.label.setText("Error: Can't find game executable.")

    def dropShadow(self, widget, blur, r, g, b, t, offx, offy):
        glow_effect = QGraphicsDropShadowEffect()
        glow_effect.setBlurRadius(blur)
        glow_effect.setColor(QColor(r, g, b, t))
        glow_effect.setOffset(offx, offy)
        widget.setGraphicsEffect(glow_effect)

    ## MouseDetecting for drag and drop
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.is_dragging:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_dragging = False
    ## MouseDetecting for drag and drop

if __name__ == '__main__':
    app = QApplication(sys.argv)
    launcher = GameLauncher()
    launcher.show()
    sys.exit(app.exec_())
