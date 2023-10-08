import sys
import warnings
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QHBoxLayout, QLabel
from PyQt5.QtGui import *
from PyQt5 import QtCore
from kexinxing6 import Ui_MainWindow


class DetailUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(DetailUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('智能计算系统可信性评估平台')
        self.timer = QtCore.QTimer(self)

        # self.pushButton_fenlei_j.clicked.connect(self.main_fenlei)
        # self.pushButton_juece_j.clicked.connect(self.main_juece)

        # self.pushButton_recognation.clicked.connect(self.main_fenlei)
        # self.pushButton_zizhu.clicked.connect(self.main_zizhu)
        # self.pushButton_decision.clicked.connect(self.main_juece)

    def main_fenlei(self):
        self.timer.stop()
        self.frame_gener.show()
        self.label_gener.show()
        self.frame_robust.show()
        self.label_robust.show()
        self.frame_data.show()
        self.frame_white.show()
        self.label_data.show()
        self.label_white.show()

        self.frame_gener_j.hide()
        self.label_gener_j.hide()
        self.frame_generdata_j.hide()
        self.frame_robustdata_j.hide()
        self.frame_show_j.hide()
        self.label_generdata_j.hide()
        self.label_robustdata_j.hide()
        self.label_data_j.hide()
        self.frame_robust_j.hide()
        self.label_robust_j.hide()

        self.frame_gengxin.hide()
        self.frame_xuexi.hide()
        self.label_rengong.hide()
        self.frame_juece_zizhu.hide()
        self.frame_shibie_zizhu.hide()
        self.label_gener_renwu.hide()
        self.frame_huanjing.hide()
        self.frame_result_zizhu.hide()
        self.label_gener_huanjing.hide()
        self.label_gener_result_zizhu.hide()
        self.label_6.hide()

    def main_juece(self):
        self.timer.stop()
        self.frame_gener.hide()
        self.label_gener.hide()
        self.frame_robust.hide()
        self.label_robust.hide()
        self.frame_data.hide()
        self.frame_white.hide()
        self.label_data.hide()
        self.label_white.hide()

        self.frame_gengxin.hide()
        self.frame_xuexi.hide()
        self.label_rengong.hide()
        self.frame_juece_zizhu.hide()
        self.frame_shibie_zizhu.hide()
        self.label_gener_renwu.hide()
        self.frame_huanjing.hide()
        self.frame_result_zizhu.hide()
        self.label_gener_huanjing.hide()
        self.label_gener_result_zizhu.hide()
        self.label_6.hide()

        self.frame_gener_j.show()
        self.label_gener_j.show()
        self.frame_generdata_j.show()
        self.frame_robustdata_j.show()
        self.frame_show_j.show()
        self.label_generdata_j.show()
        self.label_robustdata_j.show()
        self.label_data_j.show()
        self.frame_robust_j.show()
        self.label_robust_j.show()

    def main_zizhu(self):
        self.timer.stop()
        self.frame_gener.hide()
        self.label_gener.hide()
        self.frame_robust.hide()
        self.label_robust.hide()
        self.frame_data.hide()
        self.frame_white.hide()
        self.label_data.hide()
        self.label_white.hide()

        self.frame_gengxin.show()
        self.frame_xuexi.show()
        self.label_rengong.show()
        self.frame_juece_zizhu.show()
        self.frame_shibie_zizhu.show()
        self.label_gener_renwu.show()
        self.frame_huanjing.show()
        self.frame_result_zizhu.show()
        self.label_gener_huanjing.show()
        self.label_gener_result_zizhu.show()
        self.label_6.show()

        self.frame_gener_j.hide()
        self.label_gener_j.hide()
        self.frame_generdata_j.hide()
        self.frame_robustdata_j.hide()
        self.frame_show_j.hide()
        self.label_generdata_j.hide()
        self.label_robustdata_j.hide()
        self.label_data_j.hide()
        self.frame_robust_j.hide()
        self.label_robust_j.hide()


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    ex = DetailUI()
    ex.show()
    sys.exit(app.exec_())