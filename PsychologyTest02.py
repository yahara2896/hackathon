


import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import webbrowser

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):


        self.resize(500,500)
        self.move(200,200)
        self.setWindowTitle('Psychology Test')

        self.Q = QLabel('あなたは現在，18歳の青少年です．高校最後の思い出に友達と一緒に何かを盗もうという話になりました．あなたは何を盗みますか?')
        self.btn1 = QPushButton('プリンター')
        self.btn2 = QPushButton('電動アシスト自転車')
        self.btn3 = QPushButton('とんかつソース')
        self.btn4 = QPushButton('パルテノン神殿')
        self.btn5 = QPushButton('何も盗まない')

        grid = QGridLayout()
        grid.addWidget(self.Q, 0, 0)
        grid.addWidget(self.btn1, 1, 0)
        grid.addWidget(self.btn2, 2, 0)
        grid.addWidget(self.btn3, 3, 0)
        grid.addWidget(self.btn4, 4, 0)
        grid.addWidget(self.btn5, 5, 0)

        self.btn1.clicked.connect(self.select1)
        self.btn2.clicked.connect(self.select2)
        self.btn3.clicked.connect(self.select3)
        self.btn4.clicked.connect(self.select4)
        self.btn5.clicked.connect(self.select5)
                
        self.setLayout(grid)

        self.show()        
        
    def select1(self):
        self.Q.setText('それはどこで盗みますか') 
        self.btn1.setText('電気屋')
        self.btn2.setText('プリンター屋さん')
        self.btn3.setText('パソコン屋さん')
        self.btn4.setText('N/D')
        self.btn5.setText('ひとつ前の質問に戻る')

        self.btn4.setDisabled(True)
        self.btn1.clicked.connect(self.answer)
        self.btn2.clicked.connect(self.answer)
        self.btn3.clicked.connect(self.answer)
        self.btn5.clicked.connect(self.select0)

    def select2(self):
        
        self.Q.setText('それはどこで盗みますか') 
        self.btn1.setText('電気屋')
        self.btn2.setText('自転車屋')
        self.btn3.setText('自転車置き場')
        self.btn4.setText('N/D')
        self.btn5.setText('ひとつ前の質問に戻る')
        
        self.btn4.setDisabled(True)
        self.btn1.clicked.connect(self.answer)
        self.btn2.clicked.connect(self.answer)
        self.btn3.clicked.connect(self.answer)
        self.btn5.clicked.connect(self.select0)

    def select3(self):
        
        self.Q.setText('それはどこで盗みますか') 
        self.btn1.setText('スーパー')
        self.btn2.setText('カレー屋さん')
        self.btn3.setText('とんかつ屋さん')
        self.btn4.setText('N/D')
        self.btn5.setText('ひとつ前の質問に戻る')
        
        self.btn4.setDisabled(True)

        self.btn1.clicked.connect(self.answer)
        self.btn2.clicked.connect(self.answer)
        self.btn3.clicked.connect(self.answer)
        self.btn5.clicked.connect(self.select0)

    def select4(self):
        
        self.Q.setText('それはどこで盗みますか') 
        self.btn1.setText('ギリシャ，アテネ')
        self.btn2.setText('模型屋')
        self.btn3.setText('お土産物屋さん')
        self.btn4.setText('N/D')
        self.btn5.setText('ひとつ前の質問に戻る')

        self.btn4.setDisabled(True)

        self.btn1.clicked.connect(self.answer)
        self.btn2.clicked.connect(self.answer)
        self.btn3.clicked.connect(self.answer)
        self.btn5.clicked.connect(self.select0)







    def select5(self):
        
        self.Q.setText('それはどこで盗みますか') 
        self.btn1.setText('盗まないためにどこにもない')
        self.btn2.setText('やっぱり盗む')
        self.btn3.setText('N/D')
        self.btn4.setText('N/D')
        self.btn5.setText('前の質問へ戻る')

        self.btn4.setDisabled(True)
        self.btn3.setDisabled(True)

        self.btn1.clicked.connect(self.answer)
        self.btn2.clicked.connect(self.select0)
        self.btn5.clicked.connect(self.select0)

    def select0(self):
        
        self.Q.setText('あなたは現在，18歳の青少年です．高校最後の思い出に友達と一緒に何かを盗もうという話になりました．あなたは何を盗みますか?') 
        self.btn1.setText('プリンター')
        self.btn2.setText('電動アシスト自転車')
        self.btn3.setText('とんかつソース')
        self.btn4.setText('パルテノン神殿')
        self.btn5.setText('何も盗まない')

        self.btn4.setDisabled(False)
        self.btn3.setDisabled(False)

        self.btn1.clicked.connect(self.select1)
        self.btn2.clicked.connect(self.select2)
        self.btn3.clicked.connect(self.select3)
        self.btn4.clicked.connect(self.select4)
        self.btn5.clicked.connect(self.select5)
        
    def answer(self):

        self.btn1.hide()
        self.btn2.hide()
        self.btn3.hide()
       # self.btn3.setText("はじめから")
        self.btn4.setDisabled(False)
        self.btn4.setText('もっと心理テストをしたい場合はこちら')
        self.btn5.setText('欲しいものを買う')
        

        self.Q.setText("1つ目の質問はあなたの器の大きさ，2つ目の質問はあなたが今必要としているものがある場所を表しています．")
        
       # self.btn3.clicked.connect(self.select0)
        self.btn4.clicked.connect(self.url)
        self.btn5.clicked.connect(self.url2)

    def url(self):

        initurl = 'https://matome.naver.jp/odai/2134933856191786901'
        webbrowser.open(initurl)
        QCoreApplication.instance().quit
        
    def url2(self):

        initurl2 = 'https://www.amazon.co.jp'
        webbrowser.open(initurl2)
        QCoreApplication.instance().quit

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())

        

