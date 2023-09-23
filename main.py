import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

def main():
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create a QMainWindow instance (main window)
    window = QMainWindow()
    window.setWindowTitle("My PyQt5 App")  # Set window title
    window.setGeometry(100, 100, 400, 300)  # Set window size and position

    # Create a QLabel widget and add it to the main window
    label = QLabel("Hello, PyQt5!", window)
    label.setGeometry(100, 100, 200, 50)  # Set label position and size

    # Show the main window
    window.show()

    # Start the main event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
Make sure you have PyQt5 installed on your system. You can install it using pip:

Copy code
pip install PyQt5
In this example, we create a simple PyQt5 application with a main window containing a QLabel. The app.exec_() function starts the event loop, allowing the application to respond to user interactions.

Save this code in a .py file and run it to start your PyQt5 app.





