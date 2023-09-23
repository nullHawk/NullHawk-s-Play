import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

def main():
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create a QWidget instance (a borderless widget)
    widget = QWidget()
    widget.setWindowFlags(Qt.FramelessWindowHint)
    widget.setAttribute(Qt.WA_TranslucentBackground)
    widget.setWindowTitle("Borderless PyQt5 Widget")  # Set window title
    widget.setGeometry(100, 100, 400, 300)  # Set widget size and position

    # Create a QLabel widget and add it to the main widget
    label = QLabel("Hello, Borderless PyQt5!", widget)
    label.setGeometry(100, 100, 200, 50)  # Set label position and size

    # Show the main widget
    widget.show()

    # Start the main event loop
    sys.exit(app.exec_())