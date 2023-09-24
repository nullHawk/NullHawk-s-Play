import MusicPlayer
import widget
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import mutagen
from mutagen.id3 import ID3, APIC





def run_widget():
    # Create a QApplication instance
    app = QApplication(sys.argv)

    # Create the main window
    window = QMainWindow()
    ui = widget.UI_widget()
    ui.setupUi(window)

    # Show the main window
    window.show()

    
    music_name = "Yummy"
    author = "Justin Beiber"
    album = "Changes"

    photo = "resources/music.png"

    #updates the contents of widget
    #ui.update_music_data(music_name, author, album, photo)
     
    sys.exit(app.exec_())

if __name__ == "__main__":
    #MusicPlayer.main()
    #widget.widget.main()

    run_widget()
    





