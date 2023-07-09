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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(195, 182)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.label_select_model = QLabel(Form)
        self.label_select_model.setObjectName(u"label_select_model")

        self.horizontalLayout.addWidget(self.label_select_model)

        self.pushButton_select_model = QPushButton(Form)
        self.pushButton_select_model.setObjectName(u"pushButton_select_model")

        self.horizontalLayout.addWidget(self.pushButton_select_model)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.label_select_image = QLabel(Form)
        self.label_select_image.setObjectName(u"label_select_image")

        self.horizontalLayout_2.addWidget(self.label_select_image)

        self.pushButton_select_image = QPushButton(Form)
        self.pushButton_select_image.setObjectName(u"pushButton_select_image")

        self.horizontalLayout_2.addWidget(self.pushButton_select_image)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.label_image_pixmap = QLabel(Form)
        self.label_image_pixmap.setObjectName(u"label_image_pixmap")
        self.label_image_pixmap.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_image_pixmap)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButton_classify = QPushButton(Form)
        self.pushButton_classify.setObjectName(u"pushButton_classify")

        self.verticalLayout.addWidget(self.pushButton_classify)

        self.label_classify_result = QLabel(Form)
        self.label_classify_result.setObjectName(u"label_classify_result")
        self.label_classify_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_classify_result)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_select_model.setText(QCoreApplication.translate("Form", u"\uc120\ud0dd\ub41c \ubaa8\ub378", None))
        self.pushButton_select_model.setText(QCoreApplication.translate("Form", u"\ubaa8\ub378 \uc120\ud0dd", None))
        self.label_select_image.setText(QCoreApplication.translate("Form", u"\uc120\ud0dd\ub41c \uc774\ubbf8\uc9c0", None))
        self.pushButton_select_image.setText(QCoreApplication.translate("Form", u"\uc774\ubbf8\uc9c0 \uc120\ud0dd", None))
        self.label_image_pixmap.setText(QCoreApplication.translate("Form", u"img_pixmap", None))
        self.pushButton_classify.setText(QCoreApplication.translate("Form", u"\uc774\ubbf8\uc9c0 \ubd84\ub958\ud558\uae30", None))
        self.label_classify_result.setText(QCoreApplication.translate("Form", u"\ubd84\ub958 \uacb0\uacfc", None))
    # retranslateUi

