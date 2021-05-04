from PyQt5 import QtCore, QtGui, QtWidgets
import Diffi
import diffiParam
import EllipDiffiParam
import EllipDiffi
import time


class Ui_DiffiHelman(object):
    def setupUi(self, DiffiHelman):
        DiffiHelman.setObjectName("DiffiHelman")
        DiffiHelman.resize(991, 601)
        DiffiHelman.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(DiffiHelman)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, -30, 991, 601))
        self.widget.setObjectName("widget")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 308, 732, 19))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter_11 = QtWidgets.QSplitter(self.widget)
        self.splitter_11.setGeometry(QtCore.QRect(10, 40, 961, 551))
        self.splitter_11.setOrientation(QtCore.Qt.Vertical)
        self.splitter_11.setObjectName("splitter_11")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        self.label.setObjectName("label")
        self.diff_g = QtWidgets.QLineEdit(self.splitter_2)
        self.diff_g.setObjectName("diff_g")
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.calc)
        self.diffi_text = QtWidgets.QTextBrowser(self.splitter_3)
        self.diffi_text.setObjectName("diffi_text")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_2 = QtWidgets.QLabel(self.splitter_4)
        self.label_2.setObjectName("label_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.diffi_param_xa = QtWidgets.QLineEdit(self.layoutWidget)
        self.diffi_param_xa.setObjectName("diffi_param_xa")
        self.gridLayout.addWidget(self.diffi_param_xa, 0, 1, 1, 1)
        self.diffi_param_Rb = QtWidgets.QLineEdit(self.layoutWidget)
        self.diffi_param_Rb.setObjectName("diffi_param_Rb")
        self.gridLayout.addWidget(self.diffi_param_Rb, 1, 0, 1, 1)
        self.diffi_param_xb = QtWidgets.QLineEdit(self.layoutWidget)
        self.diffi_param_xb.setObjectName("diffi_param_xb")
        self.gridLayout.addWidget(self.diffi_param_xb, 1, 1, 1, 1)
        self.diffi_param_Ra = QtWidgets.QLineEdit(self.layoutWidget)
        self.diffi_param_Ra.setText("")
        self.diffi_param_Ra.setObjectName("diffi_param_Ra")
        self.gridLayout.addWidget(self.diffi_param_Ra, 0, 0, 1, 1)
        self.diffi_param_text = QtWidgets.QTextBrowser(self.splitter)
        self.diffi_param_text.setObjectName("diffi_param_text")
        self.splitter_10 = QtWidgets.QSplitter(self.splitter_11)
        self.splitter_10.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_10.setObjectName("splitter_10")
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.label_3 = QtWidgets.QLabel(self.splitter_9)
        self.label_3.setObjectName("label_3")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_6)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.el_diffi_a = QtWidgets.QLineEdit(self.layoutWidget1)
        self.el_diffi_a.setObjectName("el_diffi_a")
        self.horizontalLayout.addWidget(self.el_diffi_a)
        self.el_diffi_b = QtWidgets.QLineEdit(self.layoutWidget1)
        self.el_diffi_b.setObjectName("el_diffi_b")
        self.horizontalLayout.addWidget(self.el_diffi_b)
        self.el_diffi_text = QtWidgets.QTextBrowser(self.splitter_6)
        self.el_diffi_text.setObjectName("el_diffi_text")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.label_4 = QtWidgets.QLabel(self.splitter_8)
        self.label_4.setObjectName("label_4")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_8)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_7)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.el_diffi_para_a = QtWidgets.QLineEdit(self.layoutWidget2)
        self.el_diffi_para_a.setObjectName("el_diffi_para_a")
        self.horizontalLayout_3.addWidget(self.el_diffi_para_a)
        self.el_diffi_param_B = QtWidgets.QLineEdit(self.layoutWidget2)
        self.el_diffi_param_B.setObjectName("el_diffi_param_B")
        self.horizontalLayout_3.addWidget(self.el_diffi_param_B)
        self.el_diffi_param_R = QtWidgets.QLineEdit(self.layoutWidget2)
        self.el_diffi_param_R.setObjectName("el_diffi_param_R")
        self.horizontalLayout_3.addWidget(self.el_diffi_param_R)
        self.el_diffi_param_text = QtWidgets.QTextBrowser(self.splitter_7)
        self.el_diffi_param_text.setObjectName("el_diffi_param_text")
        DiffiHelman.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DiffiHelman)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 25))
        self.menubar.setObjectName("menubar")
        DiffiHelman.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DiffiHelman)
        self.statusbar.setObjectName("statusbar")
        DiffiHelman.setStatusBar(self.statusbar)

        self.retranslateUi(DiffiHelman)
        QtCore.QMetaObject.connectSlotsByName(DiffiHelman)

    def diffi(self, g):
        start_time = time.time()
        diffi_object = Diffi(g)
        a, b, p, g, A, B, Ka, Kb = diffi_object.calc()
        end_time = (time.time() - start_time)*1000
        diffi_text = self.diffi_text.textCursor()
        diffi_text.insertHtml(f'''<br><b>a:</b>{a}
            <br><b>b: </b>{b}
            <br><b>p: </b>{p}
            <br><b>g: </b>{g}
            <br><b>A: </b>{A}
            <br><b>B: </b>{B}
            <br><b>Ka: </b>{Ka}
            <br><b>Kb: </b>{Kb}
            <br><b>vaqt: </b>{round(end_time, 3)}<br>
            <br>''')

    def diffi_param(self, Ra, Rb, xa, xb):
        start_time = time.time()
        diffi_object = diffiParam()
        Ra, Rb, xa, xb, Ra_mult_a, Rb_mult_a, ya, yb, Ra_minus_1_mult_yb, Rb_minus_1_mult_ya, Rab, ka, kb, Ka, Ka = diffi_object.calc(
            Ra, Rb, xa, xb)
        end_time = (time.time() - start_time)*1000
        diffi_text = self.diffi_param_text.textCursor()
        diffi_text.insertHtml(f'''<br><b>Ra:</b>{Ra}
            <br><b>Rb: </b>{Rb}
            <br><b>xa: </b>{xa}
            <br><b>xb: </b>{xb}
            <br><b>Ra*a: </b>{Ra_mult_a}
            <br><b>Rb*a: </b>{Rb_mult_a}
            <br><b>ya: </b>{ya}
            <br><b>yb: </b>{yb}
            <br><b>Ra-1*yb: </b>{Ra_minus_1_mult_yb}
            <br><b>Rb-1*ya: </b>{Rb_minus_1_mult_ya}
            <br><b>Rab: </b>{Rab}
            <br><b>ka: </b>{ka}
            <br><b>kb: </b>{kb}
            <br><b>Ka: </b>{Ka}
            <br><b>Ka: </b>{Ka}
            <br><b>vaqt: </b>{round(end_time, 3)}<br>
            <br>''')

    def el_diffi_param(self, a, B, R):
        start_time = time.time()
        diffi_object = EllipDiffiParam(a, B, R)
        N, primes, p, a, b, G, n, h, Na, Nb, pa, pb, Pa, Pb, ka, kb, Ka, Kb = diffi_object.calc()
        end_time = (time.time() - start_time)*1000
        diffi_text = self.el_diffi_param_text.textCursor()
        diffi_text.insertHtml(f'''<br><b>N:</b>{N}
            <br><b>Tub bo'luvchilari: </b>{primes}
            <br><b>p: </b>{p}
            <br><b>a: </b>{a}
            <br><b>b: </b>{b}
            <br><b>G: </b>{G}
            <br><b>n: </b>{n}
            <br><b>h: </b>{h}
            <br><b>Na: </b>{Na}
            <br><b>Nb: </b>{Nb}
            <br><b>pa: </b>{pa}
            <br><b>pb: </b>{pb}
            <br><b>Pa: </b>{Pa}
            <br><b>Pb: </b>{Pb}
            <br><b>ka: </b>{ka}
            <br><b>kb: </b>{kb}
            <br><b>Ka: </b>{Ka}
            <br><b>Kb: </b>{Kb}
            <br><b>vaqt: </b>{round(end_time, 3)}<br>
            <br>''')

    def el_diffi(self, a, b):
        start_time = time.time()
        diffi_object = EllipDiffi(a, b)
        N, prim, all_points, G, p, a, b, G, h, a_maxfiy, b_maxfiy, A_nuqta, B_nuqta, K_a, K_b = diffi_object.calc()
        end_time = (time.time() - start_time)*1000
        diffi_text = self.el_diffi_text.textCursor()
        diffi_text.insertHtml(f'''<br><b>N:</b>{N}
            <br><b>Tub bo'luvchilari: </b>{prim}
            <br><b>all_points: </b>{all_points}
            <br><b>G: </b>{G}
            <br><b>p: </b>{p}
            <br><b>a: </b>{a}
            <br><b>b: </b>{b}
            <br><b>G: </b>{G}
            <br><b>h: </b>{h}
            <br><b>a_maxfiy: </b>{a_maxfiy}
            <br><b>b_maxfiy: </b>{b_maxfiy}
            <br><b>A_nuqta: </b>{A_nuqta}
            <br><b>B_nuqta: </b>{B_nuqta}
            <br><b>K_a: </b>{K_a}
            <br><b>K_b: </b>{K_b}
            <br><b>vaqt: </b>{round(end_time, 3)}<br>
            <br>''')

    def calc(self):
        g = int(self.diff_g.text())
        self.diffi(g)
        Ra = int(self.diffi_param_Ra.text())
        Rb = int(self.diffi_param_Rb.text())
        xa = int(self.diffi_param_xa.text())
        xb = int(self.diffi_param_xb.text())
        self.diffi_param(Ra, Rb, xa, xb)
        a = int(self.el_diffi_para_a.text())
        B = int(self.el_diffi_param_B.text())
        R = int(self.el_diffi_param_R.text())
        self.el_diffi_param(a, B, R)
        a = int(self.el_diffi_a.text())
        b = int(self.el_diffi_b.text())
        self.el_diffi(a, b)

    def retranslateUi(self, DiffiHelman):
        _translate = QtCore.QCoreApplication.translate
        DiffiHelman.setWindowTitle(_translate("DiffiHelman", "Diffi Helman"))
        self.label.setText(_translate("DiffiHelman", "Diffi Helman"))
        self.diff_g.setPlaceholderText(_translate("DiffiHelman", "g"))
        self.pushButton.setText(_translate("DiffiHelman", "Hisoblash"))
        self.diffi_text.setWhatsThis(_translate(
            "DiffiHelman", "<html><head/><body><p>dsadasd</p></body></html>"))
        self.diffi_text.setPlaceholderText(_translate("DiffiHelman", "Natija"))
        self.label_2.setText(_translate("DiffiHelman", "Diffi Helman(param)"))
        self.diffi_param_xa.setPlaceholderText(_translate("DiffiHelman", "xa"))
        self.diffi_param_Rb.setPlaceholderText(_translate("DiffiHelman", "Rb"))
        self.diffi_param_xb.setPlaceholderText(_translate("DiffiHelman", "xb"))
        self.diffi_param_Ra.setPlaceholderText(_translate("DiffiHelman", "Ra"))
        self.diffi_param_text.setPlaceholderText(
            _translate("DiffiHelman", "Natija"))
        self.label_3.setText(_translate(
            "DiffiHelman", "Elliptic Diffi Helman"))
        self.el_diffi_a.setPlaceholderText(_translate("DiffiHelman", "a"))
        self.el_diffi_b.setPlaceholderText(_translate("DiffiHelman", "b"))
        self.el_diffi_text.setPlaceholderText(
            _translate("DiffiHelman", "Natija"))
        self.label_4.setText(_translate(
            "DiffiHelman", "Elliptic Diffi Helman(Param)"))
        self.el_diffi_para_a.setPlaceholderText(_translate("DiffiHelman", "a"))
        self.el_diffi_param_B.setPlaceholderText(
            _translate("DiffiHelman", "B"))
        self.el_diffi_param_R.setPlaceholderText(
            _translate("DiffiHelman", "R"))
        self.el_diffi_param_text.setPlaceholderText(
            _translate("DiffiHelman", "Natija"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DiffiHelman = QtWidgets.QMainWindow()
    ui = Ui_DiffiHelman()
    ui.setupUi(DiffiHelman)
    DiffiHelman.show()
    sys.exit(app.exec_())
