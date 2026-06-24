import sys
import platform
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt6.QtWidgets import *

# GUI FILE
from app_modules import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('NetfloxPyDesk')
        UIFunctions.labelTitle(self, 'NetfloxPyDesk')
        UIFunctions.labelDescription(self, 'Mi Programa')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1024, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/20x20/icons/20x20/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "Add User", "btn_new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
        UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        UIFunctions.addNewMenu(self, "Movies", "btn_movies", "url(:/16x16/icons/16x16/cil-movie.png)", False)
        
        # --- LÍNEA NUEVA: CREA UNA PÁGINA COMPLETAMENTE EN BLANCO ---
        self.ui.page_movies = QWidget()
        self.ui.stackedWidget.addWidget(self.ui.page_movies)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        UIFunctions.userIcon(self, "SC", "", True)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.MouseButton.LeftButton:
                self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
                self.dragPos = event.globalPosition().toPoint()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        ## ==> END ##

        # --- LÍNEAS NUEVAS CORREGIDAS PARA LIMPIAR LA PÁGINA DE MOVIES ---
        self.ui.tableWidget.hide()    # Oculta la tabla vacía del fondo (Este sí existe)  
        self.ui.frame_3.hide()        # Oculta la caja de instalación de Blender
        self.ui.tableWidget.hide()    # Oculta la tabla vacía del fondo



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE NEW USER
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "New User")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "Custom Widgets")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE MOVIES
        # PAGE MOVIES
        if btnWidget.objectName() == "btn_movies":
        
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_movies) 
            
            UIFunctions.resetStyle(self, "btn_movies")
            UIFunctions.labelPage(self, "Movies")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()
        if event.buttons() == Qt.MouseButton.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.MouseButton.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MouseButton.MiddleButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')

    # Obtiene la altura de la pantalla y calcula un tamaño de fuente dinámico
    # IMPORTANTE: Se debe tener en cuenta que el tamaño de fuente puede variar
    # dependiendo de la resolución de la pantalla 0.016 es para resolusion != 4k, para 4k usar 0.008

    font_size = int(app.primaryScreen().size().height() * 0.015) 

    # Usa f-string para definir el stylesheet correctamente
    style_sheet = f"QWidget {{ font-size: {font_size}px; }}"
    
    # Aplica el stylesheet al aplicativo
    #app.setStyleSheet(style_sheet)

    window = MainWindow()
    sys.exit(app.exec())
