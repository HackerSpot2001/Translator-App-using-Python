#!/usr/bin/python3
from PyQt5.QtWidgets import QLabel, QMainWindow,QApplication,QPushButton,QTextEdit,QLineEdit
from PyQt5 import uic
from googletrans import Translator
from speech_recognition import Recognizer,Microphone
import sys

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("main.ui",self)
        self.lineEdit = self.findChild(QLineEdit,"lineEdit")
        self.label_2 = self.findChild(QLabel,"label_2")
        self.textEdit = self.findChild(QTextEdit,"textEdit")
        self.pushButton = self.findChild(QPushButton,"pushButton")
        self.pushButton2 = self.findChild(QPushButton,"pushButton_2")
        self.pushButton.clicked.connect(self.translateText)
        self.pushButton2.clicked.connect(self.textFromMic)
        self.setMaximumSize(1000,600)
        self.setMinimumSize(1000,600)

    def translateText(self):
        self.textEdit.setText("")
        txt = self.lineEdit.text()
        if len(txt) != 0:
            try:
                translator = Translator()
                data = translator.translate(txt,src="en",dest="hi").text
                self.textEdit.setText(str(data))
                self.lineEdit.setText("")

            except Exception as e:
                print("Error: ",e)

        else:
            print("Enter some text")
    
    def textFromMic(self):
        r = Recognizer()
        with Microphone() as source:
            self.label_2.setText("Listening.......")
            audio = r.listen(source)
        
        try:
            self.label_2.setText("Recognizing your text .......")
            txt = r.recognize_google(audio,language="en-in")
            txt1 = self.lineEdit.setText(txt)
            if len(txt) != 0:
                try:
                    translator = Translator()
                    data = translator.translate(txt,src="en",dest="hi").text
                    self.textEdit.setText(str(data))
                    self.lineEdit.setText("")

                except Exception as e:
                    print("Error: ",e)

            else:
                print("Enter some text")

        except Exception as e:
            print(e)

        self.label_2.setText("")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec())