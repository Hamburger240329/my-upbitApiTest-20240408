import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *  # PyQt5 는 윈도우를 만들어 주는 애. 스레드로 만들어야 함

class SignalThread(QThread):  # signal 파트
    signal1 = pyqtSignal()  # signal 함수
    signal2 = pyqtSignal(int, int)  # signal # 윈도우로 전달할 값의 타입을 넣어줌(int 2개를 보내보자)

    def run(self):  # 6줄 ~ 8줄은 픽스값. 동일한 형식으로 만드는 것)
        self.signal1.emit()
        self.signal2.emit(1000, 2000)

class MeinWin(QMainWindow):
    def __init__(self):
        super().__init__()
        signalClass = SignalThread()

        signalClass.signal1.connect(self.signal1_print)
        # 시그널 함수와 슬롯함수를 연결
        signalClass.signal2.connect(self.signal2_print)
        # 시그널 함수와 슬롯함수를 연결
        signalClass.run()
        
    @pyqtSlot()
    def signal1_print(self):  # slot 함수
        print(f"signal1 제출됨(emit!!")

    @pyqtSlot(int, int)
    def signal2_print(self, int1, int2):  # slot 함수
        print(f"signal2 제출됨(emit!!->{int1}, {int2}")
        # 실제 프로그램에서는 윈도우에 출력하는 내용이 와야함

app = QApplication(sys.argv)
win = MeinWin()
win.show()
sys.exit(app.exec_())




