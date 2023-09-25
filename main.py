import musicPlayer
import widget
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import mutagen
from mutagen.id3 import ID3, APIC




def load_widget():
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create the main window
    window = QMainWindow()
    ui = widget.UI_widget()
    ui.setupUi(window)
    window.show()

    # Show the main window

     
    sys.exit(app.exec_())

def run_player():
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create the main window
    window = QMainWindow()
    ui = musicPlayer.Ui_mainWindow()
    ui.setupUi(window)

    # Show the main window
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    #MusicPlayer.main()
    #widget.widget.main()

    #load_widget()
    run_player()
    





