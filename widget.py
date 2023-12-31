from PyQt5 import QtCore, QtGui, QtWidgets;
from PyQt5.QtCore import Qt;
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor
import sys


class UI_widget(object):

    

    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.setWindowModality(QtCore.Qt.ApplicationModal)
        widget.resize(400, 250)
        widget.setWindowFlag(Qt.FramelessWindowHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)
        widget.setWindowFlags(widget.windowFlags() | Qt.WindowStaysOnTopHint)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget.sizePolicy().hasHeightForWidth())

        

        widget.setSizePolicy(sizePolicy)
        widget.setMinimumSize(QtCore.QSize(400, 250))
        widget.setMaximumSize(QtCore.QSize(400, 250))
        widget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        widget.setWindowOpacity(1.0)
        widget.setAutoFillBackground(False)
        widget.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

        widget.resize(400, 250)
        desktop = QtWidgets.QApplication.desktop()
        screen_rect = desktop.availableGeometry(desktop.primaryScreen())
        # Calculate the position for the top-right corner
        top_right_x = screen_rect.width() - widget.width()
        top_right_y = 0
        widget.move(top_right_x, top_right_y)

        self.frame = QtWidgets.QFrame(widget)
        self.frame.setGeometry(QtCore.QRect(50, 50, 300, 150))

        font = QtGui.QFont()
        font.setFamily("Inconsolata Condensed Bold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)

        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")

        self.prev_button = QtWidgets.QPushButton(self.frame)
        self.prev_button.setGeometry(QtCore.QRect(110, 100, 30, 30))
        self.prev_button.setText("")

        icon = QtGui.QIcon.fromTheme("media-skip-backward")

        self.prev_button.setIcon(icon)
        self.prev_button.setFlat(True)
        self.prev_button.setObjectName("prev_button")
        self.play_button = QtWidgets.QPushButton(self.frame)
        self.play_button.setGeometry(QtCore.QRect(160, 100, 30, 30))
        self.play_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.play_button.setText("")

        icon = QtGui.QIcon.fromTheme("media-playback-pause")

        self.play_button.setIcon(icon)
        self.play_button.setFlat(True)
        self.play_button.setObjectName("play_button")
        self.next_button = QtWidgets.QPushButton(self.frame)
        self.next_button.setGeometry(QtCore.QRect(210, 100, 30, 30))
        self.next_button.setText("")

        icon = QtGui.QIcon.fromTheme("media-skip-forward")

        self.next_button.setIcon(icon)
        self.next_button.setFlat(True)
        self.next_button.setObjectName("next_button")
        
        self.close_button = QtWidgets.QPushButton(self.frame)
        self.close_button.setGeometry(QtCore.QRect(270, 0, 30, 30))
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.close_button.setFont(font)
        self.close_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.close_button.setStyleSheet("color: rgb(90, 82, 82);")
        self.close_button.setText("")
        
        icon = QtGui.QIcon.fromTheme("window-close")
        
        self.close_button.setIcon(icon)
        self.close_button.setFlat(True)
        self.close_button.setObjectName("close_button")
        self.close_button.clicked.connect(widget.close)
        
        self.music_name = QtWidgets.QLabel(self.frame)
        self.music_name.setGeometry(QtCore.QRect(90, 50, 171, 21))
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.music_name.sizePolicy().hasHeightForWidth())
        
        self.music_name.setSizePolicy(sizePolicy)
        
        font = QtGui.QFont()
        font.setFamily("Inconsolata Condensed Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        
        self.music_name.setFont(font)
        self.music_name.setTextFormat(QtCore.Qt.AutoText)
        self.music_name.setScaledContents(False)
        self.music_name.setWordWrap(False)
        self.music_name.setObjectName("music_name")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 30, 161, 23))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.author_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.author_name.setEnabled(True)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.author_name.sizePolicy().hasHeightForWidth())
        
        self.author_name.setSizePolicy(sizePolicy)
        self.author_name.setMinimumSize(QtCore.QSize(30, 0))
        self.author_name.setMaximumSize(QtCore.QSize(70, 16777215))
        
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.author_name.setFont(font)
        self.author_name.setStyleSheet("color: rgb(82, 74, 74);")
        self.author_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.author_name.setTextFormat(QtCore.Qt.AutoText)
        self.author_name.setScaledContents(True)
        self.author_name.setWordWrap(False)
        self.author_name.setObjectName("author_name")
        
        self.horizontalLayout.addWidget(self.author_name)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setStyleSheet("background-color: rgb(150, 150, 150);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.horizontalLayout.addWidget(self.line)
        self.album_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.album_name.setEnabled(True)
        self.album_name.setMaximumSize(QtCore.QSize(70, 16777215))
        
        font = QtGui.QFont()
        font.setFamily("Inconsolata Semi Condensed Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.album_name.setFont(font)
        self.album_name.setStyleSheet("color: rgb(82, 74, 74);")
        self.album_name.setObjectName("album_name")
        
        self.horizontalLayout.addWidget(self.album_name)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.maximize = QtWidgets.QPushButton(self.frame)
        self.maximize.setGeometry(QtCore.QRect(240, 0, 30, 30))
        
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        
        self.maximize.setFont(font)
        self.maximize.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.maximize.setStyleSheet("background-color: rgb(90, 82, 82);")
        self.maximize.setText("")
        
        icon = QtGui.QIcon.fromTheme("window-maximize")
        
        self.maximize.setIcon(icon)
        self.maximize.setFlat(True)
        self.maximize.setObjectName("close_button_2")
        self.maximize.clicked.connect(self.open_max)
        
        self.horizontalSlider = QtWidgets.QSlider(self.frame)
        self.horizontalSlider.setGeometry(QtCore.QRect(90, 80, 161, 20))
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(40)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setCursor(Qt.PointingHandCursor)
        self.horizontalSlider.setObjectName("horizontalSlider")
        
        self.album_photo = QtWidgets.QLabel(widget)
        self.album_photo.setGeometry(QtCore.QRect(25, 75, 100, 100))
        self.album_photo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.album_photo.setText("")
        self.album_photo.setPixmap(QtGui.QPixmap(":/widget/resources/jbalbum.webp"))
        self.album_photo.setScaledContents(True)
        self.album_photo.setObjectName("album_photo")
        
        shadow = QGraphicsDropShadowEffect()
        # setting blur radius
        shadow.setBlurRadius(15)
        color = QColor(0, 0, 0) 
        color.setAlpha(100)
        shadow.setColor(color)
        # adding shadow to the label
        self.album_photo.setGraphicsEffect(shadow)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "NullHawk\'s Play"))
        self.music_name.setText(_translate("widget", "Music Name"))
        self.author_name.setText(_translate("widget", "Author"))
        self.album_name.setText(_translate("widget", "Album"))

    def open_max(self):
        #TODO : open the main Music Player
        print("open")

    def close_application(self):
        widget.close()
    
    def update_music_data(self, music_name, author, album, photo_add):
        if len(music_name) > 12:
            music_name = music_name[:12].strip() + "..."
        if len(author) > 6:
            author = author[:6].strip() +  "..."
        if len(album) > 7:
            album = album[:7].strip() + "..."
        self.music_name.setText(music_name)
        self.author_name.setText(author)
        self.album_name.setText(album)
        self.album_photo.setPixmap(QtGui.QPixmap(photo_add))
    

import nullHawkPlay_rc
