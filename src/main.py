import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtCore import Signal, Slot, QObject
from PySide6.QtGui import QPixmap

from ui.main_form import Ui_MainWindow

from threading import Thread

class Check_signal(QObject):
    check = Signal(bool)

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.check_signal = Check_signal()
        self.label_file_path = ""
        self.image_file_path = ""
        self.model_file_path = ""
        self.pushButton_classify.clicked.connect(self.btn_classify_handler)
        self.pushButton_select_label.clicked.connect(self.btn_select_label_handler)
        self.pushButton_select_model.clicked.connect(self.btn_select_model_handler)
        self.pushButton_select_image.clicked.connect(self.btn_select_image_handler)

        self.check_signal.check.connect(self.check_signal_handler)
        self.setWindowTitle("이미지 분류")
        self.pushButton_classify.setEnabled(False)

    @Slot()    
    def btn_select_label_handler(self):
        file = QFileDialog.getOpenFileName(self, "라벨 파일 선택", "", "Label Files (*.txt)")
        if file[0]:
            self.label_file_path = file[0]
            self.label_select_label.setText(file[0])
            self.classes_number = []
            with open(file[0], 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    self.classes_number.append(line.strip())
        
        self.classes_btn_check()

    @Slot()
    def btn_select_model_handler(self):
        file = QFileDialog.getOpenFileName(self, "모델 파일 선택", "", "Model Files (*.h5)")
        if file[0]:
            self.label_select_model.setText(file[0])
            self.model_file_path = file[0]
        
        self.classes_btn_check()

    @Slot()
    def btn_select_image_handler(self):
        file = QFileDialog.getOpenFileName(self, "이미지 파일 선택", "", "Image Files (*.png *.jpg *.bmp)")
        
        if file[0]:
            self.image_file_path = file[0]
            self.label_select_image.setText(file[0])
            img = QPixmap(file[0])
            while img.size().width() > 300:
                img = img.scaled(img.size().width()/2, img.size().height()/2)
            self.label_image_pixmap.setPixmap(img)
        
        self.classes_btn_check()

    @Slot()
    def btn_classify_handler(self):
        self.pushButton_classify.setEnabled(False)
        self.pushButton_classify.setText("처리중...")
        work_thread = Thread( target=self.work, args=(self.check_signal, self.classes_number, self.model_file_path, self.image_file_path) )
        work_thread.start()
    
    def work(self, check_signal: Check_signal, classes_number : list, model_file_path: str, image_file_path: str):
        import os
        import matplotlib.pyplot as plt
        import numpy as np
        import keras.utils as image
        import tensorflow as tf

        model = tf.keras.models.load_model(model_file_path)

        classes_image = image.load_img(image_file_path, color_mode='grayscale', target_size=(150, 150), interpolation='bilinear')
        classes_image = image.img_to_array(classes_image)
        classes_image = np.expand_dims(classes_image, axis=0)
        classes_image = np.vstack([classes_image])

        classes = model.predict(classes_image, batch_size=10)

        for idx in classes_number:            
            if int(classes[0][0]) == int(idx[0]):
                self.label_classify_result.setText(f"이미지 분류 결과: {idx[1:]}")
                break

        check_signal.check.emit(True)

    def classes_btn_check(self):
        if self.label_file_path and self.model_file_path and self.image_file_path:
            self.pushButton_classify.setEnabled(True)
        else:
            self.pushButton_classify.setEnabled(False)

    @Slot(bool)
    def check_signal_handler(self, check):
        if check:
            self.pushButton_classify.setEnabled(True)
            self.pushButton_classify.setText("이미지 분류하기")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    window.show()
    app.exec()
