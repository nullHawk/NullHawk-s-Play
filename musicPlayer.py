
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTabWidget, QListWidget, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QPixmap
import ytBack
import requests
import main
import sys




class Ui_mainWindow(object):
    def setupUi(self, mainWindow):

        self.global_music_name = "Music Name"
        self.srchList = []
        self.global_music_id = None
        self.global_album_name = "Album Name"
        self.global_artist_name = "Artist Name"
        self.global_thumbnail = None
        self.defaultThumNail = ":/widget/resources/jbalbum.webp" # Thumnail
        self.url = None

        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(400, 600)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/widget/resources/play_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.searchBox = QtWidgets.QTextEdit(self.horizontalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBox.sizePolicy().hasHeightForWidth())

        self.searchBox.setSizePolicy(sizePolicy)
        self.searchBox.setMaximumSize(QtCore.QSize(500, 30))
        self.searchBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.searchBox.setOverwriteMode(False)
        self.searchBox.setObjectName("searchBox")

        self.horizontalLayout.addWidget(self.searchBox)
        self.searchBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchBtn.sizePolicy().hasHeightForWidth())

        self.searchBtn.setSizePolicy(sizePolicy)
        self.searchBtn.setMaximumSize(QtCore.QSize(16777215, 30))
        self.searchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchBtn.setText("")

        icon = QtGui.QIcon.fromTheme("search")

        self.searchBtn.setIcon(icon)
        self.searchBtn.setFlat(True)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout.addWidget(self.searchBtn)
        self.searchBtn.clicked.connect(self.search)
        

        self.musicTab = QtWidgets.QTabWidget(self.centralwidget)
        self.musicTab.setGeometry(QtCore.QRect(0, 40, 400, 560))
        self.musicTab.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.musicTab.setTabPosition(QtWidgets.QTabWidget.South)
        self.musicTab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.musicTab.setElideMode(QtCore.Qt.ElideNone)
        self.musicTab.setTabsClosable(False)
        self.musicTab.setTabBarAutoHide(False)
        self.musicTab.setObjectName("musicTab")

        self.search = QtWidgets.QWidget()
        self.search.setObjectName("search")
        self.search_List = QtWidgets.QListWidget(self.search)
        self.search_List.setGeometry(QtCore.QRect(-1, 0, 393, 524))
        self.search_List.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_List.setObjectName("search_List")
        self.search_List.itemDoubleClicked.connect(self.startMusic)
        self.musicTab.addTab(self.search, "")

        self.music = QtWidgets.QWidget()
        self.music.setObjectName("music")

        self.album_photo = QtWidgets.QLabel(self.music)
        self.album_photo.setGeometry(QtCore.QRect(75, 50, 250, 250))
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed Bold")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.album_photo.setFont(font)
        self.album_photo.setText("")
        self.album_photo.setPixmap(QtGui.QPixmap(":/widget/resources/jbalbum.webp"))
        
        # self.album_photo.setScaledContents(True)
        self.album_photo.setObjectName("album_photo")
        shadow = QGraphicsDropShadowEffect()
        # setting blur radius
        shadow.setBlurRadius(15)
        color = QColor(0, 0, 0) 
        color.setAlpha(100)
        shadow.setColor(color)
        # adding shadow to the label
        self.album_photo.setGraphicsEffect(shadow)

        self.slider = QtWidgets.QSlider(self.music)
        self.slider.setGeometry(QtCore.QRect(15, 400, 360, 20))
        self.slider.setProperty("value", 30)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")

        self.music_name = QtWidgets.QLabel(self.music)
        self.music_name.setGeometry(QtCore.QRect(10, 320, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed Bold")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)

        self.music_name.setFont(font)
        self.music_name.setAlignment(QtCore.Qt.AlignCenter)
        self.music_name.setObjectName("music_name")

        self.artist_name = QtWidgets.QLabel(self.music)
        self.artist_name.setGeometry(QtCore.QRect(10, 350, 371, 20))
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed")
        font.setPointSize(12)
        self.artist_name.setFont(font)
        self.artist_name.setStyleSheet("color: rgb(162, 162, 162);")
        self.artist_name.setAlignment(QtCore.Qt.AlignCenter)
        self.artist_name.setObjectName("artist_name")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.music)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 430, 331, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.backward = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.backward.setText("")
        icon = QtGui.QIcon.fromTheme("media-skip-backward")
        self.backward.setIcon(icon)
        self.backward.setIconSize(QtCore.QSize(25, 25))
        self.backward.setFlat(True)
        self.backward.setObjectName("backward")
        self.horizontalLayout_2.addWidget(self.backward)

        self.pause = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pause.setText("")
        icon = QtGui.QIcon.fromTheme("media-playback-pause")
        self.pause.setIcon(icon)
        self.pause.setIconSize(QtCore.QSize(25, 25))
        self.pause.setFlat(True)
        self.pause.setObjectName("pause")
        self.horizontalLayout_2.addWidget(self.pause)

        self.forward = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.forward.setText("")
        icon = QtGui.QIcon.fromTheme("media-skip-forward")
        self.forward.setIcon(icon)
        self.forward.setIconSize(QtCore.QSize(25, 25))
        self.forward.setFlat(True)
        self.forward.setObjectName("forward")
        self.horizontalLayout_2.addWidget(self.forward)
        self.musicTab.addTab(self.music, "")
        mainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(mainWindow)
        self.musicTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "NullHawk\'s Play"))
        self.searchBox.setPlaceholderText(_translate("mainWindow", "Search Music"))
        self.musicTab.setTabText(self.musicTab.indexOf(self.search), _translate("mainWindow", "Search"))
        self.music_name.setText(_translate("mainWindow", "Music Name"))
        self.artist_name.setText(_translate("mainWindow", "Artist"))
        self.musicTab.setTabText(self.musicTab.indexOf(self.music), _translate("mainWindow", "Music"))

    def search(self):
        self.musicTab.setCurrentIndex(0)
        self.search_List.clear()
        search_text = self.searchBox.toPlainText()
        search_result = ytBack.search(search_text)
        for i in search_result:
            self.search_List.addItem(i[0])
            self.srchList.append(i)
    
    def startMusic(self):
        selected_items = self.search_List.selectedItems()
        if selected_items:
            global_music_name = selected_items[0].text()
            for i in self.srchList:
                if i[0] == global_music_name:
                    global_music_id = i[1]
                    break
            detail = ytBack.get_song_detail(global_music_id)
            global_artist_name = detail['artist']
            self.global_thumbnail = detail['img_link'][0]["url"]

            self.music_name.setText(global_music_name if (len(global_music_name) < 20) else global_music_name[:20] + "...")
            self.artist_name.setText(global_artist_name)

            # Download the image using requests
            response = requests.get(self.global_thumbnail)
            if response.status_code == 200:
                # Convert the image data to QPixmap and display it
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)

                self.album_photo.setFixedHeight(250)  # Set the desired height
    
                # Calculate the width to maintain the image's aspect ratio
                width = int(pixmap.width() * (self.album_photo.height() / pixmap.height()))

                pixmap = pixmap.scaled(width, self.album_photo.height())

                self.album_photo.setPixmap(pixmap)
                self.album_photo.setAlignment(Qt.AlignCenter)
            else:
                self.album_photo.setPixmap(self.defaultThumNail)

            self.musicTab.setCurrentIndex(1)
    def openWidget(self):
        app = QApplication(sys.argv)

        # Create the main window
        window = QMainWindow()
        ui = widget.UI_widget()
        widget.setupUi(window)

        # Show the main window
        sys.exit(app.exec_())
    def closeEvent(self, event):
        # Override the closeEvent method to intercept the close button click
        self.openWidget()
        event.accept()  # Accept the close event

import nullHawkPlay_rc
