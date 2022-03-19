
        self.menuANPR = QtWidgets.QMenu(self.menubar)
        self.menuANPR.setObjectName("menuANPR")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuANPR.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.entry)
        self.pushButton_2.clicked.connect(self.exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Entry"))
        self.pushButton_2.setText(_translate("MainWindow", "Exit"))
        self.menuANPR.setTitle(_translate("MainWindow", "ANPR"))

    def entry(self):
        video_final.forDesign(1)

    def exit(self):
        video_final.forDesign(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
