import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

def main():
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create a QMainWindow instance (main window)
    window = QMainWindow()
    window.setWindowTitle("Music Player")  # Set window title
    window.setGeometry(100, 100, 400, 300)  # Set window size and position

    # Create a QLabel widget and add it to the main window
    label = QLabel("This is NullHawk's Play!", window)
    label.setGeometry(100, 100, 200, 50)  # Set label position and size

    # Show the main window
    window.show()

    # Start the main event loop
    sys.exit(app.exec_())