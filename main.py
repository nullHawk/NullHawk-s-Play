import MusicPlayer
import widget
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

def run_widget():
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create the main window
    window = QMainWindow()
    ui = widget.UI_widget()
    ui.setupUi(window)

    # Show the main window
    window.show()

    # Start the main event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    #MusicPlayer.main()
    #widget.widget.main()
    run_widget()





