import webbrowser
from PyQt5.QtWidgets import*
from Ders_tasarım import Ui_MainWindow


class a(QMainWindow):


    def __init__(self):
        super().__init__()


        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_1.clicked.connect(self.a_clicked_slot)
        self.ui.pushButton_2.clicked.connect(self.b_clicked_slot)
        self.ui.pushButton_3.clicked.connect(self.c_clicked_slot)
        self.ui.pushButton_4.clicked.connect(self.d_clicked_slot)
        self.ui.pushButton_5.clicked.connect(self.e_clicked_slot)
        self.ui.pushButton_6.clicked.connect(self.f_clicked_slot)
        self.ui.pushButton_7.clicked.connect(self.g_clicked_slot)
        self.ui.pushButton_8.clicked.connect(self.h_clicked_slot)
        self.ui.pushButton_9.clicked.connect(self.i_clicked_slot)
        self.ui.pushButton_10.clicked.connect(self.j_clicked_slot)
        self.ui.pushButton_11.clicked.connect(self.k_clicked_slot)
        self.ui.pushButton_12.clicked.connect(self.l_clicked_slot)
        self.ui.pushButton_13.clicked.connect(self.m_clicked_slot)
        self.ui.pushButton_14.clicked.connect(self.n_clicked_slot)
        self.ui.pushButton_15.clicked.connect(self.o_clicked_slot)
        self.ui.pushButton_16.clicked.connect(self.p_clicked_slot)
        self.ui.pushButton_17.clicked.connect(self.r_clicked_slot)
        self.ui.pushButton_18.clicked.connect(self.s_clicked_slot)
        self.ui.pushButton_19.clicked.connect(self.t_clicked_slot)

        self.ui.pushButton_20.clicked.connect(self.u_clicked_slot)
        self.ui.pushButton_21.clicked.connect(self.v_clicked_slot)
        self.ui.pushButton_22.clicked.connect(self.w_clicked_slot)
        self.ui.pushButton_23.clicked.connect(self.x_clicked_slot)
        self.ui.pushButton_24.clicked.connect(self.y_clicked_slot)
        self.ui.pushButton_25.clicked.connect(self.z_clicked_slot)

        self.ui.pushButton_26.clicked.connect(self.aa_clicked_slot)
        self.ui.pushButton_27.clicked.connect(self.bb_clicked_slot)
        self.ui.pushButton_28.clicked.connect(self.cc_clicked_slot)
        self.ui.pushButton_29.clicked.connect(self.dd_clicked_slot)
        self.ui.pushButton_30.clicked.connect(self.ee_clicked_slot)

        self.ui.pushButton_31.clicked.connect(self.ff_clicked_slot)
        self.ui.pushButton_32.clicked.connect(self.gg_clicked_slot)
        self.ui.pushButton_33.clicked.connect(self.hh_clicked_slot)
        self.ui.pushButton_34.clicked.connect(self.ii_clicked_slot)
        self.ui.pushButton_35.clicked.connect(self.jj_clicked_slot)


    def a_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesimatematik/9/unite1/index.html")
    
    def b_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesimatematik/9/unite2/index.html")

    def c_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesimatematik/9/unite3/index.html")

    def d_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesimatematik/9/unite4/index.html")

    def e_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesimatematik/9/unite5/index.html")
        
    def f_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesifizik/9/unite1/index.html")

    def g_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesifizik/9/unite2/index.html")

    def h_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesifizik/9/unite3/index.html")

    def i_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesifizik/9/unite4/index.html")

    def j_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesifizik/9/unite5/index.html")

    def k_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesifizik/9/unite6/index.html")

    def l_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesibiyoloji/9/unite1/index.html")

    def m_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesibiyoloji/9/unite2/index.html")

    def n_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesibiyoloji/9/unite3/index.html")

    def o_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesikimya/9/unite1/index.html")

    def p_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesikimya/9/unite2/index.html")

    def r_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesikimya/9/unite3/index.html")

    def s_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesikimya/9/unite4/index.html")

    def t_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/fenlisesikimya/9/unite5/index.html")

    def u_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/tarih/9/unite1/index.html")

    def v_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/tarih/9/unite2/index.html")

    def w_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/tarih/9/unite3/index.html")

    def x_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/tarih/9/unite4/index.html")

    def y_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/tarih/9/unite5/index.html")

    def z_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/tarih/9/unite6/index.html")
        
    def aa_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/cografya/9/ankara/unite1/bolum1234/index.html")

    def bb_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/cografya/9/ankara/unite1/bolum5/index.html")

    def cc_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/cografya/9/ankara/unite2/index.html")

    def dd_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/cografya/9/ankara/unite3/index.html")

    def ee_clicked_slot(self):
        webbrowser.open("http://ogmmateryal.eba.gov.tr/panel/upload/etkilesimli/kitap/cografya/9/ankara/unite4/index.html")

    def ff_clicked_slot(self):
        webbrowser.open("http://dogm.eba.gov.tr/panel/upload/etkilesimli/kitap/DKB9/Unite1/unite1.html")

    def gg_clicked_slot(self):
        webbrowser.open("http://dogm.eba.gov.tr/panel/upload/etkilesimli/kitap/DKB9/Unite2/unite2.html")

    def hh_clicked_slot(self):
        webbrowser.open("http://dogm.eba.gov.tr/panel/upload/etkilesimli/kitap/DKB9/Unite3/unite3.html")

    def ii_clicked_slot(self):
        webbrowser.open("http://dogm.eba.gov.tr/panel/upload/etkilesimli/kitap/DKB9/Unite4/unite4.html")

    def jj_clicked_slot(self):
        webbrowser.open("http://dogm.eba.gov.tr/panel/upload/etkilesimli/kitap/DKB9/Unite5/unite5.html")

    

    







uygulama = QApplication([])
pencere = a()
pencere.show()
uygulama.exec_()
