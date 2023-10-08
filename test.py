import sys
import warnings
import shutil
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QHBoxLayout, QLabel
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtWidgets
from kexinxing import Ui_MainWindow, Ui_MainWindow1
from generalization import load_data, Generalization
import robustness, chouqu, robust1_exp, robust2_exp, robust3_exp, readtxt, robust, robust2, robust3
import generalization_j, robustness_j, Test_case_generation_gai, noise_true, noise, noise_exp
import gener_net, gener_net2, robust_net, robust_net2, noise_net
import evaluate, unbalance

global datapath1, datapath2, image_path, RRpath, image_path1, image_path2, image_path3, image_path4, image_path5, RDpath1, \
    RDpath2, RDR1path1, RDR1path2, RDR2path1, RDR2path2, RDR3path1, RDR3path2, GTpath1, JRpath2
global datapath3, datapath4, datapath5, datapath6, image_path6, image_path7, image_path8, image_path9
global score
global image_path_C
score = -1
datapath41 = None
datapath51 = None
# datapath511 = None
JRpath211 = None
JRpath11 = None
import profile

class EmittingStr(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


class DetailUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(DetailUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('智能计算系统可信性评估平台')
        self.timer = QtCore.QTimer(self)

        self.pushButton_data.clicked.connect(self.main_data)
        self.pushButton_recognation.clicked.connect(self.main_fenlei)
        self.pushButton_decision.clicked.connect(self.main_juece)
        self.pushButton_decision2.clicked.connect(self.main_juece2)
        self.pushButton_zizhu.clicked.connect(self.main_zizhu)

        self.pushButton_generdata.clicked.connect(self.data_gener)
        self.pushButton_noise.clicked.connect(self.data_noise)
        self.pushButton_zhedang.clicked.connect(self.data_zhedang)
        self.pushButton_gauss.clicked.connect(self.data_gauss)

        self.pushButton_y_pred_A.clicked.connect(self.RG_input1)
        self.pushButton_y_true_A.clicked.connect(self.RG_input2)
        self.pushButton_run_A.clicked.connect(self.RG_run)

        self.pushButton_input1_r.clicked.connect(self.RR_input1)
        self.pushButton_run_r.clicked.connect(self.RR_run)

        self.pushButton_filedir_gener.clicked.connect(self.RD_input1)
        self.pushButton_tardir_gener.clicked.connect(self.RD_input2)
        self.pushButton_run_gener.clicked.connect(self.RD_run)

        self.pushButton_filedir_gener_N.clicked.connect(self.RDR1_input1)
        self.pushButton_tardir_gener_N.clicked.connect(self.RDR1_input2)
        self.pushButton_run_gener_N.clicked.connect(self.RDR1_run)

        self.pushButton_filedir_gener_Z.clicked.connect(self.RDR2_input1)
        self.pushButton_tardir_gener_Z.clicked.connect(self.RDR2_input2)
        self.pushButton_run_gener_Z.clicked.connect(self.RDR2_run)

        self.pushButton_filedir_gener_G.clicked.connect(self.RDR3_input1)
        self.pushButton_tardir_gener_G.clicked.connect(self.RDR3_input2)
        self.pushButton_run_gener_G.clicked.connect(self.RDR3_run)

        self.pushButton_ASS.clicked.connect(self.ASS)
        self.pushButton_ACAC.clicked.connect(self.ACAC)
        self.pushButton_ACTC.clicked.connect(self.ACTC)
        self.pushButton_BD.clicked.connect(self.BD)
        self.pushButton_SNAC.clicked.connect(self.SNAC)
        self.pushButton_ALDp.clicked.connect(self.ALDp)
        self.pushButton_KMNC.clicked.connect(self.KMNC)
        self.pushButton_ENI.clicked.connect(self.ENI)
        self.pushButton_NTE.clicked.connect(self.NTE)
        self.pushButton_NBC.clicked.connect(self.NBC)
        self.pushButton_NC.clicked.connect(self.NC)
        self.pushButton_PSD.clicked.connect(self.PSD)
        self.pushButton_TKNP.clicked.connect(self.TKNP)
        self.pushButton_TKNC.clicked.connect(self.TKNP)
        self.pushButton_RGB.clicked.connect(self.RGB)
        self.pushButton_RIC.clicked.connect(self.RIC)

        self.pushButton_run_ACAC.clicked.connect(self.ACAC_run)
        self.pushButton_run_ACTC.clicked.connect(self.ACTC_run)
        self.pushButton_run_ASS.clicked.connect(self.ASS_run)
        self.pushButton_run_BD.clicked.connect(self.BD_run)
        self.pushButton_run_SNAC.clicked.connect(self.SNAC_run)
        self.pushButton_run_ALDp.clicked.connect(self.ALDp_run)
        self.pushButton_run_KMNC.clicked.connect(self.KMNC_run)
        self.pushButton_run_ENI.clicked.connect(self.ENI_run)
        self.pushButton_run_NBC.clicked.connect(self.NBC_run)
        self.pushButton_run_NTE.clicked.connect(self.NTE_run)
        self.pushButton_run_NC.clicked.connect(self.NC_run)
        self.pushButton_run_PSD.clicked.connect(self.PSD_run)
        self.pushButton_run_TKNC.clicked.connect(self.TKNC_run)
        self.pushButton_run_TKNP.clicked.connect(self.TKNP_run)
        self.pushButton_run_RIC.clicked.connect(self.RIC_run)
        self.pushButton_run_RGB.clicked.connect(self.RGB_run)

        self.pushButton_filepath_white.clicked.connect(self.GT_input1)
        # self.pushButton_run_white.clicked.connect(self.GT_run)
        # self.pushButton_run_ACTC.clicked.connect(self.GT_run)
        # self.pushButton_run_ACAC.clicked.connect(self.GT_run)
        # self.pushButton_run_ASS.clicked.connect(self.GT_run)
        # self.pushButton_run_ALDp.clicked.connect(self.GT_run)
        # self.pushButton_run_BD.clicked.connect(self.GT_run)
        # self.pushButton_run_ENI.clicked.connect(self.GT_run)
        # self.pushButton_run_KMNC.clicked.connect(self.GT_run)
        # self.pushButton_run_NBC.clicked.connect(self.GT_run)
        # self.pushButton_run_NC.clicked.connect(self.GT_run)
        # self.pushButton_run_NTE.clicked.connect(self.GT_run)
        # self.pushButton_run_PSD.clicked.connect(self.GT_run)
        # self.pushButton_run_SNAC.clicked.connect(self.GT_run)
        # self.pushButton_run_TKNC.clicked.connect(self.GT_run)
        # self.pushButton_run_TKNP.clicked.connect(self.GT_run)
        # self.pushButton_run_RIC.clicked.connect(self.GT_run)
        # self.pushButton_run_RGB.clicked.connect(self.GT_run)

        self.pushButton_y_pred_A_j.clicked.connect(self.JG_input1)
        self.pushButton_y_true_A_j.clicked.connect(self.JG_input2)
        self.pushButton_run_A_j.clicked.connect(self.JG_run)

        self.pushButton_ypred_j.clicked.connect(self.JR_input2)
        self.pushButton_input1_r_j.clicked.connect(self.JR_input1)
        self.pushButton_run_r_j_2.clicked.connect(self.JR_run)

        self.pushButton_sourcedir_g_j.clicked.connect(self.JD_input1)
        self.pushButton__tardir_g_j.clicked.connect(self.JD_input2)
        self.pushButton_run_g_j.clicked.connect(self.JD_run)

        self.pushButton_source_r_j.clicked.connect(self.JDR_input1)
        self.pushButton_tardir_r_j.clicked.connect(self.JDR_input2)
        # self.pushButton_changedir_r_j.clicked.connect(self.JDR_input3)
        self.pushButton_run_r_j.clicked.connect(self.JDR_run)

        self.pushButton_y_pred_j2.clicked.connect(self.JG2_input1)
        self.pushButton_y_pred1_j2.clicked.connect(self.JG2_input3)
        self.pushButton_y_true_j2.clicked.connect(self.JG2_input2)
        self.pushButton_run_j2.clicked.connect(self.JG2_run)

        self.pushButton_ypred_j2.clicked.connect(self.JR2_input1)
        self.pushButton_input1_r_j2.clicked.connect(self.JR2_input2)
        self.pushButton_input2_r_j2.clicked.connect(self.JR2_input3)
        self.pushButton_run_r_j2_2.clicked.connect(self.JR2_run)

        self.pushButton_source_r_j2.clicked.connect(self.JD2_input1)
        self.pushButton_tardir_r_j2.clicked.connect(self.JD2_input2)
        # self.pushButton_changedir_r_j.clicked.connect(self.JDR_input3)
        self.pushButton_run_r_j2.clicked.connect(self.J2DR_run)

        self.pushButton_21.clicked.connect(self.score_calculate)
        self.pushButton_27.clicked.connect(self.score_zero)

        self.pushButton_C.clicked.connect(self.btnClicked_DC)
        self.pushButton_ROC.clicked.connect(self.btnClicked_DR)
        self.pushButton_A.clicked.connect(self.btnClicked_DA)
        self.pushButton_P.clicked.connect(self.btnClicked_DP)
        self.pushButton_R.clicked.connect(self.btnClicked_DRE)
        self.pushButton_ROC_j.clicked.connect(self.btnClicked_DROCJ)
        self.pushButton_A_j.clicked.connect(self.btnClicked_DAJ)
        self.pushButton_P_j.clicked.connect(self.btnClicked_DPJ)
        self.pushButton_R_j.clicked.connect(self.btnClicked_DRJ)

        self.pushButton_JFGWC.clicked.connect(self.btnClicked_JFWC)
        self.pushButton_PJJDWC.clicked.connect(self.btnClicked_PJJDWC)
        self.pushButton_PJJDBFBWC.clicked.connect(self.btnClicked_PJJDBFBWC)
        self.pushButton_PCL.clicked.connect(self.btnClicked_JDXS)
        self.pushButton_FCL.clicked.connect(self.btnClicked_ZWSJDWC)
        self.pushButton_XEBDXS.clicked.connect(self.btnClicked_XEBDXS)
        self.pushButton_XFCL.clicked.connect(self.btnClicked_FCL)
        self.pushButton_JSFCFS.clicked.connect(self.btnClicked_JSFCFS)
        self.pushButton_MSLE.clicked.connect(self.btnClicked_JFGWC)
        self.pushButton_pjjdwc.clicked.connect(self.btnClicked_PJJDWC_R)
        self.pushButton_jfgwc.clicked.connect(self.btnClicked_JFGWC_R)
        self.pushButton_jsfcfs.clicked.connect(self.btnClicked_ZWSJDWC_R)

        self.pushButton_dataeva.clicked.connect(self.DATAEVA_input)
        self.pushButton_run_dataeva.clicked.connect(self.DATAEVA_run)

        self.pushButton_SD_filter.clicked.connect(self.DATASET_SD)
        self.pushButton_TS_filter.clicked.connect(self.DATASET_TD)
        self.pushButton_run_filter.clicked.connect(self.DATASET_run)

        self.pushButton_SD_dataset.clicked.connect(self.DATASETADV_SD)
        self.pushButton_TD_dataset.clicked.connect(self.DATASETADV_TD)
        self.pushButton_YX_dataset.clicked.connect(self.DATASETADV_run)

        self.pushButton_FSBH.clicked.connect(self.btnClicked_FSBH)
        self.pushButton_CJ.clicked.connect(self.btnClicked_CJ)
        self.pushButton_GBYSKJ.clicked.connect(self.btnClicked_GBYSKJ)
        self.pushButton_SIG.clicked.connect(self.btnClicked_SIG)
        self.pushButton_FZ.clicked.connect(self.btnClicked_FZ)
        self.pushButton_HDT.clicked.connect(self.btnClicked_HDT)
        self.pushButton_GAMMA.clicked.connect(self.btnClicked_GAMMA)
        self.pushButton_XXDBD.clicked.connect(self.btnClicked_XXDBD)
        self.pushButton_GSZY.clicked.connect(self.btnClicked_GSZY)
        self.pushButton_GSMH.clicked.connect(self.btnClicked_GSMH)
        self.pushButton_ZZMH.clicked.connect(self.btnClicked_ZZMH)
        self.pushButton_SBMH.clicked.connect(self.btnClicked_SBMH)
        self.pushButton_PJMH.clicked.connect(self.btnClicked_PJMH)
        self.pushButton_YDMH.clicked.connect(self.btnClicked_YDMH)
        self.pushButton_SCKJ.clicked.connect(self.btnClicked_SCKJ)
        self.pushButton_SJSDBHD.clicked.connect(self.btnClicked_SJSDHBHD)

        # sys.stdout = EmittingStr(textWritten=self.outputWritten_RGA)
        # sys.stderr = EmittingStr(textWritten=self.outputWritten_RGA)

    # 图像放大
    def btnClicked_DC(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.DC()

    def btnClicked_DR(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.DR()

    def btnClicked_DA(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.DA()

    def btnClicked_DP(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.DP()

    def btnClicked_DRE(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.DRE()

    def btnClicked_DROCJ(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.DROCJ()

    def btnClicked_DAJ(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.DAJ()

    def btnClicked_DPJ(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.DPJ()

    def btnClicked_DRJ(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.DRJ()

    def btnClicked_JFWC(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.JFWC()

    def btnClicked_PJJDWC(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.PJJDWC()

    def btnClicked_PJJDBFBWC(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.PJJDBFBWC()

    def btnClicked_JDXS(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.JDXS()

    def btnClicked_ZWSJDWC(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.ZWSJDWC()

    def btnClicked_PJJDBFBWC(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.PJJDBFBWC()

    def btnClicked_XEBDXS(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.XEBDXS()

    def btnClicked_JSFCFS(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.JSFCFS()

    def btnClicked_FCL(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.FCL()

    def btnClicked_JFGWC(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.JFGWC()

    def btnClicked_PJJDWC_R(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.J2R1()

    def btnClicked_ZWSJDWC_R(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.J2R2()

    def btnClicked_JFGWC_R(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.J2R3()

    def btnClicked_FSBH(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.FSBH()

    def btnClicked_CJ(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.CJ()

    def btnClicked_GBYSKJ(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.GBYSKJ()

    def btnClicked_SIG(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.SIG()

    def btnClicked_FZ(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.FZ()

    def btnClicked_HDT(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.HDT()

    def btnClicked_GAMMA(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.GAMMA()

    def btnClicked_XXDBD(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.XXDBD()

    def btnClicked_GSZY(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.GSZY()

    def btnClicked_GSMH(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.GSMH()

    def btnClicked_PJMH(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.PJMH()

    def btnClicked_ZZMH(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.ZZMH()

    def btnClicked_YDMH(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.YDMH()

    def btnClicked_SBMH(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.SBMH()

    def btnClicked_SCKJ(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.SCKJ()

    def btnClicked_SJSDHBHD(self):
        self.chile_Win = Ui_MainWindow1()
        self.chile_Win.show()
        # self.chile_Win.exec_()
        self.chile_Win.SJSDHBHD()

    # 界面转换
    def main_data(self):
        self.timer.stop()
        self.label_dataeva.show()
        self.frame_dataeva.show()
        self.label_filter.show()
        self.frame_filter.show()
        self.label_dataubl.show()
        self.frame_datasetadv.show()
        self.label_datasetadv.show()
        self.frame_gener.hide()
        self.label_gener.hide()
        self.frame_robust.hide()
        self.label_robust.hide()
        self.frame_data.hide()
        self.frame_white.hide()
        self.label_data.hide()
        self.label_white.hide()
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
        self.frame_gener_j2.hide()
        self.label_gener_j2.hide()
        self.frame_robustdata_j2.hide()
        self.frame_show_j2.hide()
        self.label_robustdata_j2.hide()
        self.label_data_j2.hide()
        self.frame_robust_j2.hide()
        self.label_robust_j2.hide()

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
        self.frame_gener_j2.hide()
        self.label_gener_j2.hide()
        self.frame_robustdata_j2.hide()
        self.frame_show_j2.hide()
        self.label_robustdata_j2.hide()
        self.label_data_j2.hide()
        self.frame_robust_j2.hide()
        self.label_robust_j2.hide()
        self.label_dataeva.hide()
        self.frame_dataeva.hide()
        self.label_filter.hide()
        self.frame_filter.hide()
        self.label_dataubl.hide()
        self.frame_datasetadv.hide()
        self.label_datasetadv.hide()

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
        self.frame_gener_j2.hide()
        self.label_gener_j2.hide()
        self.frame_robustdata_j2.hide()
        self.frame_show_j2.hide()
        self.label_robustdata_j2.hide()
        self.label_data_j2.hide()
        self.frame_robust_j2.hide()
        self.label_robust_j2.hide()
        self.label_dataeva.hide()
        self.frame_dataeva.hide()
        self.label_filter.hide()
        self.frame_filter.hide()
        self.label_dataubl.hide()
        self.frame_datasetadv.hide()
        self.label_datasetadv.hide()

    def main_juece2(self):
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
        self.frame_gener_j2.show()
        self.label_gener_j2.show()
        self.frame_robustdata_j2.show()
        self.frame_show_j2.show()
        self.label_robustdata_j2.show()
        self.label_data_j2.show()
        self.frame_robust_j2.show()
        self.label_robust_j2.show()
        self.label_dataeva.hide()
        self.frame_dataeva.hide()
        self.label_filter.hide()
        self.frame_filter.hide()
        self.label_dataubl.hide()
        self.frame_datasetadv.hide()
        self.label_datasetadv.hide()

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
        self.frame_gener_j2.hide()
        self.label_gener_j2.hide()
        self.frame_robustdata_j2.hide()
        self.frame_show_j2.hide()
        self.label_robustdata_j2.hide()
        self.label_data_j2.hide()
        self.frame_robust_j2.hide()
        self.label_robust_j2.hide()
        self.label_dataeva.hide()
        self.frame_dataeva.hide()
        self.label_filter.hide()
        self.frame_filter.hide()
        self.label_dataubl.hide()
        self.frame_datasetadv.hide()
        self.label_datasetadv.hide()

    def data_gener(self):
        self.textBrowser_show_data_gener.clear()
        self.pushButton_filedir_gener.show()
        self.pushButton_tardir_gener.show()
        self.pushButton_run_gener.show()
        self.label_guanjiancanshu_data_gener.show()
        self.label_num_gener.show()
        self.lineEdit_num_gener.show()
        self.pushButton_filedir_gener_N.hide()
        self.pushButton_tardir_gener_N.hide()
        self.pushButton_run_gener_N.hide()
        self.label_guanjiancanshu_data_gener_N.hide()
        self.label_num_gener_N.hide()
        self.lineEdit_num_gener_N.hide()
        self.pushButton_filedir_gener_Z.hide()
        self.pushButton_tardir_gener_Z.hide()
        self.pushButton_run_gener_Z.hide()
        self.label_guanjiancanshu_data_gener_Z.hide()
        self.label_num_gener_Z.hide()
        self.lineEdit_num_gener_Z.hide()
        self.pushButton_filedir_gener_G.hide()
        self.pushButton_tardir_gener_G.hide()
        self.pushButton_run_gener_G.hide()
        self.label_guanjiancanshu_data_gener_G.hide()
        self.label_num_gener_G.hide()
        self.lineEdit_num_gener_G.hide()

    def data_noise(self):
        self.textBrowser_show_data_gener.clear()
        self.pushButton_filedir_gener.hide()
        self.pushButton_tardir_gener.hide()
        self.pushButton_run_gener.hide()
        self.label_guanjiancanshu_data_gener.hide()
        self.label_num_gener.hide()
        self.lineEdit_num_gener.hide()
        self.pushButton_filedir_gener_N.show()
        self.pushButton_tardir_gener_N.show()
        self.pushButton_run_gener_N.show()
        self.label_guanjiancanshu_data_gener_N.show()
        self.label_num_gener_N.show()
        self.lineEdit_num_gener_N.show()
        self.pushButton_filedir_gener_Z.hide()
        self.pushButton_tardir_gener_Z.hide()
        self.pushButton_run_gener_Z.hide()
        self.label_guanjiancanshu_data_gener_Z.hide()
        self.label_num_gener_Z.hide()
        self.lineEdit_num_gener_Z.hide()
        self.pushButton_filedir_gener_G.hide()
        self.pushButton_tardir_gener_G.hide()
        self.pushButton_run_gener_G.hide()
        self.label_guanjiancanshu_data_gener_G.hide()
        self.label_num_gener_G.hide()
        self.lineEdit_num_gener_G.hide()

    def data_zhedang(self):
        self.textBrowser_show_data_gener.clear()
        self.pushButton_filedir_gener.hide()
        self.pushButton_tardir_gener.hide()
        self.pushButton_run_gener.hide()
        self.label_guanjiancanshu_data_gener.hide()
        self.label_num_gener.hide()
        self.lineEdit_num_gener.hide()
        self.pushButton_filedir_gener_N.hide()
        self.pushButton_tardir_gener_N.hide()
        self.pushButton_run_gener_N.hide()
        self.label_guanjiancanshu_data_gener_N.hide()
        self.label_num_gener_N.hide()
        self.lineEdit_num_gener_N.hide()
        self.pushButton_filedir_gener_Z.show()
        self.pushButton_tardir_gener_Z.show()
        self.pushButton_run_gener_Z.show()
        self.label_guanjiancanshu_data_gener_Z.show()
        self.label_num_gener_Z.show()
        self.lineEdit_num_gener_Z.show()
        self.pushButton_filedir_gener_G.hide()
        self.pushButton_tardir_gener_G.hide()
        self.pushButton_run_gener_G.hide()
        self.label_guanjiancanshu_data_gener_G.hide()
        self.label_num_gener_G.hide()
        self.lineEdit_num_gener_G.hide()

    def data_gauss(self):
        self.textBrowser_show_data_gener.clear()
        self.pushButton_filedir_gener.hide()
        self.pushButton_tardir_gener.hide()
        self.pushButton_run_gener.hide()
        self.label_guanjiancanshu_data_gener.hide()
        self.label_num_gener.hide()
        self.lineEdit_num_gener.hide()
        self.pushButton_filedir_gener_N.hide()
        self.pushButton_tardir_gener_N.hide()
        self.pushButton_run_gener_N.hide()
        self.label_guanjiancanshu_data_gener_N.hide()
        self.label_num_gener_N.hide()
        self.lineEdit_num_gener_N.hide()
        self.pushButton_filedir_gener_Z.hide()
        self.pushButton_tardir_gener_Z.hide()
        self.pushButton_run_gener_Z.hide()
        self.label_guanjiancanshu_data_gener_Z.hide()
        self.label_num_gener_Z.hide()
        self.lineEdit_num_gener_Z.hide()
        self.pushButton_filedir_gener_G.show()
        self.pushButton_tardir_gener_G.show()
        self.pushButton_run_gener_G.show()
        self.label_guanjiancanshu_data_gener_G.show()
        self.label_num_gener_G.show()
        self.lineEdit_num_gener_G.show()

    # 分类-特异性指标
    def ACAC(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.show()
        self.textBrowser_white_intro.append(
            '对错误类别的平均预测置信度。其定义为经过对抗攻击后，对于所有攻击成功对抗样本，所有误分类类别的平均概率。ACAC越小代表误分类的概率越低，所以ACAC越小越好。')

    def ACTC(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.show()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '正确类别平均置信度。通过对对抗攻击样本的真实类，计算预测可信度的平均值。ACTC越小代表攻击在越小程度上上偏离真实值，所以ACTC越小越好。')

    def ASS(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.show()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '平均结构相似性。ASS被定义为所有攻击成功对抗样本与其原始样本间的平均相似性。ASS值越大，则对抗样本的不可感知性越强，所以ASS越小越好。')

    def ALDp(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.show()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '平均Lp失真度。几乎所有的攻击都采用Lp norm距离（p=0,2,∞）作为评价的失真度量。具体来说，L0计算扰动后发生改变的像素数量；L2计算原始示例和扰动示例之间的欧氏距离；L∞测量对抗样本全维度下最大变化量。ALDp为所有攻击成功的对抗样本的平均归一化Lp失真度，ALDp越小，对抗样本的不可感知性越强，所以ALDp越小越好。')

    def RGB(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.show()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '对高斯模糊鲁棒性。高斯模糊常被用于计算机视觉算法中的图像去噪。RGB结果越高，说明对抗样本鲁棒性越强，所以RGB越大越好。')

    def RIC(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.show()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '对图像压缩鲁棒性。图像压缩常被用于计算机视觉算法中的图像去噪。RIC结果越高，说明对抗样本鲁棒性越强，所以RIC越大越好。')

    def TKNP(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.show()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            'Top-k神经元模式。从直观上看，top-k神经元模式代表了每一层顶层过度活跃神经元的不同激活场景。TKNP结果越高，说明对抗样本鲁棒性越差，所以TKNP越大越好。')

    def TKNC(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.show()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            'Top-k神经元覆盖。前k个神经元的覆盖量测量了每层上曾经最活跃的k个神经元的数量。定义为每一层的top-k神经元总数与DNN中神经元总数的比值。TKNC结果越高，说明对抗样本鲁棒性越差，所以TKNC越大越好。')

    def PSD(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.show()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '扰动敏感距离。用于评测人类对扰动的感知能力。PSD的值越小，则对抗样本的不可感知性越强，所以PSD越大越好。')

    def NC(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.show()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '神经元覆盖率，用于衡量测试数据是否可以对神经网络神经元进行覆盖。NC的值越高，说明对抗样本鲁棒性越好，所以NC越大越好。')

    def NTE(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.show()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '噪声容量估计。对抗样本的鲁棒性可通过噪声容限来估计，噪声容限反映了对抗样本在保持分类类别不变的情况下，可容忍的噪声量。具体来说，NTE计算了误分类概率与其他类最大概率之间的差值。NTE值越高，说明对抗样本的鲁棒性越高，所以NTE越大越好。')

    def NBC(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.show()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '神经元边界覆盖。神经元边界覆盖度量了给定的测试输入集T覆盖了多少个拐角区域(包括上边界和下边界值)。NBC的值越高，说明对抗样本鲁棒性越好，所以NBC越大越好。')

    def ENI(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.show()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '综合对抗攻击和自然噪音的一个test set。ENI值越低，攻击的不可感知性越强，所以ENI越大越好。')

    def KMNC(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.show()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            'K多节神经元覆盖。给定一个神经元n，k个多段神经元覆盖度量给定的测试输入集合T覆盖范围[lown, highn]的彻底程度。KMNC值越高，说明对抗样本鲁棒性越好，所以KMNC越大越好。')

    def SNAC(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.show()
        self.pushButton_run_BD.hide()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '强神经元激活覆盖。强神经元激活覆盖度量了给定的测试输入T覆盖了多少个角落情况。SNAC值越高，说明对抗样本鲁棒性越好，所以SNAC越大越好。')

    def BD(self):
        self.textBrowser_white.clear()
        self.textBrowser_white_intro.clear()
        self.pushButton_run_RGB.hide()
        self.pushButton_run_RIC.hide()
        self.pushButton_run_TKNP.hide()
        self.pushButton_run_TKNC.hide()
        self.pushButton_run_PSD.hide()
        self.pushButton_run_NC.hide()
        self.pushButton_run_NTE.hide()
        self.pushButton_run_NBC.hide()
        self.pushButton_run_ENI.hide()
        self.pushButton_run_KMNC.hide()
        self.pushButton_run_ALDp.hide()
        self.pushButton_run_ASS.hide()
        self.pushButton_run_ACTC.hide()
        self.pushButton_run_SNAC.hide()
        self.pushButton_run_BD.show()
        self.pushButton_run_ACAC.hide()
        self.textBrowser_white_intro.append(
            '最大边界距离。数据点之间到决策边界的距离衡量模型在最坏情况下的稳定性和鲁棒性。BD值越高，说明对抗样本鲁棒性越好，所以BD越大越好。')

    # input
    # 分类-正常工作模式
    def RG_input1(self):
        global datapath1
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath1 = filepath[0]

    def RG_input2(self):
        global datapath2
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath2 = filepath[0]

    # 分类-干扰工作模式
    def RR_input1(self):
        global RRpath
        RRpath = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    # 分类-测试用例生成
    def RD_input1(self):
        global RDpath1
        RDpath1 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def RD_input2(self):
        global RDpath2
        RDpath2 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def RDR1_input1(self):
        global RDR1path1
        RDR1path1 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def RDR1_input2(self):
        global RDR1path2
        RDR1path2 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def RDR2_input1(self):
        global RDR2path1
        RDR2path1 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def RDR2_input2(self):
        global RDR2path2
        RDR2path2 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def RDR3_input1(self):
        global RDR3path1
        RDR3path1 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def RDR3_input2(self):
        global RDR3path2
        RDR3path2 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    # 分类-特异性指标
    def GT_input1(self):
        global GTpath1
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        GTpath1 = filepath[0]

    # 决策-正常工作模式
    def JG_input1(self):
        global datapath3
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath3 = filepath[0]

    def JG_input2(self):
        global datapath4
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath4 = filepath[0]

    # 决策-干扰工作模式
    def JR_input1(self):
        global datapath5
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath5 = filepath[0]

    def JR_input2(self):
        global JRpath1
        JRpath1 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    # 决策-测试用例生成
    def JD_input1(self):
        global datapath6
        self.textBrowser_show_j.clear()
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath6 = filepath[0]

    def JD_input2(self):
        global JDpath1
        self.textBrowser_show_j.clear()
        JDpath1 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def JDR_input1(self):
        global JDRpath1
        self.textBrowser_show_j.clear()
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        JDRpath1 = filepath[0]

    def JDR_input2(self):
        global JDRpath2
        self.textBrowser_show_j.clear()
        # filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        # JDRpath2 = filepath[0]
        JDRpath2 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def JDR_input3(self):
        global JDRpath3
        self.textBrowser_show_j.clear()
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        JDRpath3 = filepath[0]

    # 决策2-正常工作模式
    def JG2_input1(self):
        global datapath31
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath31 = filepath[0]

    def JG2_input2(self):
        global datapath41
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath41 = filepath[0]

    def JG2_input3(self):
        global datapath51
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath51 = filepath[0]

    # 决策2-干扰工作模式
    def JR2_input1(self):
        global datapath511
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath511 = filepath[0]

    def JR2_input2(self):
        global JRpath11
        JRpath11 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def JR2_input3(self):
        global JRpath211
        JRpath211 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    # 决策2-测试用例生成
    def JD2_input1(self):
        global datapath6
        self.textBrowser_show_j.clear()
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath6 = filepath[0]

    def JD2_input2(self):
        global JDpath1
        self.textBrowser_show_j.clear()
        JDpath1 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    # 数据评估-图像质量评价
    def DATAEVA_input(self):
        global datapath_data
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath_data = filepath[0]

    # 数据评估-数据集筛选
    def DATASET_SD(self):
        global datapath_dataset1
        datapath_dataset1 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    def DATASET_TD(self):
        global datapath_dataset2
        datapath_dataset2 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    # 数据评估-数据集优化
    def DATASETADV_SD(self):
        global datapath_datasetadv1
        filepath = QFileDialog.getOpenFileName(None, "导入数据", ".")
        datapath_datasetadv1 = filepath[0]

    def DATASETADV_TD(self):
        global datapath_datasetadv2
        datapath_datasetadv2 = QFileDialog.getExistingDirectory(None, "请选择文件夹路径", ".")

    # run
    # 数据评估-图像质量评价
    def DATAEVA_run(self):
        global datapath_data
        self.timer.stop()
        self.textBrowser_BRE.clear()
        self.textBrowser_LAP.clear()
        self.textBrowser_SMD.clear()
        self.textBrowser_SMD2.clear()
        self.textBrowser_VAR.clear()
        self.textBrowser_ENE.clear()
        self.textBrowser_VOL.clear()
        self.textBrowser_ENT.clear()
        bre = evaluate.brenner(datapath_data)
        self.textBrowser_BRE.append(str(bre))
        self.cursot = self.textBrowser_BRE.textCursor()
        self.textBrowser_BRE.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        lap = evaluate.Laplacian(datapath_data)
        self.textBrowser_LAP.append(str(lap))
        self.cursot = self.textBrowser_LAP.textCursor()
        self.textBrowser_LAP.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        smd = evaluate.SMD(datapath_data)
        self.textBrowser_SMD.append(str(smd))
        self.cursot = self.textBrowser_SMD.textCursor()
        self.textBrowser_SMD.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        smd2 = evaluate.SMD2(datapath_data)
        self.textBrowser_SMD2.append(str(smd2))
        self.cursot = self.textBrowser_SMD2.textCursor()
        self.textBrowser_SMD2.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        var = evaluate.variance(datapath_data)
        self.textBrowser_VAR.append(str(var))
        self.cursot = self.textBrowser_VAR.textCursor()
        self.textBrowser_VAR.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        ene = evaluate.energy(datapath_data)
        self.textBrowser_ENE.append(str(ene))
        self.cursot = self.textBrowser_ENE.textCursor()
        self.textBrowser_ENE.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        vol = evaluate.Vollath(datapath_data)
        self.textBrowser_VOL.append(str(vol))
        self.cursot = self.textBrowser_VOL.textCursor()
        self.textBrowser_VOL.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        ent = evaluate.entropy(datapath_data)
        self.textBrowser_ENT.append(str(ent))
        self.cursot = self.textBrowser_ENT.textCursor()
        self.textBrowser_ENT.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    # 数据评估-数据集筛选
    def DATASET_run(self):
        global datapath_dataset1, datapath_dataset2
        self.timer.stop()
        self.textBrowser.clear()
        if self.lineEdit_BRE_filter.text():
            bre1 = int(self.lineEdit_BRE_filter.text())
        else:
            bre1 = 20427990
        if self.lineEdit_LAP_filter.text():
            lap1 = int(self.lineEdit_LAP_filter.text())
        else:
            lap1 = 759
        if self.lineEdit_SMD_filter.text():
            smd1 = int(self.lineEdit_SMD_filter.text())
        else:
            smd1 = 964230
        if self.lineEdit_SMD2_filter.text():
            smd21 = int(self.lineEdit_SMD2_filter.text())
        else:
            smd21 = 5706759
        if self.lineEdit_VAR_filter.text():
            var1 = int(self.lineEdit_VAR_filter.text())
        else:
            var1 = 58121230
        if self.lineEdit_ENE_filter.text():
            ene1 = int(self.lineEdit_ENE_filter.text())
        else:
            ene1 = 4
        if self.lineEdit_VOL_filter.text():
            vol1 = int(self.lineEdit_VOL_filter.text())
        else:
            vol1 = 50758917
        if self.lineEdit_ENT_filter.text():
            ent1 = int(self.lineEdit_ENT_filter.text())
        else:
            ent1 = 4
        evaluate.writetxt(bre1, lap1, smd1, smd21, var1, ene1, vol1, ent1, datapath_dataset1, datapath_dataset2)
        self.textBrowser.append('运行结束！')
        self.cursot = self.textBrowser.textCursor()
        self.textBrowser.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    # 数据评估-数据集优化
    def display_datasetadv(self):
        global image_path_d1, image_path_d2, image_path_d3, image_path_d4, image_path_d5, image_path_d6, image_path_d7, image_path_d8, image_path_d9, image_path_d10, image_path_d11, image_path_d12, image_path_d13, image_path_d14, image_path_d15, image_path_d16
        self.pil_image_d1 = QImage(image_path_d1)
        self.pil_image_d2 = QImage(image_path_d2)
        self.pil_image_d3 = QImage(image_path_d3)
        self.pil_image_d4 = QImage(image_path_d4)
        self.pil_image_d5 = QImage(image_path_d5)
        self.pil_image_d6 = QImage(image_path_d6)
        self.pil_image_d7 = QImage(image_path_d7)
        self.pil_image_d8 = QImage(image_path_d8)
        self.pil_image_d9 = QImage(image_path_d9)
        self.pil_image_d10 = QImage(image_path_d10)
        self.pil_image_d11 = QImage(image_path_d11)
        self.pil_image_d12 = QImage(image_path_d12)
        self.pil_image_d13 = QImage(image_path_d13)
        self.pil_image_d14 = QImage(image_path_d14)
        self.pil_image_d15 = QImage(image_path_d15)
        self.pil_image_d16 = QImage(image_path_d16)
        self.fcku_datasetadv(self.pil_image_d1)
        self.fcku2_datasetadv(self.pil_image_d2)
        self.fcku3_datasetadv(self.pil_image_d3)
        self.fcku4_datasetadv(self.pil_image_d4)
        self.fcku5_datasetadv(self.pil_image_d5)
        self.fcku6_datasetadv(self.pil_image_d6)
        self.fcku7_datasetadv(self.pil_image_d7)
        self.fcku8_datasetadv(self.pil_image_d8)
        self.fcku9_datasetadv(self.pil_image_d9)
        self.fcku10_datasetadv(self.pil_image_d10)
        self.fcku11_datasetadv(self.pil_image_d11)
        self.fcku12_datasetadv(self.pil_image_d12)
        self.fcku13_datasetadv(self.pil_image_d13)
        self.fcku14_datasetadv(self.pil_image_d14)
        self.fcku15_datasetadv(self.pil_image_d15)
        self.fcku16_datasetadv(self.pil_image_d16)
        self.timer.timeout.connect(lambda: self.fcku_datasetadv(self.pil_image_d1))
        self.timer.timeout.connect(lambda: self.fcku2_datasetadv(self.pil_image_d2))
        self.timer.timeout.connect(lambda: self.fcku3_datasetadv(self.pil_image_d3))
        self.timer.timeout.connect(lambda: self.fcku4_datasetadv(self.pil_image_d4))
        self.timer.timeout.connect(lambda: self.fcku5_datasetadv(self.pil_image_d5))
        self.timer.timeout.connect(lambda: self.fcku6_datasetadv(self.pil_image_d6))
        self.timer.timeout.connect(lambda: self.fcku7_datasetadv(self.pil_image_d7))
        self.timer.timeout.connect(lambda: self.fcku8_datasetadv(self.pil_image_d8))
        self.timer.timeout.connect(lambda: self.fcku9_datasetadv(self.pil_image_d9))
        self.timer.timeout.connect(lambda: self.fcku10_datasetadv(self.pil_image_d10))
        self.timer.timeout.connect(lambda: self.fcku11_datasetadv(self.pil_image_d11))
        self.timer.timeout.connect(lambda: self.fcku12_datasetadv(self.pil_image_d12))
        self.timer.timeout.connect(lambda: self.fcku13_datasetadv(self.pil_image_d13))
        self.timer.timeout.connect(lambda: self.fcku14_datasetadv(self.pil_image_d14))
        self.timer.timeout.connect(lambda: self.fcku15_datasetadv(self.pil_image_d15))
        self.timer.timeout.connect(lambda: self.fcku16_datasetadv(self.pil_image_d16))
        self.timer.start(10)

    def fcku_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_FSBH_S.width(), self.label_FSBH_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_FSBH_S.setPixmap(pixmap)

    def fcku2_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_CJ_S.width(), self.label_CJ_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_CJ_S.setPixmap(pixmap)

    def fcku3_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_YSKJ_S.width(), self.label_YSKJ_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_YSKJ_S.setPixmap(pixmap)

    def fcku4_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_SIG_S.width(), self.label_SIG_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_SIG_S.setPixmap(pixmap)

    def fcku5_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_FZ_S.width(), self.label_FZ_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_FZ_S.setPixmap(pixmap)

    def fcku6_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_HDT_S.width(), self.label_HDT_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_HDT_S.setPixmap(pixmap)

    def fcku7_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_GAMMA_S.width(), self.label_GAMMA_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_GAMMA_S.setPixmap(pixmap)

    def fcku8_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_XXDBD_S.width(), self.label_XXDBD_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_XXDBD_S.setPixmap(pixmap)

    def fcku9_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_GSZY_S.width(), self.label_GSZY_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_GSZY_S.setPixmap(pixmap)

    def fcku10_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_GSMH_S.width(), self.label_GSMH_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_GSMH_S.setPixmap(pixmap)

    def fcku11_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_PJMH_2.width(), self.label_PJMH_2.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_PJMH_2.setPixmap(pixmap)

    def fcku12_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_ZZMH_S.width(), self.label_ZZMH_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_ZZMH_S.setPixmap(pixmap)

    def fcku13_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_YDMH_S.width(), self.label_YDMH_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_YDMH_S.setPixmap(pixmap)

    def fcku14_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_SBMH_S.width(), self.label_SBMH_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_SBMH_S.setPixmap(pixmap)

    def fcku15_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_SCKJ_S.width(), self.label_SCKJ_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_SCKJ_S.setPixmap(pixmap)

    def fcku16_datasetadv(self, fckimage):
        pil_image = self.m_resize(self.label_SJYS_S.width(), self.label_SJYS_S.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_SJYS_S.setPixmap(pixmap)

    def m_resize(self, w_box, h_box, pil_image):
        w, h = pil_image.width(), pil_image.height()
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.scaled(width, height)

    def DATASETADV_run(self):
        global datapath_datasetadv1, datapath_datasetadv2, image_path_d1, image_path_d2, image_path_d3, image_path_d4, image_path_d5, image_path_d6, image_path_d7, image_path_d8, image_path_d9, image_path_d10, image_path_d11, image_path_d12, image_path_d13, image_path_d14, image_path_d15, image_path_d16
        x = unbalance.unblance(datapath_datasetadv1, datapath_datasetadv2)
        image_path_d1 = 'FSBH.jpg'
        image_path_d2 = 'CJ.jpg'
        image_path_d3='GBYSKJ.jpg'
        image_path_d4 = 'Sigmoid.jpg'
        image_path_d5 = 'FZ.jpg'
        image_path_d6 = 'HDT.jpg'
        image_path_d7 = 'Gamma.jpg'
        image_path_d8 = 'XXDBD.jpg'
        image_path_d9 = 'GSZY.jpg'
        image_path_d10 = 'GSMH.jpg'
        image_path_d11 = 'PJMH.jpg'
        image_path_d12 = 'ZZMH.jpg'
        image_path_d13 = 'YDMH.jpg'
        image_path_d14 = 'SBMH.jpg'
        image_path_d15 = 'SCKJ.jpg'
        image_path_d16 = 'SJSDBHD.jpg'
        self.display_datasetadv()

    # 分类-正常工作模式
    def display(self):
        global image_path1, image_path2
        self.pil_image1 = QImage(image_path1)
        self.pil_image2 = QImage(image_path2)
        self.fcku(self.pil_image1)
        self.fcku2(self.pil_image2)
        self.timer.timeout.connect(lambda: self.fcku(self.pil_image1))
        self.timer.timeout.connect(lambda: self.fcku2(self.pil_image2))
        self.timer.start(10)

    def fcku(self, fckimage):
        pil_image = self.m_resize(self.label_C_2.width(), self.label_C_2.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_C_2.setPixmap(pixmap)

    def fcku2(self, fckimage):
        pil_image = self.m_resize(self.label_ROC.width(), self.label_ROC.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_ROC.setPixmap(pixmap)

    def m_resize(self, w_box, h_box, pil_image):
        w, h = pil_image.width(), pil_image.height()
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.scaled(width, height)

    def RG_run(self):
        global datapath1, datapath2, image_path1, image_path2
        # global image_path1, image_path2
        # datapath1 = 'D:\\data\\recognition\\result\\gener\\y_pred.txt'
        # datapath2 = 'D:\\data\\recognition\\result\\gener\\y_true.txt'
        self.timer.stop()
        self.textBrowser_A.clear()
        self.textBrowser_P.clear()
        self.textBrowser_R.clear()
        self.textBrowser_F1.clear()
        self.textBrowser_AUC.clear()
        self.textBrowser_K.clear()
        self.textBrowser_H.clear()
        self.textBrowser_8.clear()
        self.textBrowser_jielun.clear()
        self.label_ROC.clear()
        self.label_C_2.clear()
        if self.lineEdit_gener_A.text():
            label = int(self.lineEdit_gener_A.text())
        else:
            label = 20
        y_pred, y_true, label = load_data(datapath1, datapath2, label)
        x1 = Generalization().Accuracy(y_pred, y_true)
        self.textBrowser_A.append(str(x1))
        self.cursot = self.textBrowser_A.textCursor()
        self.textBrowser_A.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        pre1, pre2, pre3 = Generalization().Precision(y_pred, y_true)
        self.textBrowser_P.append(str(pre1))
        # self.textBrowser_P.append('macro:' + str(pre1))
        # self.textBrowser_P.append('micro' + str(pre2))
        # self.textBrowser_P.append('weighted' + str(pre3))
        self.cursot = self.textBrowser_P.textCursor()
        self.textBrowser_P.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        re1, re2, re3 = Generalization().Recall(y_pred, y_true)
        self.textBrowser_R.append(str(re1))
        # self.textBrowser_R.append('macro:' + str(re1))
        # self.textBrowser_R.append('micro' + str(re2))
        # self.textBrowser_R.append('weighted' + str(re3))
        self.cursot = self.textBrowser_R.textCursor()
        self.textBrowser_R.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        F1, F2, F3 = Generalization().Recall(y_pred, y_true)
        self.textBrowser_F1.append(str(F1))
        # self.textBrowser_F1.append('macro:' + str(F1))
        # self.textBrowser_F1.append('micro' + str(F2))
        # self.textBrowser_F1.append('weighted' + str(F3))
        self.cursot = self.textBrowser_F1.textCursor()
        self.textBrowser_F1.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        auc = Generalization().AUC(y_pred, y_true, label)
        self.textBrowser_AUC.append(str(auc))
        self.cursot = self.textBrowser_AUC.textCursor()
        self.textBrowser_AUC.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        kappa = Generalization().kappa(y_pred, y_true)
        self.textBrowser_K.append(str(kappa))
        self.cursot = self.textBrowser_K.textCursor()
        self.textBrowser_K.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        h = Generalization().haimingdistance(y_pred, y_true)
        self.textBrowser_H.append(str(h))
        self.cursot = self.textBrowser_H.textCursor()
        self.textBrowser_H.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        j = Generalization().jiekade(y_pred, y_true)
        self.textBrowser_8.append(str(j))
        self.cursot = self.textBrowser_8.textCursor()
        self.textBrowser_8.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        if x1 > 0.9 and re1 > 0.9 and F1 > 0.9 and kappa > 0.9:
            self.textBrowser_jielun.append("因为准确率、召回率、F1值、kappa系数都高于0.9，所以算法具有良好的泛化能力，建议直接使用。")
        elif x1 > 0.85 or re1 > 0.85 or F1 > 0.85 or kappa > 0.85:
            self.textBrowser_jielun.append(
                "因为准确率、召回率、F1值、kappa系数有一个以上高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优。")
        elif x1 > 0.7 or re1 > 0.7 or F1 > 0.7 or kappa > 0.7:
            self.textBrowser_jielun.append(
                "因为准确率、召回率、F1值、kappa系数有一个以上高于0.7，所以算法具有一定的泛化能力，但需要优化调整，建议按照混淆矩阵错误分类分布情况调整算法对于错分类的适应性。")
        else:
            self.textBrowser_jielun.append("因为准确率、召回率、F1值、kappa系数没有一个高于0.7，所以算法不适合于本任务，建议更换其他算法。")
        self.cursot = self.textBrowser_jielun.textCursor()
        self.textBrowser_jielun.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        x = Generalization().Confusionmatrix(y_pred, y_true, label)
        y = Generalization().ROC(y_pred, y_true)
        image_path1 = 'Confusionmatrix.jpg'
        image_path2 = 'ROC.jpg'
        self.display()

    # 分类-干扰工作模式
    def display_RR(self):
        global image_path3, image_path4, image_path5
        self.pil_image3 = QImage(image_path3)
        self.pil_image4 = QImage(image_path4)
        self.pil_image5 = QImage(image_path5)
        self.fcku_RR(self.pil_image3)
        self.fcku2_RR(self.pil_image4)
        self.fcku3_RR(self.pil_image5)
        self.timer.timeout.connect(lambda: self.fcku_RR(self.pil_image3))
        self.timer.timeout.connect(lambda: self.fcku2_RR(self.pil_image4))
        self.timer.timeout.connect(lambda: self.fcku3_RR(self.pil_image5))
        self.timer.start(10)

    def fcku_RR(self, fckimage):
        pil_image = self.m_resize_RR(self.label_A_show_r.width(), self.label_A_show_r.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_A_show_r.setPixmap(pixmap)

    def fcku2_RR(self, fckimage):
        pil_image = self.m_resize_RR(self.label_P_show_r.width(), self.label_P_show_r.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_P_show_r.setPixmap(pixmap)

    def fcku3_RR(self, fckimage):
        pil_image = self.m_resize_RR(self.label_R_show_r.width(), self.label_R_show_r.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_R_show_r.setPixmap(pixmap)

    def m_resize_RR(self, w_box, h_box, pil_image):
        w, h = pil_image.width(), pil_image.height()
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.scaled(width, height)

    def RR_run(self):
        global RRpath, image_path3, image_path4, image_path5
        # global image_path3, image_path4, image_path5
        # RRpath = 'D:\\data\\recognition\\result\\noise'
        self.timer.stop()
        self.textBrowser_A_r.clear()
        self.textBrowser_P_r.clear()
        self.textBrowser_R_r.clear()
        self.textBrowser_jielun_r.clear()
        self.label_R_show_r.clear()
        self.label_P_show_r.clear()
        self.label_A_show_r.clear()
        if self.lineEdit_threthold.text():
            threthold = float(self.lineEdit_threthold.text())
        else:
            threthold = 0.9
        if self.lineEdit_lapse.text():
            lapse = float(self.lineEdit_lapse.text())
        else:
            lapse = 0.6
        y_list1 = robustness.run_A(RRpath, threthold, lapse)
        self.textBrowser_A_r.append(str(y_list1))
        self.cursot = self.textBrowser_A_r.textCursor()
        self.textBrowser_A_r.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        y_list2 = robustness.run_P(RRpath, threthold, lapse)
        self.textBrowser_P_r.append(str(y_list2))
        self.cursot = self.textBrowser_P_r.textCursor()
        self.textBrowser_P_r.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        y_list3 = robustness.run_R(RRpath, threthold, lapse)
        self.textBrowser_R_r.append(str(y_list3))
        self.cursot = self.textBrowser_R_r.textCursor()
        self.textBrowser_R_r.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        if y_list1[19] > y_list1[0] * threthold and y_list2[19] > y_list2[0] * threthold and y_list3[19] > y_list3[
            0] * threthold:
            self.textBrowser_jielun_r.append("因为准确率、精确率、召回率加0.2噪声时也不低于可用阈值，所以算法具有良好的鲁棒能力，建议直接使用。")
        elif y_list1[14] > y_list1[0] * threthold and y_list1[19] > y_list1[0] * lapse or y_list2[14] > y_list2[
            0] * threthold and y_list2[19] > y_list2[0] * lapse or y_list3[14] > y_list3[0] * threthold and y_list3[
            19] > y_list3[0] * lapse:
            self.textBrowser_jielun_r.append(
                "因为准确率、精确率、召回率中有一个以上加0.15噪声时也不低于可用阈值，同时加0.2噪声时也不低于失效阈值，所以算法具有较好的鲁棒能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优。")
        elif y_list1[9] > y_list1[0] * threthold or y_list1[19] > y_list1[0] * lapse or y_list2[9] > y_list2[
            0] * threthold or y_list2[19] > y_list2[0] * lapse or y_list3[9] > y_list3[0] * threthold or y_list3[19] > \
                y_list3[0] * lapse:
            self.textBrowser_jielun_r.append(
                "因为准确率、精确率、召回率中有一个以上加0.05噪声时也不低于可用阈值或者准确率、精确率、召回率中有一个以上加0.2噪声时也不低于失效阈值，所以算法具有一定的鲁棒能力，但需要优化调整，建议从算法上提升性能，可以将通道分成多组，每组单独进行卷积，然后再将通道合成可以减少模型的参数，提高模型准确率。")
        else:
            self.textBrowser_jielun_r.append(
                "因为准确率、精确率、召回率都加0.05噪声时高于可用阈值，同时准确率、精确率、召回率加0.2噪声时也都高于失效阈值，所以算法鲁棒能力较差，不适合于本任务，建议更换其他算法。")
        self.cursot = self.textBrowser_jielun_r.textCursor()
        self.textBrowser_jielun_r.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        image_path3 = 'Accuracy.jpg'
        image_path4 = 'Precision.jpg'
        image_path5 = 'Recall.jpg'
        self.display_RR()

    # 分类-测试用例生成
    def RD_run(self):
        global RDpath1, RDpath2
        # RDpath1 = 'D:\\data\\recognition\\data\\NWPU-RESISC45'
        # RDpath2 = 'D:\\data\\recognition\\data\\generalization'
        self.timer.stop()
        self.textBrowser_show_data_gener.clear()
        shutil.rmtree(RDpath2)
        if self.lineEdit_num_gener.text():
            num = self.lineEdit_num_gener.text().split(',')
        else:
            num = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        numl = []
        for i in range(len(num)):
            numl.append(float(num[i]))
        # print(numl)
        x = chouqu.moveFile(RDpath1, RDpath2, numl)
        self.textBrowser_show_data_gener.append('运行结束！')
        self.cursot = self.textBrowser_show_data_gener.textCursor()
        self.textBrowser_show_data_gener.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def RDR1_run(self):
        global RDR1path1, RDR1path2
        # RDR1path1 = 'D:\\data\\recognition\\data\\generalization'
        # RDR1path2 = 'D:\\data\\recognition\\data\\robust'
        self.timer.stop()
        self.textBrowser_show_data_gener.clear()
        shutil.rmtree(RDR1path2)
        # shutil.rmtree('D:\\data\\recognition\\data\\robust')
        if self.lineEdit_num_gener_N.text():
            noise_num = self.lineEdit_num_gener_N.text().split(',')
        else:
            noise_num = [0.01, 0.01, 20]
        numl = []
        for i in range(len(noise_num)):
            numl.append(float(noise_num[i]))
        qishi, buchang, zu = numl[0], numl[1], int(numl[2])
        # x = robust.doFile(RDR1path1, RDR1path2, noise_num)
        x = robust1_exp.main(RDR1path1, RDR1path2, qishi, buchang, zu)
        self.textBrowser_show_data_gener.append('运行结束！')
        self.cursot = self.textBrowser_show_data_gener.textCursor()
        self.textBrowser_show_data_gener.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def RDR2_run(self):
        global RDR2path1, RDR2path2
        # RDR2path1 = 'D:\\data\\recognition\\data\\generalization'
        # RDR2path2 = 'D:\\data\\recognition\\data\\robust'
        self.timer.stop()
        self.textBrowser_show_data_gener.clear()
        shutil.rmtree(RDR2path2)
        # shutil.rmtree('D:\\data\\recognition\\data\\robust')
        if self.lineEdit_num_gener_Z.text():
            mianji = self.lineEdit_num_gener_Z.text().split(',')
        else:
            mianji = [0.01, 0.01, 20]
        numl = []
        for i in range(len(mianji)):
            numl.append(float(mianji[i]))
        qishi, buchang, zu = numl[0], numl[1], int(numl[2])
        # x = robust2.doFile(RDR2path1, RDR2path2, mianji)
        x = robust2_exp.main(RDR2path1, RDR2path2, qishi, buchang, zu)
        self.textBrowser_show_data_gener.append('运行结束！')
        self.cursot = self.textBrowser_show_data_gener.textCursor()
        self.textBrowser_show_data_gener.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def RDR3_run(self):
        global RDR3path1, RDR3path2
        # RDR3path1 = 'D:\\data\\recognition\\data\\generalization'
        # RDR3path2 = 'D:\\data\\recognition\\data\\robust'
        self.timer.stop()
        self.textBrowser_show_data_gener.clear()
        shutil.rmtree(RDR3path2)
        # shutil.rmtree('D:\\data\\recognition\\data\\robust')
        if self.lineEdit_num_gener_G.text():
            var = self.lineEdit_num_gener_G.text().split(',')
        else:
            var = [0.01, 0.01, 20]
        numl = []
        for i in range(len(var)):
            numl.append(float(var[i]))
        qishi, buchang, zu = numl[0], numl[1], int(numl[2])
        # x = robust3.doFile(RDR3path1, RDR3path2, var)
        x = robust3_exp.main(RDR3path1, RDR3path2, qishi, buchang, zu)
        self.textBrowser_show_data_gener.append('运行结束！')
        self.cursot = self.textBrowser_show_data_gener.textCursor()
        self.textBrowser_show_data_gener.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    # 分类-特异性指标
    def ACAC_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\ACAC.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def ACTC_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\ACTC.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def ASS_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\ASS.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def BD_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\BD.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def SNAC_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\SNAC.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def ALDp_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\ALDp.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def KMNC_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\KMNC.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def ENI_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\ENI.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def NBC_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\NBC.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def NTE_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\NTE.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def NC_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\NC.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def PSD_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\PSD.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def TKNC_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\TKNC.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def TKNP_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\TKNP.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def RIC_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\RIC.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def RGB_run(self):
        global GTpath1
        # GTpath1 = 'D:\\data\\recognition\\AISAFETY\\result\\RGB.txt'
        self.timer.stop()
        self.textBrowser_white.clear()
        # shutil.rmtree('D:\\data\\recognition\\AISAFETY')
        x = readtxt.readtxt(GTpath1)
        self.textBrowser_white.append(x)
        self.cursot = self.textBrowser_white.textCursor()
        self.textBrowser_white.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    # run
    # 决策-正常工作模式
    def display_GJ(self):
        global image_path6
        self.pil_image6 = QImage(image_path6)
        self.fcku_GJ(self.pil_image6)
        self.timer.timeout.connect(lambda: self.fcku_GJ(self.pil_image6))
        self.timer.start(10)

    def fcku_GJ(self, fckimage):
        pil_image = self.m_resize_GJ(self.label_ROC_j.width(), self.label_ROC_j.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_ROC_j.setPixmap(pixmap)

    def m_resize_GJ(self, w_box, h_box, pil_image):
        w, h = pil_image.width(), pil_image.height()
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.scaled(width, height)

    def JG_run(self):
        global datapath3, datapath4, image_path6
        # global image_path6
        # datapath3='D:\\data\\juece\\gener\\result.json'
        # datapath4='D:\\data\\juece\\gener\\result_change.json'
        # datapath3 = 'D:\\data\\juece\\gener\\gener\\output_U1QGX4HJSXGZ_00000000.json'
        # datapath4 = 'D:\\data\\juece\\gener\\gener\\output_U1QGX4HJSXGZ_00000000_change.json'
        self.timer.stop()
        self.textBrowser_A_j.clear()
        self.textBrowser_P_j.clear()
        self.textBrowser_R_j.clear()
        self.textBrowser_F1_j.clear()
        self.textBrowser_K_j.clear()
        self.textBrowser_H_j.clear()
        self.textBrowser_J_j.clear()
        self.textBrowser_jielun_j.clear()
        self.label_ROC.clear()
        y_pred, y_true = generalization_j.load_data(datapath3, datapath4)
        x1 = generalization_j.Generalization().Accuracy(y_pred, y_true)
        self.textBrowser_A_j.append(str(x1))
        self.cursot = self.textBrowser_A_j.textCursor()
        self.textBrowser_A_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        pre1, pre2, pre3 = generalization_j.Generalization().Precision(y_pred, y_true)
        self.textBrowser_P_j.append(str(pre1))
        # self.textBrowser_P_j.append('macro:' + str(pre1))
        # self.textBrowser_P_j.append('micro' + str(pre2))
        # self.textBrowser_P_j.append('weighted' + str(pre3))
        self.cursot = self.textBrowser_P_j.textCursor()
        self.textBrowser_P_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        re1, re2, re3 = generalization_j.Generalization().Recall(y_pred, y_true)
        self.textBrowser_R_j.append(str(re1))
        # self.textBrowser_R_j.append('macro:' + str(re1))
        # self.textBrowser_R_j.append('micro' + str(re2))
        # self.textBrowser_R_j.append('weighted' + str(re3))
        self.cursot = self.textBrowser_R_j.textCursor()
        self.textBrowser_R_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        F1, F2, F3 = generalization_j.Generalization().Recall(y_pred, y_true)
        self.textBrowser_F1_j.append(str(F1))
        # self.textBrowser_F1_j.append('macro:' + str(F1))
        # self.textBrowser_F1_j.append('micro' + str(F2))
        # self.textBrowser_F1_j.append('weighted' + str(F3))
        self.cursot = self.textBrowser_F1_j.textCursor()
        self.textBrowser_F1_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        kappa = generalization_j.Generalization().kappa(y_pred, y_true)
        self.textBrowser_K_j.append(str(kappa))
        self.cursot = self.textBrowser_K_j.textCursor()
        self.textBrowser_K_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        h = generalization_j.Generalization().haimingdistance(y_pred, y_true)
        self.textBrowser_H_j.append(str(h))
        self.cursot = self.textBrowser_H_j.textCursor()
        self.textBrowser_H_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        j = generalization_j.Generalization().jiekade(y_pred, y_true)
        self.textBrowser_J_j.append(str(j))
        self.cursot = self.textBrowser_J_j.textCursor()
        self.textBrowser_J_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        y = Generalization().ROC(y_pred, y_true)
        if x1 > 0.9 and re1 > 0.9 and F1 > 0.9 and kappa > 0.9:
            self.textBrowser_jielun_j.append("因为准确率、召回率、F1值、kappa系数都高于0.9，所以算法具有良好的泛化能力，建议直接使用。")
        elif x1 > 0.85 and re1 > 0.85 and F1 > 0.85 and kappa > 0.85:
            self.textBrowser_jielun_j.append(
                "因为准确率、召回率、F1值、kappa系数都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优。")
        elif x1 > 0.85 and re1 > 0.85 and F1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为准确率、召回率、F1值都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的一致性。")
        elif kappa > 0.85 and re1 > 0.85 and F1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为召回率、F1值、kappa系数都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的分类精度。")
        elif x1 > 0.85 and kappa > 0.85 and F1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为准确率、F1值、kappa系数都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的覆盖性。")
        elif x1 > 0.85 and kappa > 0.85 and re1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为准确率、召回率、kappa系数都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法不均衡数据的适应性。")
        elif F1 > 0.85 and kappa > 0.85:
            self.textBrowser_jielun_j.append(
                "因为F1值、kappa系数都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的分类精度和覆盖性。")
        elif re1 > 0.85 and kappa > 0.85:
            self.textBrowser_jielun_j.append(
                "因为召回率、kappa系数都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的分类精度和不均衡数据的适应性。")
        elif re1 > 0.85 and F1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为召回率、F1值都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的分类精度和一致性。")
        elif x1 > 0.85 and re1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为准确率、召回率都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法不均衡数据的适应性和一致性。")
        elif x1 > 0.85 and F1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为准确率、F1值都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的覆盖性和一致性。")
        elif x1 > 0.85 and kappa > 0.85:
            self.textBrowser_jielun_j.append(
                "因为准确率、kappa系数都高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的覆盖性和不均衡数据的适应性。")
        elif x1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为准确率高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的覆盖性、不均衡数据的适应性和一致性。")
        elif re1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为召回率高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的分类精度、覆盖性和一致性。")
        elif F1 > 0.85:
            self.textBrowser_jielun_j.append(
                "因为F1值高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的分类精度、不均衡数据的适应性和一致性。")
        elif kappa > 0.85:
            self.textBrowser_jielun_j.append(
                "因为kappa系数高于0.85，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优，来提升算法的分类精度、覆盖性和不均衡数据的适应性。")
        elif x1 > 0.7 or re1 > 0.7 or F1 > 0.7 or kappa > 0.7:
            self.textBrowser_jielun_j.append(
                "因为准确率、召回率、F1值、kappa系数有一个以上高于0.7，所以算法具有一定的泛化能力，但需要优化调整，建议参考ROC曲线考虑敏感性和特异性的相互关系，来提升分类精度、覆盖性、不均衡数据的适应性、一致性。")
        else:
            self.textBrowser_jielun_j.append("因为准确率、召回率、F1值、kappa系数没有一个高于0.7，所以算法不适合于本任务，建议更换其他算法。")
        self.cursot = self.textBrowser_jielun_j.textCursor()
        self.textBrowser_jielun_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        image_path6 = 'ROC_j.jpg'
        self.display_GJ()

    # 决策-干扰工作模式
    def display_JR(self):
        global image_path7, image_path8, image_path9
        self.pil_image7 = QImage(image_path7)
        self.pil_image8 = QImage(image_path8)
        self.pil_image9 = QImage(image_path9)
        self.fcku_JR(self.pil_image7)
        self.fcku2_JR(self.pil_image8)
        self.fcku3_JR(self.pil_image9)
        self.timer.timeout.connect(lambda: self.fcku_JR(self.pil_image7))
        self.timer.timeout.connect(lambda: self.fcku2_JR(self.pil_image8))
        self.timer.timeout.connect(lambda: self.fcku3_JR(self.pil_image9))
        self.timer.start(10)

    def fcku_JR(self, fckimage):
        pil_image = self.m_resize_JR(self.label_A_show_r_j.width(), self.label_A_show_r_j.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_A_show_r_j.setPixmap(pixmap)

    def fcku2_JR(self, fckimage):
        pil_image = self.m_resize_JR(self.label_P_show_r_j.width(), self.label_P_show_r_j.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_P_show_r_j.setPixmap(pixmap)

    def fcku3_JR(self, fckimage):
        pil_image = self.m_resize_JR(self.label_R_show_r_j.width(), self.label_R_show_r_j.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_R_show_r_j.setPixmap(pixmap)

    def m_resize_JR(self, w_box, h_box, pil_image):
        w, h = pil_image.width(), pil_image.height()
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.scaled(width, height)

    def JR_run(self):
        global datapath5, JRpath1, image_path7, image_path8, image_path9
        # global image_path7, image_path8, image_path9
        # datapath5 = 'D:\\data\\juece\\robust\\robust\\result.json'
        # JRpath1 = 'D:\\data\\juece\\robust\\robust\\robust'
        self.timer.stop()
        self.textBrowser_A_r_2_j.clear()
        self.textBrowser_P_r_j.clear()
        self.textBrowser_R_r_j.clear()
        self.textBrowser_jielun_r_j.clear()
        self.label_R_show_r_j.clear()
        self.label_P_show_r_j.clear()
        self.label_A_show_r_j.clear()
        if self.lineEdit_threthold_j.text():
            threthold = float(self.lineEdit_threthold_j.text())
        else:
            threthold = 0.9
        if self.lineEdit_lapse_j.text():
            lapse = float(self.lineEdit_lapse_j.text())
        else:
            lapse = 0.6
        y_list1 = robustness_j.run_A(JRpath1, datapath5, threthold, lapse)
        self.textBrowser_A_r_2_j.append(str(y_list1))
        self.cursot = self.textBrowser_A_r_2_j.textCursor()
        self.textBrowser_A_r_2_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        y_list2 = robustness_j.run_P(JRpath1, datapath5, threthold, lapse)
        self.textBrowser_P_r_j.append(str(y_list2))
        self.cursot = self.textBrowser_P_r_j.textCursor()
        self.textBrowser_P_r_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        y_list3 = robustness_j.run_R(JRpath1, datapath5, threthold, lapse)
        self.textBrowser_R_r_j.append(str(y_list3))
        self.cursot = self.textBrowser_R_r_j.textCursor()
        self.textBrowser_R_r_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        if y_list1[19] > y_list1[0] * threthold and y_list2[19] > y_list2[0] * threthold and y_list3[19] > y_list3[
            0] * threthold:
            self.textBrowser_jielun_r_j.append("因为准确率、精确率、召回率加0.2噪声时也不低于可用阈值，所以算法具有良好的鲁棒能力，建议直接使用。")
        elif y_list1[14] > y_list1[0] * threthold and y_list1[19] > y_list1[0] * lapse or y_list2[14] > y_list2[
            0] * threthold and y_list2[19] > y_list2[0] * lapse or y_list3[14] > y_list3[0] * threthold and y_list3[
            19] > y_list3[0] * lapse:
            self.textBrowser_jielun_r_j.append(
                "因为准确率、精确率、召回率中有一个以上加0.15噪声时也不低于可用阈值，同时加0.2噪声时也不低于失效阈值，所以算法具有较好的鲁棒能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优。")
        elif y_list1[9] > y_list1[0] * threthold or y_list1[19] > y_list1[0] * lapse or y_list2[9] > y_list2[
            0] * threthold or y_list2[19] > y_list2[0] * lapse or y_list3[9] > y_list3[0] * threthold or y_list3[19] > \
                y_list3[0] * lapse:
            self.textBrowser_jielun_r_j.append(
                "因为准确率、精确率、召回率中有一个以上加0.05噪声时也不低于可用阈值或者准确率、精确率、召回率中有一个以上加0.2噪声时也不低于失效阈值，所以算法具有一定的鲁棒能力，但需要优化调整，建议从算法上提升性能，可以将通道分成多组，每组单独进行卷积，然后再将通道合成可以减少模型的参数，提高模型准确率。")
        else:
            self.textBrowser_jielun_r_j.append(
                "因为准确率、精确率、召回率都加0.05噪声时高于可用阈值，同时准确率、精确率、召回率加0.2噪声时也都高于失效阈值，所以算法鲁棒能力较差，不适合于本任务，建议更换其他算法。")
        self.cursot = self.textBrowser_jielun_r_j.textCursor()
        self.textBrowser_jielun_r_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()
        image_path7 = 'Accuracy_j.jpg'
        image_path8 = 'Precision_j.jpg'
        image_path9 = 'Recall_j.jpg'
        self.display_JR()

    # 决策-测试用例生成
    def JD_run(self):
        global datapath6, JDpath1
        # datapath6 = 'D:\\data\\juece\\data\\input-format.json'
        # JDpath1='D:\\data\\juece\\data\\output'
        # JDpath1 = 'D:\\Shared-Input'
        self.timer.stop()
        self.textBrowser_show_j.clear()
        # shutil.rmtree(JDpath1)
        x = Test_case_generation_gai.randomnum(datapath6, JDpath1)
        # x=Test_case_generation.jsonfile(datapath6, JDpath1, input_fields)
        self.textBrowser_show_j.append('运行结束！')
        self.cursot = self.textBrowser_show_j.textCursor()
        self.textBrowser_show_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    def JDR_run(self):
        global JDRpath1, JDRpath2, JDRpath3
        # JDRpath1 = 'E:\\kexinxing\\zhongqi\\jiemian4\\data\\juece\\data\\output_U1QGX4HJSXGZ_00000000.json'
        # JDRpath2 = 'E:\\kexinxing\\zhongqi\\jiemian4\\data\\juece\\data\\output_U1QGX4HJSXGZ_00000000_change.json'
        # JDRpath3 = 'E:\\kexinxing\\zhongqi\\jiemian4\\data\\juece\\data\\output_U1QGX4HJSXGZ_00000000_choice.json'
        # JDRpath1 = 'D:\\Shared-Solution\\output_output-format.json'
        # JDRpath2 = 'D:\\data\\juece\\data\\output_U1QGX4HJSXGZ_00000000_change.json'
        # JDRpath3 = 'D:\\data\\juece\\data\\output_U1QGX4HJSXGZ_00000000_choice.json'
        self.timer.stop()
        self.textBrowser_show_j.clear()
        # shutil.rmtree('D:\\data\\juece\\robust\\robust')
        shutil.rmtree(JDRpath2)
        if self.lineEdit_noise_j.text():
            noise_num = self.lineEdit_noise_j.text().split(',')
        else:
            noise_num = [0.01, 0.01, 20]
        if self.lineEdit_num_j.text():
            num = self.lineEdit_num_j.text().split(',')
        else:
            num = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17,
                   0.18, 0.19, 0.20]
        numl = []
        for i in range(len(noise_num)):
            numl.append(float(noise_num[i]))
        qishi, buchang, zu = numl[0], numl[1], int(numl[2])
        numl1 = []
        for i in range(len(num)):
            numl1.append(float(num[i]))
        # x = noise.change(JDRpath1, JDRpath2, JDRpath3, noise_num)
        x = noise_true.main(JDRpath1, JDRpath2, qishi, buchang, zu, numl1)
        self.textBrowser_show_j.append('运行结束！')
        self.cursot = self.textBrowser_show_j.textCursor()
        self.textBrowser_show_j.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    # 决策2-泛化性
    def JG2_run(self):
        global datapath31, datapath41, datapath51
        self.timer.stop()
        self.textBrowser_JFGWC.clear()
        self.textBrowser_PJJJWC.clear()
        self.textBrowser_PJJDBFBWC.clear()
        self.textBrowser_PCL.clear()
        self.textBrowser_FCL.clear()
        self.textBrowser_XEBDXS.clear()
        self.textBrowser_JSFCFS.clear()
        self.textBrowser_XFCL.clear()
        self.textBrowser_MSLE.clear()
        self.textBrowser_jielun_j2.clear()
        if datapath31 and datapath41 and datapath51:
            M, N, N1 = gener_net2.load_data(datapath31, datapath51, datapath41)
            result1, result11, x1, x11 = gener_net2.JFWC(M, N, N1)
            self.textBrowser_JFGWC.append('model1:' + str(x1))
            self.textBrowser_JFGWC.append('model2:' + str(x11))
            self.cursot = self.textBrowser_JFGWC.textCursor()
            self.textBrowser_JFGWC.moveCursor(self.cursot.End)
            result2, result21, x2, x21 = gener_net2.PJJDWC(M, N, N1)
            self.textBrowser_PJJJWC.append('model1:' + str(x2))
            self.textBrowser_PJJJWC.append('model2:' + str(x21))
            self.cursot = self.textBrowser_PJJJWC.textCursor()
            self.textBrowser_PJJJWC.moveCursor(self.cursot.End)
            result3, result31, x3, x31 = gener_net2.PJJDBFBWC(M, N, N1)
            self.textBrowser_PJJDBFBWC.append('model1:' + str(x3))
            self.textBrowser_PJJDBFBWC.append('model2:' + str(x31))
            self.cursot = self.textBrowser_PJJDBFBWC.textCursor()
            self.textBrowser_PJJDBFBWC.moveCursor(self.cursot.End)
            result4, result41, x4, x41 = gener_net2.JDXS(M, N, N1)
            self.textBrowser_PCL.append('model1:' + str(x4))
            self.textBrowser_PCL.append('model2:' + str(x41))
            self.cursot = self.textBrowser_PCL.textCursor()
            self.textBrowser_PCL.moveCursor(self.cursot.End)
            result5, result51, x5, x51 = gener_net2.ZWSJDWC(M, N, N1)
            self.textBrowser_FCL.append('model1:' + str(x5))
            self.textBrowser_FCL.append('model2:' + str(x51))
            self.cursot = self.textBrowser_FCL.textCursor()
            self.textBrowser_FCL.moveCursor(self.cursot.End)
            result6, result61, x6, x61 = gener_net2.XEBDXS(M, N, N1)
            self.textBrowser_XEBDXS.append('model1:' + str(x6))
            self.textBrowser_XEBDXS.append('model2:' + str(x61))
            self.cursot = self.textBrowser_XEBDXS.textCursor()
            self.textBrowser_XEBDXS.moveCursor(self.cursot.End)
            result7, result71, x7, x71 = gener_net2.FCL(M, N, N1)
            self.textBrowser_XFCL.append('model1:' + str(x7))
            self.textBrowser_XFCL.append('model2:' + str(x71))
            self.cursot = self.textBrowser_XFCL.textCursor()
            self.textBrowser_XFCL.moveCursor(self.cursot.End)
            result8, result81, x8, x81 = gener_net2.JSFCFS(M, N, N1)
            self.textBrowser_JSFCFS.append('model1:' + str(x8))
            self.textBrowser_JSFCFS.append('model2:' + str(x81))
            self.cursot = self.textBrowser_JSFCFS.textCursor()
            self.textBrowser_JSFCFS.moveCursor(self.cursot.End)
            result9, result91, x9, x91 = gener_net2.JFGWC(M, N, N1)
            self.textBrowser_MSLE.append('model1:' + str(x9))
            self.textBrowser_MSLE.append('model2:' + str(x91))
            self.cursot = self.textBrowser_MSLE.textCursor()
            self.textBrowser_MSLE.moveCursor(self.cursot.End)
            cal1, cal2 = gener_net2.calculate(M, N, N1)
            if cal1 > cal2:
                self.textBrowser_jielun_j2.append("因为模型1的误差比模型2的误差小，所以模型1的泛化能力比模型2的泛化能力强。")
            elif cal1 < cal2:
                self.textBrowser_jielun_j2.append("因为模型1的误差比模型2的误差大，所以模型2的泛化能力比模型1的泛化能力强。")
            else:
                self.textBrowser_jielun_j2.append("因为模型1的误差比模型2的误差一样，所以模型1的泛化能力和模型2的泛化能力一样。")
            datapath41 = None
            datapath51 = None
        elif datapath31 and datapath41:
            M, N = gener_net.load_data(datapath31, datapath41)
            result1, x1 = gener_net.JFWC(M, N)
            self.textBrowser_JFGWC.append(str(x1))
            self.cursot = self.textBrowser_JFGWC.textCursor()
            self.textBrowser_JFGWC.moveCursor(self.cursot.End)
            result2, x2 = gener_net.PJJDWC(M, N)
            self.textBrowser_PJJJWC.append(str(x2))
            self.cursot = self.textBrowser_PJJJWC.textCursor()
            self.textBrowser_PJJJWC.moveCursor(self.cursot.End)
            result3, x3 = gener_net.PJJDBFBWC(M, N)
            self.textBrowser_PJJDBFBWC.append(str(x3))
            self.cursot = self.textBrowser_PJJDBFBWC.textCursor()
            self.textBrowser_PJJDBFBWC.moveCursor(self.cursot.End)
            result4, x4 = gener_net.JDXS(M, N)
            self.textBrowser_PCL.append(str(x4))
            self.cursot = self.textBrowser_PCL.textCursor()
            self.textBrowser_PCL.moveCursor(self.cursot.End)
            result5, x5 = gener_net.ZWSJDWC(M, N)
            self.textBrowser_FCL.append(str(x5))
            self.cursot = self.textBrowser_FCL.textCursor()
            self.textBrowser_FCL.moveCursor(self.cursot.End)
            result6, x6 = gener_net.XEBDXS(M, N)
            self.textBrowser_XEBDXS.append(str(x6))
            self.cursot = self.textBrowser_XEBDXS.textCursor()
            self.textBrowser_XEBDXS.moveCursor(self.cursot.End)
            result7, x7 = gener_net.FCL(M, N)
            self.textBrowser_XFCL.append(str(x7))
            self.cursot = self.textBrowser_XFCL.textCursor()
            self.textBrowser_XFCL.moveCursor(self.cursot.End)
            result8, x8 = gener_net.JSFCFS(M, N)
            self.textBrowser_JSFCFS.append(str(x8))
            self.cursot = self.textBrowser_JSFCFS.textCursor()
            self.textBrowser_JSFCFS.moveCursor(self.cursot.End)
            result9, x9 = gener_net.JFGWC(M, N)
            self.textBrowser_MSLE.append(str(x9))
            self.cursot = self.textBrowser_MSLE.textCursor()
            self.textBrowser_MSLE.moveCursor(self.cursot.End)
            cal = gener_net.calculate(M, N)
            if x1 < 0.001 and x2 < 0.001 and x3 < 0.001 and x4 > 0.95 and x5 < 0.001 and x6 < 0.001 and x7 < 0.001 and x8 > 0.95 and x9 < 0.001 and gener_net.calculate(
                    M, N) < 30:
                self.textBrowser_jielun_j2.append(
                    "因为均方误差、平均绝对误差、平均绝对误差百分比中位数绝对误差、希尔不等系数、方差率和均方根误差都低于0.001，决定系数和解释方差系数高于0.95，同时不平滑的奇异点不超过30个，所以算法具有良好的泛化能力，建议直接使用。")
            elif x1 < 0.001 or x2 < 0.001 or x3 < 0.001 or x4 > 0.95 or x5 < 0.001 or x6 < 0.001 or x7 < 0.001 or x8 > 0.95 or x9 < 0.001 and gener_net.calculate(
                    M, N) < 40:
                self.textBrowser_jielun_j2.append(
                    "因为均方误差、平均绝对误差、平均绝对误差百分比中位数绝对误差、希尔不等系数、方差率和均方根误差有一个以上低于0.001，决定系数和解释方差系数有一个以上高于0.95，同时不平滑的奇异点不超过40个，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优。")
            elif x1 < 0.01 or x2 < 0.01 or x3 < 0.01 or x4 > 0.85 or x5 < 0.01 or x6 < 0.01 or x7 < 0.01 or x8 > 0.85 or x9 < 0.01 and gener_net.calculate(
                    M, N) < 50:
                self.textBrowser_jielun_j2.append(
                    "因为均方误差、平均绝对误差、平均绝对误差百分比中位数绝对误差、希尔不等系数、方差率和均方根误差有一个以上低于0.01，决定系数和解释方差系数有一个以上高于0.85，同时不平滑的奇异点不超过50个，所以算法具有一定的泛化能力，但需要优化调整。")
            else:
                self.textBrowser_jielun_j2.append(
                    "因为均方误差、平均绝对误差、平均绝对误差百分比中位数绝对误差、希尔不等系数、方差率和均方根误差都高于0.01，决定系数和解释方差系数都低于0.85，或者不平滑的奇异点超过50个，所以算法不适合于本任务，建议更换其他算法。")
            datapath41 = None
        elif datapath31 and datapath51:
            M, N = gener_net.load_data(datapath31, datapath51)
            result1, x1 = gener_net.JFWC(M, N)
            self.textBrowser_JFGWC.append(str(x1))
            self.cursot = self.textBrowser_JFGWC.textCursor()
            self.textBrowser_JFGWC.moveCursor(self.cursot.End)
            result2, x2 = gener_net.PJJDWC(M, N)
            self.textBrowser_PJJJWC.append(str(x2))
            self.cursot = self.textBrowser_PJJJWC.textCursor()
            self.textBrowser_PJJJWC.moveCursor(self.cursot.End)
            result3, x3 = gener_net.PJJDBFBWC(M, N)
            self.textBrowser_PJJDBFBWC.append(str(x3))
            self.cursot = self.textBrowser_PJJDBFBWC.textCursor()
            self.textBrowser_PJJDBFBWC.moveCursor(self.cursot.End)
            result4, x4 = gener_net.JDXS(M, N)
            self.textBrowser_PCL.append(str(x4))
            self.cursot = self.textBrowser_PCL.textCursor()
            self.textBrowser_PCL.moveCursor(self.cursot.End)
            result5, x5 = gener_net.ZWSJDWC(M, N)
            self.textBrowser_FCL.append(str(x5))
            self.cursot = self.textBrowser_FCL.textCursor()
            self.textBrowser_FCL.moveCursor(self.cursot.End)
            result6, x6 = gener_net.XEBDXS(M, N)
            self.textBrowser_XEBDXS.append(str(x6))
            self.cursot = self.textBrowser_XEBDXS.textCursor()
            self.textBrowser_XEBDXS.moveCursor(self.cursot.End)
            result7, x7 = gener_net.FCL(M, N)
            self.textBrowser_XFCL.append(str(x7))
            self.cursot = self.textBrowser_XFCL.textCursor()
            self.textBrowser_XFCL.moveCursor(self.cursot.End)
            result8, x8 = gener_net.JSFCFS(M, N)
            self.textBrowser_JSFCFS.append(str(x8))
            self.cursot = self.textBrowser_JSFCFS.textCursor()
            self.textBrowser_JSFCFS.moveCursor(self.cursot.End)
            result9, x9 = gener_net.JFGWC(M, N)
            self.textBrowser_MSLE.append(str(x9))
            self.cursot = self.textBrowser_MSLE.textCursor()
            self.textBrowser_MSLE.moveCursor(self.cursot.End)
            if x1 < 0.001 and x2 < 0.001 and x3 < 0.001 and x4 > 0.95 and x5 < 0.001 and x6 < 0.001 and x7 < 0.001 and x8 > 0.95 and x9 < 0.001 and gener_net.calculate(
                    M, N) < 30:
                self.textBrowser_jielun_j2.append(
                    "因为均方误差、平均绝对误差、平均绝对误差百分比中位数绝对误差、希尔不等系数、方差率和均方根误差都低于0.001，决定系数和解释方差系数高于0.95，同时不平滑的奇异点不超过30个，所以算法具有良好的泛化能力，建议直接使用。")
            elif x1 < 0.001 or x2 < 0.001 or x3 < 0.001 or x4 > 0.95 or x5 < 0.001 or x6 < 0.001 or x7 < 0.001 or x8 > 0.95 or x9 < 0.001 and gener_net.calculate(
                    M, N) < 40:
                self.textBrowser_jielun_j2.append(
                    "因为均方误差、平均绝对误差、平均绝对误差百分比中位数绝对误差、希尔不等系数、方差率和均方根误差有一个以上低于0.001，决定系数和解释方差系数有一个以上高于0.95，同时不平滑的奇异点不超过40个，所以算法具有较好的泛化能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优。")
            elif x1 < 0.01 or x2 < 0.01 or x3 < 0.01 or x4 > 0.85 or x5 < 0.01 or x6 < 0.01 or x7 < 0.01 or x8 > 0.85 or x9 < 0.01 and gener_net.calculate(
                    M, N) < 50:
                self.textBrowser_jielun_j2.append(
                    "因为均方误差、平均绝对误差、平均绝对误差百分比中位数绝对误差、希尔不等系数、方差率和均方根误差有一个以上低于0.01，决定系数和解释方差系数有一个以上高于0.85，同时不平滑的奇异点不超过50个，所以算法具有一定的泛化能力，但需要优化调整。")
            else:
                self.textBrowser_jielun_j2.append(
                    "因为均方误差、平均绝对误差、平均绝对误差百分比中位数绝对误差、希尔不等系数、方差率和均方根误差都高于0.01，决定系数和解释方差系数都低于0.85，或者不平滑的奇异点超过40个，所以算法不适合于本任务，建议更换其他算法。")
            datapath51 = None

    # 决策2-鲁棒性
    def display_J2R(self):
        global image_path_jr1, image_path_jr2, image_path_jr3
        self.image_path_jr1 = QImage(image_path_jr1)
        self.image_path_jr2 = QImage(image_path_jr2)
        self.image_path_jr3 = QImage(image_path_jr3)
        self.fcku_J2R(self.image_path_jr1)
        self.fcku2_J2R(self.image_path_jr2)
        self.fcku3_J2R(self.image_path_jr3)
        self.timer.timeout.connect(lambda: self.fcku_J2R(self.image_path_jr1))
        self.timer.timeout.connect(lambda: self.fcku2_J2R(self.image_path_jr2))
        self.timer.timeout.connect(lambda: self.fcku3_J2R(self.image_path_jr3))
        self.timer.start(10)

    def fcku_J2R(self, fckimage):
        pil_image = self.m_resize_J2R(self.label_pjjdwc_2.width(), self.label_pjjdwc_2.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_pjjdwc_2.setPixmap(pixmap)

    def fcku2_J2R(self, fckimage):
        pil_image = self.m_resize_J2R(self.label_jfgwc_2.width(), self.label_jfgwc_2.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_jfgwc_2.setPixmap(pixmap)

    def fcku3_J2R(self, fckimage):
        pil_image = self.m_resize_J2R(self.label_jsfcfs_2.width(), self.label_jsfcfs_2.height(), fckimage)
        pixmap = QPixmap.fromImage(pil_image)
        self.label_jsfcfs_2.setPixmap(pixmap)

    def m_resize_J2R(self, w_box, h_box, pil_image):
        w, h = pil_image.width(), pil_image.height()
        f1 = 1.0 * w_box / w
        f2 = 1.0 * h_box / h
        factor = min([f1, f2])
        width = int(w * factor)
        height = int(h * factor)
        return pil_image.scaled(width, height)

    def JR2_run(self):
        global datapath511, JRpath11, JRpath211, image_path_jr1, image_path_jr2, image_path_jr3
        self.timer.stop()
        self.label_pjjdwc_2.clear()
        self.textBrowser_pjjdwc.clear()
        self.label_jfgwc_2.clear()
        self.textBrowser_jfgwc.clear()
        self.label_jsfcfs_2.clear()
        self.textBrowser_jsfcfs.clear()
        self.textBrowser_jielun_r_j2.clear()
        if self.lineEdit_threthold_j2.text():
            threthold = float(self.lineEdit_threthold_j2.text())
        else:
            threthold = 30
        if self.lineEdit_lapse_j2.text():
            lapse = float(self.lineEdit_lapse_j2.text())
        else:
            lapse = 60
        a = JRpath11
        b = JRpath211
        print(JRpath11)
        print(JRpath211)
        if datapath511 and JRpath211 and JRpath11:
            y_list1, ylist11 = robust_net2.PJJDWC_data(datapath511, JRpath11, JRpath211, threthold, lapse)
            self.textBrowser_pjjdwc.append(str(y_list1))
            self.textBrowser_pjjdwc.append(str(ylist11))
            self.cursot = self.textBrowser_pjjdwc.textCursor()
            self.textBrowser_pjjdwc.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            y_list2, y_list21 = robust_net2.JFGWC_data(datapath511, JRpath11, JRpath211, threthold, lapse)
            self.textBrowser_jfgwc.append(str(y_list2))
            self.textBrowser_jfgwc.append(str(y_list21))
            self.cursot = self.textBrowser_jfgwc.textCursor()
            self.textBrowser_jfgwc.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            y_list3, y_list31 = robust_net2.ZWSJDWC_data(datapath511, JRpath11, JRpath211, threthold, lapse)
            self.textBrowser_jsfcfs.append(str(y_list3))
            self.textBrowser_jsfcfs.append(str(y_list31))
            self.cursot = self.textBrowser_jsfcfs.textCursor()
            self.textBrowser_jsfcfs.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            cal, cal1 = robust_net2.calculate(datapath511, JRpath11, JRpath211)
            if cal > cal1:
                self.textBrowser_jielun_r_j2.append("因为模型1的误差比模型2的误差小，所以模型1具有更好的鲁棒能力。")
            elif cal1 > cal:
                self.textBrowser_jielun_r_j2.append("因为模型2的误差比模型1的误差小，所以模型1具有更好的鲁棒能力。")
            else:
                self.textBrowser_jielun_r_j2.append("因为模型1的误差和模型2的误差一样，所以模型1和模型2鲁棒能力相同。")
            self.cursot = self.textBrowser_jielun_r_j.textCursor()
            self.textBrowser_jielun_r_j.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            image_path_jr1 = 'PJJDWC_r.jpg'
            image_path_jr3 = 'ZWSJDWC_r.jpg'
            image_path_jr2 = 'JFGWC_r.jpg'
            self.display_J2R()
            JRpath11 = None
            JRpath211 = None
        elif datapath511 and JRpath11:
            y_list1 = robust_net.PJJDWC_data(datapath511, JRpath11, threthold, lapse)
            self.textBrowser_pjjdwc.append(str(y_list1))
            self.cursot = self.textBrowser_pjjdwc.textCursor()
            self.textBrowser_pjjdwc.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            y_list2 = robust_net.JFGWC_data(datapath511, JRpath11, threthold, lapse)
            self.textBrowser_jfgwc.append(str(y_list2))
            self.cursot = self.textBrowser_jfgwc.textCursor()
            self.textBrowser_jfgwc.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            y_list3 = robust_net.ZWSJDWC_data(datapath511, JRpath11, threthold, lapse)
            self.textBrowser_jsfcfs.append(str(y_list3))
            self.cursot = self.textBrowser_jsfcfs.textCursor()
            self.textBrowser_jsfcfs.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            if y_list1[19] < y_list1[0] * threthold and y_list2[19] < y_list2[0] * threthold and y_list3[19] < y_list3[
                0] * threthold:
                self.textBrowser_jielun_r_j2.append("因为平均绝对误差、均方根误差、中位数绝对误差加0.2噪声时也不高于可用阈值，所以算法具有良好的鲁棒能力，建议直接使用。")
            elif y_list1[14] < y_list1[0] * threthold and y_list1[19] < y_list1[0] * lapse or y_list2[14] < y_list2[
                0] * threthold and y_list2[19] < y_list2[0] * lapse or y_list3[14] < y_list3[0] * threthold and y_list3[
                19] < y_list3[0] * lapse:
                self.textBrowser_jielun_r_j2.append(
                    "因为平均绝对误差、均方根误差、中位数绝对误差中有一个以上加0.15噪声时也不高于可用阈值，同时平均绝对误差、均方根误差、中位数绝对误差有一个以上加0.2噪声时也不高于失效阈值，所以算法具有较好的鲁棒能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优。")
            elif y_list1[4] < y_list1[0] * threthold or y_list1[19] < y_list1[0] * lapse or y_list2[4] < y_list2[
                0] * threthold or y_list2[19] < y_list2[0] * lapse or y_list3[4] < y_list3[0] * threthold or y_list3[
                19] < \
                    y_list3[0] * lapse:
                self.textBrowser_jielun_r_j2.append(
                    "因为平均绝对误差、均方根误差、中位数绝对误差中有一个以上加0.05噪声时也不高于可用阈值，或者平均绝对误差、均方根误差、中位数绝对误差有一个以上加0.2噪声时也不高于失效阈值，所以算法具有一定的鲁棒能力，但需要优化调整，建议从算法上提升性能，可以将通道分成多组，每组单独进行卷积，然后再将通道合成可以减少模型的参数，提高模型准确率。")
            else:
                self.textBrowser_jielun_r_j2.append(
                    "因为平均绝对误差、均方根误差、中位数绝对误差加0.05噪声时都高于可用阈值，同时平均绝对误差、均方根误差、中位数绝对误差加0.2噪声时都高于失效阈值，所以算法鲁棒能力较差，不适合于本任务，建议更换其他算法。")
            self.cursot = self.textBrowser_jielun_r_j.textCursor()
            self.textBrowser_jielun_r_j.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            image_path_jr1 = 'PJJDWC_r.jpg'
            image_path_jr3 = 'ZWSJDWC_r.jpg'
            image_path_jr2 = 'JFGWC_r.jpg'
            self.display_J2R()
            JRpath11 = None
        elif datapath511 and JRpath211:
            y_list1 = robust_net.PJJDWC_data(datapath511, JRpath211, threthold, lapse)
            self.textBrowser_pjjdwc.append(str(y_list1))
            self.cursot = self.textBrowser_pjjdwc.textCursor()
            self.textBrowser_pjjdwc.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            y_list2 = robust_net.JFGWC_data(datapath511, JRpath211, threthold, lapse)
            self.textBrowser_jfgwc.append(str(y_list2))
            self.cursot = self.textBrowser_jfgwc.textCursor()
            self.textBrowser_jfgwc.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            y_list3 = robust_net.ZWSJDWC_data(datapath511, JRpath211, threthold, lapse)
            self.textBrowser_jsfcfs.append(str(y_list3))
            self.cursot = self.textBrowser_jsfcfs.textCursor()
            self.textBrowser_jsfcfs.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            if y_list1[19] < y_list1[0] * threthold and y_list2[19] < y_list2[0] * threthold and y_list3[19] < y_list3[
                0] * threthold:
                self.textBrowser_jielun_r_j2.append("因为平均绝对误差、均方根误差、中位数绝对误差加0.2噪声时也不高于可用阈值，所以算法具有良好的鲁棒能力，建议直接使用。")
            elif y_list1[14] < y_list1[0] * threthold and y_list1[19] < y_list1[0] * lapse or y_list2[14] < y_list2[
                0] * threthold and y_list2[19] < y_list2[0] * lapse or y_list3[14] < y_list3[0] * threthold and y_list3[
                19] < y_list3[0] * lapse:
                self.textBrowser_jielun_r_j2.append(
                    "因为平均绝对误差、均方根误差、中位数绝对误差中有一个以上加0.15噪声时也不高于可用阈值，同时平均绝对误差、均方根误差、中位数绝对误差有一个以上加0.2噪声时也不高于失效阈值，所以算法具有较好的鲁棒能力，建议在有条件情况下增加样本数量，同时在训练过程中进行参数调优。")
            elif y_list1[4] < y_list1[0] * threthold or y_list1[19] < y_list1[0] * lapse or y_list2[4] < y_list2[
                0] * threthold or y_list2[19] < y_list2[0] * lapse or y_list3[4] < y_list3[0] * threthold or y_list3[
                19] < \
                    y_list3[0] * lapse:
                self.textBrowser_jielun_r_j2.append(
                    "因为平均绝对误差、均方根误差、中位数绝对误差中有一个以上加0.05噪声时也不高于可用阈值，或者平均绝对误差、均方根误差、中位数绝对误差有一个以上加0.2噪声时也不高于失效阈值，所以算法具有一定的鲁棒能力，但需要优化调整，建议从算法上提升性能，可以将通道分成多组，每组单独进行卷积，然后再将通道合成可以减少模型的参数，提高模型准确率。")
            else:
                self.textBrowser_jielun_r_j2.append(
                    "因为平均绝对误差、均方根误差、中位数绝对误差加0.05噪声时都高于可用阈值，同时平均绝对误差、均方根误差、中位数绝对误差加0.2噪声时都高于失效阈值，所以算法鲁棒能力较差，不适合于本任务，建议更换其他算法。")
            self.cursot = self.textBrowser_jielun_r_j.textCursor()
            self.textBrowser_jielun_r_j.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
            image_path_jr1 = 'PJJDWC_r.jpg'
            image_path_jr3 = 'ZWSJDWC_r.jpg'
            image_path_jr2 = 'JFGWC_r.jpg'
            self.display_J2R()
            JRpath211 = None

    # 决策2-测试用例生成
    def J2DR_run(self):
        global JDpath1, datapath6
        self.timer.stop()
        self.textBrowser_show_j2.clear()
        # shutil.rmtree('D:\\data\\juece\\robust\\robust')
        # shutil.rmtree(JDRpath2)
        if self.lineEdit_noise_j.text():
            noise_num = self.lineEdit_noise_j.text().split(',')
        else:
            noise_num = [0.01, 0.01, 20]
        numl = []
        for i in range(len(noise_num)):
            numl.append(float(noise_num[i]))
        qishi, buchang, zu = numl[0], numl[1], int(numl[2])
        x = noise_net.main(datapath6, JDpath1, qishi, buchang, zu)
        self.textBrowser_show_j2.append('运行结束！')
        self.cursot = self.textBrowser_show_j2.textCursor()
        self.textBrowser_show_j2.moveCursor(self.cursot.End)
        QtWidgets.QApplication.processEvents()

    # 自主能力等级
    def score_zero(self):
        self.textBrowser_result_zizhu.clear()

    def score_calculate(self):
        global score
        self.textBrowser_result_zizhu.clear()
        score_gengxin = -1
        score_xuexi = -1
        score_shibie = -1
        score_juece = -1
        score_huanjing = -1
        if self.radioButton_gengxinA.isChecked() == True:
            score_gengxin = 0
            score_gengxin += 5
        elif self.radioButton_gengxinB.isChecked() == True:
            score_gengxin = 0
            score_gengxin += 4
        elif self.radioButton_gengxinC.isChecked() == True:
            score_gengxin = 0
            score_gengxin += 3
        elif self.radioButton_gengxinD.isChecked() == True:
            score_gengxin = 0
            score_gengxin += 2
        elif self.radioButton_gengxinE.isChecked() == True:
            score_gengxin = 0
            score_gengxin += 1
        elif self.radioButton.isChecked() == True:
            score_gengxin = 0
            score_gengxin += 0
        if self.radioButton_xuexiA.isChecked() == True:
            score_xuexi = 0
            score_xuexi += 5
        elif self.radioButton_xuexiB.isChecked() == True:
            score_xuexi = 0
            score_xuexi += 4
        elif self.radioButton_xuexiC.isChecked() == True:
            score_xuexi = 0
            score_xuexi += 3
        elif self.radioButton_xuexiD.isChecked() == True:
            score_xuexi = 0
            score_xuexi += 2
        elif self.radioButton_xuexiE.isChecked() == True:
            score_xuexi = 0
            score_xuexi += 1
        elif self.radioButton_4.isChecked() == True:
            score_xuexi = 0
            score_xuexi += 0
        if self.radioButton_shibieA.isChecked() == True:
            score_shibie = 0
            score_shibie += 5
        elif self.radioButton_shibieB.isChecked() == True:
            score_shibie = 0
            score_shibie += 4
        elif self.radioButton_shibieC.isChecked() == True:
            score_shibie = 0
            score_shibie += 3
        elif self.radioButton_shibieD.isChecked() == True:
            score_shibie = 0
            score_shibie += 2
        elif self.radioButton_shibieE.isChecked() == True:
            score_shibie = 0
            score_shibie += 1
        elif self.radioButton_2.isChecked() == True:
            score_shibie = 0
            score_shibie += 0
        if self.radioButton_jueceA.isChecked() == True:
            score_juece = 0
            score_juece += 5
        elif self.radioButton_jueceB.isChecked() == True:
            score_juece = 0
            score_juece += 4
        elif self.radioButton_jueceC.isChecked() == True:
            score_juece = 0
            score_juece += 3
        elif self.radioButton_jueceD.isChecked() == True:
            score_juece = 0
            score_juece += 2
        elif self.radioButton_jueceE.isChecked() == True:
            score_juece = 0
            score_juece += 1
        elif self.radioButton_5.isChecked() == True:
            score_juece = 0
            score_juece += 0
        if self.radioButton_huanjingA.isChecked() == True:
            score_huanjing = 0
            score_huanjing += 5
        elif self.radioButton_huanjingB.isChecked() == True:
            score_huanjing = 0
            score_huanjing += 4
        elif self.radioButton_huanjingC.isChecked() == True:
            score_huanjing = 0
            score_huanjing += 3
        elif self.radioButton_huanjingD.isChecked() == True:
            score_huanjing = 0
            score_huanjing += 2
        elif self.radioButton_huanjingE.isChecked() == True:
            score_huanjing = 0
            score_huanjing += 1
        elif self.radioButton_3.isChecked() == True:
            score_huanjing = 0
            score_huanjing += 0
        if score_gengxin != -1 and score_xuexi != -1 and score_shibie != -1 and score_juece != -1 and score_huanjing != -1:
            score = score_gengxin + score_xuexi + score_shibie + score_juece + score_huanjing
        else:
            self.textBrowser_result_zizhu.append('您未选全则全部评价标准！')
        if score >= 0 and score <= 5:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为0级。')
        elif score >= 6 and score <= 9:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为1级。')
        elif score >= 10 and score <= 11:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为2级。')
        elif score >= 12 and score <= 13:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为3级。')
        elif score >= 14 and score <= 15:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为4级。')
        elif score >= 16 and score <= 17:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为5级。')
        elif score >= 18 and score <= 19:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为6级。')
        elif score >= 20 and score <= 21:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为7级。')
        elif score >= 22 and score <= 23:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为8级。')
        elif score >= 24 and score <= 25:
            self.textBrowser_result_zizhu.append('经评定，该系统自主能力得分为' + str(score) + '分,为9级。')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DetailUI()
    ex.show()
    sys.exit(app.exec_())
