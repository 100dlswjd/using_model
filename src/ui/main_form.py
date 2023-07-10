# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(347, 298)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_select_model = QLabel(self.centralwidget)
        self.label_select_model.setObjectName(u"label_select_model")

        self.horizontalLayout.addWidget(self.label_select_model)

        self.pushButton_select_model = QPushButton(self.centralwidget)
        self.pushButton_select_model.setObjectName(u"pushButton_select_model")

        self.horizontalLayout.addWidget(self.pushButton_select_model)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.label_select_label = QLabel(self.centralwidget)
        self.label_select_label.setObjectName(u"label_select_label")

        self.horizontalLayout_5.addWidget(self.label_select_label)

        self.pushButton_select_label = QPushButton(self.centralwidget)
        self.pushButton_select_label.setObjectName(u"pushButton_select_label")

        self.horizontalLayout_5.addWidget(self.pushButton_select_label)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.label_select_image = QLabel(self.centralwidget)
        self.label_select_image.setObjectName(u"label_select_image")

        self.horizontalLayout_2.addWidget(self.label_select_image)

        self.pushButton_select_image = QPushButton(self.centralwidget)
        self.pushButton_select_image.setObjectName(u"pushButton_select_image")

        self.horizontalLayout_2.addWidget(self.pushButton_select_image)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.label_image_pixmap = QLabel(self.centralwidget)
        self.label_image_pixmap.setObjectName(u"label_image_pixmap")
        self.label_image_pixmap.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_image_pixmap)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton_classify = QPushButton(self.centralwidget)
        self.pushButton_classify.setObjectName(u"pushButton_classify")

        self.verticalLayout.addWidget(self.pushButton_classify)

        self.label_classify_result = QLabel(self.centralwidget)
        self.label_classify_result.setObjectName(u"label_classify_result")
        self.label_classify_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_classify_result)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 347, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_select_model.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\ub41c \ubaa8\ub378", None))
        self.pushButton_select_model.setText(QCoreApplication.translate("MainWindow", u"\ubaa8\ub378 \uc120\ud0dd", None))
        self.label_select_label.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\ub41c \ub77c\ubca8", None))
        self.pushButton_select_label.setText(QCoreApplication.translate("MainWindow", u"\ub77c\ubca8 \uc120\ud0dd", None))
        self.label_select_image.setText(QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\ub41c \uc774\ubbf8\uc9c0", None))
        self.pushButton_select_image.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \uc120\ud0dd", None))
        self.label_image_pixmap.setText(QCoreApplication.translate("MainWindow", u"img_pixmap", None))
        self.pushButton_classify.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubbf8\uc9c0 \ubd84\ub958\ud558\uae30", None))
        self.label_classify_result.setText(QCoreApplication.translate("MainWindow", u"\ubd84\ub958 \uacb0\uacfc", None))
    # retranslateUi

