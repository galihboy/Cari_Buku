# -*- coding: utf-8 -*-
'''
Created on Tue Oct  5 06:11:45 2021

@author: galih-hermawan
Repository: https://github.com/galihboy/
Web: https://galih.eu
'''
# Form implementation generated from reading ui file 'cari buku.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 526)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(MainWindow.width(), MainWindow.height()))
        MainWindow.setMaximumSize(QtCore.QSize(MainWindow.width(), MainWindow.height()))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("buku.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1, 1, 541, 471))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tabCari = QtWidgets.QWidget()
        self.tabCari.setObjectName("tabCari")
        self.label = QtWidgets.QLabel(self.tabCari)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 13))
        self.label.setObjectName("label")
        self.txtCari = QtWidgets.QLineEdit(self.tabCari)
        self.txtCari.setGeometry(QtCore.QRect(83, 6, 220, 20))
        self.txtCari.setObjectName("txtCari")
        self.cboExtensions = QtWidgets.QComboBox(self.tabCari)
        self.cboExtensions.setGeometry(QtCore.QRect(310, 6, 70, 22))
        self.cboExtensions.setObjectName("cboExtensions")
        #self.cboExtensions.setToolTip("Tes")
        self.cboFileDir = QtWidgets.QComboBox(self.tabCari)
        self.cboFileDir.setGeometry(QtCore.QRect(83, 36, 111, 22))
        self.cboFileDir.setObjectName("cboFileDir")
        #self.cboFileDir.setCurrentIndex(2)
        self.label_2 = QtWidgets.QLabel(self.tabCari)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.label_2.setObjectName("label_2")
        self.cboDir = QtWidgets.QComboBox(self.tabCari)
        self.cboDir.setGeometry(QtCore.QRect(200, 36, 181, 22))
        self.cboDir.setObjectName("cboDir")
        self.btnCariIndeks = QtWidgets.QPushButton(self.tabCari)
        #self.btnCariIndeks.setDefault(True)
        self.btnCariIndeks.setGeometry(QtCore.QRect(400, 5, 121, 23))
        self.btnCariIndeks.setObjectName("btnCariIndeks")
        self.btnCariFolder = QtWidgets.QPushButton(self.tabCari)
        self.btnCariFolder.setGeometry(QtCore.QRect(400, 36, 121, 23))
        self.btnCariFolder.setObjectName("btnCariFolder")
        self.line = QtWidgets.QFrame(self.tabCari)
        self.line.setGeometry(QtCore.QRect(10, 63, 511, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lstDaftarFile = QtWidgets.QListWidget(self.tabCari)
        self.lstDaftarFile.setGeometry(QtCore.QRect(10, 80, 511, 331))
        self.lstDaftarFile.setObjectName("lstDaftarFile")
        self.lblKeterangan = QtWidgets.QLabel(self.tabCari)
        self.lblKeterangan.setGeometry(QtCore.QRect(11, 420, 200, 13))
        self.lblKeterangan.setObjectName("lblKeterangan")
        self.tabWidget.addTab(self.tabCari, "")
        self.tabFile = QtWidgets.QWidget()
        self.tabFile.setObjectName("tabFile")
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.tabFile)
        self.label_3.setGeometry(QtCore.QRect(10, 62, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tabFile)
        self.label_4.setGeometry(QtCore.QRect(10, 38, 91, 16))
        self.label_4.setObjectName("label_4")
        self.txtFileIndeks = QtWidgets.QLineEdit(self.tabFile)
        self.txtFileIndeks.setGeometry(QtCore.QRect(110, 34, 113, 20))
        self.txtFileIndeks.setReadOnly(True)
        self.txtFileIndeks.setObjectName("txtFileIndeks")
        self.txtFileDirektori = QtWidgets.QLineEdit(self.tabFile)
        self.txtFileDirektori.setGeometry(QtCore.QRect(110, 62, 113, 20))
        self.txtFileDirektori.setReadOnly(True)
        self.txtFileDirektori.setObjectName("txtFileDirektori")
        self.label_5 = QtWidgets.QLabel(self.tabFile)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_5.setObjectName("label_5")
        self.txtDirektoriKerja = QtWidgets.QLineEdit(self.tabFile)
        self.txtDirektoriKerja.setGeometry(QtCore.QRect(110, 8, 411, 20))
        self.txtDirektoriKerja.setReadOnly(True)
        self.txtDirektoriKerja.setObjectName("txtDirektoriKerja")
        self.txtAlamatDir = QtWidgets.QPlainTextEdit(self.tabFile)
        self.txtAlamatDir.setGeometry(QtCore.QRect(110, 90, 411, 141))
        self.txtAlamatDir.setObjectName("txtAlamatDir")
        self.btnBacaFileDir = QtWidgets.QPushButton(self.tabFile)
        self.btnBacaFileDir.setGeometry(QtCore.QRect(240, 60, 141, 23))
        self.btnBacaFileDir.setObjectName("btnBacaFileDir")
        self.chkKunci = QtWidgets.QCheckBox(self.tabFile)
        self.chkKunci.setGeometry(QtCore.QRect(110, 240, 70, 17))
        self.chkKunci.setObjectName("chkKunci")
        self.chkKunci.setChecked(True)
        self.btnSimpan = QtWidgets.QPushButton(self.tabFile)
        self.btnSimpan.setGeometry(QtCore.QRect(446, 240, 75, 23))
        self.btnSimpan.setObjectName("pushButton_4")
        self.btnReIndex = QtWidgets.QPushButton(self.tabFile)
        self.btnReIndex.setGeometry(QtCore.QRect(240, 32, 141, 23))
        self.btnReIndex.setObjectName("btnReIndex")
        self.line2 = QtWidgets.QFrame(self.tabFile)
        self.line2.setGeometry(QtCore.QRect(10, 270, 511, 16))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblWaktuIndeks = QtWidgets.QLabel(self.tabFile)
        self.lblWaktuIndeks.setGeometry(QtCore.QRect(10, 310, 300, 16))
        self.lblWaktuIndeks.setObjectName("lblWaktuIndeks")
        self.lblWaktuDir = QtWidgets.QLabel(self.tabFile)
        self.lblWaktuDir.setGeometry(QtCore.QRect(10, 330, 300, 16))
        self.lblWaktuDir.setObjectName("lblWaktuDir")
        self.lblInfo = QtWidgets.QLabel(self.tabFile)
        self.lblInfo.setGeometry(QtCore.QRect(10, 290, 250, 16))
        self.lblInfo.setObjectName("lblInfo")
        self.tabWidget.addTab(self.tabFile, "")
        self.btnKeluar = QtWidgets.QPushButton(self.centralwidget)
        self.btnKeluar.setGeometry(QtCore.QRect(424, 448, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.btnKeluar.setFont(font)
        self.btnKeluar.setObjectName("btnKeluar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Checkbox kunci frame diklik
        self.chkKunci.stateChanged.connect(self.KunciArea)
        # Keluar aplikasi
        self.btnKeluar.clicked.connect(MainWindow.close)
        # combobox dir dipilih
        self.cboFileDir.currentIndexChanged.connect(self.on_currentIndexChanged_currentIndexChanged)
        self.ListDirektori(self.cboFileDir.currentText())
        # Tombol ReIndes
        self.btnReIndex.clicked.connect(self.ReIndeks)
        # tombol cari - aktivasi
        self.btnCariIndeks.clicked.connect(self.CariBukuIndeks)
        self.txtCari.returnPressed.connect(self.CariBukuIndeks)
        # cari buku dalam direktori
        self.btnCariFolder.clicked.connect(self.cariBukuDirektori)
        # listbox diklik ganda
        self.lstDaftarFile.itemDoubleClicked.connect(self.BukaFile)
        # simpan file direktori
        self.btnSimpan.clicked.connect(self.SimpanDirektori)
        # pemrosesan ekstensi file
        self.DataExtension(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cari Buku - by Galih Hermawan. 10/2021"))
        self.label.setText(_translate("MainWindow", "Cari file :"))
        self.label_2.setText(_translate("MainWindow", "File Direktori :"))
        self.btnCariIndeks.setText(_translate("MainWindow", "Cari di Indeks"))
        self.btnCariFolder.setText(_translate("MainWindow", "Cari di Folder"))
        self.lblKeterangan.setText(_translate("MainWindow", "Info ..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCari), _translate("MainWindow", "Cari"))
        self.label_3.setText(_translate("MainWindow", "Nama file direktori : "))
        self.label_4.setText(_translate("MainWindow", "Nama file indeks :"))
        self.txtFileIndeks.setText(_translate("MainWindow", "indeks.txt"))
        self.txtFileDirektori.setText(_translate("MainWindow", "direktori.txt"))
        self.label_5.setText(_translate("MainWindow", "Direktori kerja :"))
        self.btnBacaFileDir.setText(_translate("MainWindow", "Baca file direktori"))
        self.chkKunci.setText(_translate("MainWindow", "Kunci"))
        self.btnSimpan.setText(_translate("MainWindow", "Simpan"))
        self.btnReIndex.setText(_translate("MainWindow", "Re-Index"))
        self.lblInfo.setText(_translate("MainWindow", "Info ..."))
        #waktuIndeks = time.ctime(os.path.getmtime(MB.almFileIndeks))
        self.lblWaktuIndeks.setText(_translate("MainWindow", "Waktu update file Indeks : "))
        self.lblWaktuDir.setText(_translate("MainWindow", "Waktu update file Direktori : "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFile), _translate("MainWindow", "Manajemen File"))
        self.btnKeluar.setText(_translate("MainWindow", "Keluar"))
        
        # aktivasi kunci frame on load
        self.KunciArea()
        # cek file indeks dan file direktori
        self.CekFile()
        # isi current (direktori kerja) ke line (text) edit
        self.txtDirektoriKerja.setText(_translate("MainWindow", dirKerja))
        # baca isi file direktori.txt        
        isiFileDir = MB.BacaBerkas(MB.almFileDir)
        self.txtAlamatDir.setPlainText("\n".join(isiFileDir))
        # update waktu file indeks n direktori
        self.UpdateWaktu()
        #self.DataExtension()
        
    # comboBox onChange data
    def on_currentIndexChanged_currentIndexChanged(self, index):
        #self.cboFileDir.currentText()
        self.ListDirektori(self.cboFileDir.currentText())
        
    # Kunci area di manajemen File: sebagian komponen
    def KunciArea(self):
        bKunci = self.chkKunci.isChecked()
        #if bkunci:
        self.btnSimpan.setEnabled(not bKunci)
        self.txtAlamatDir.setEnabled(not bKunci)
        #self.txtFileIndeks.setEnabled(not bKunci)
        #self.txtFileDirektori.setEnabled(not bKunci)
    
    def CekFile(self):
        #dirKerja = os.getcwd()
        #MB = ManajemenBerkas(dirKerja)
        cekFileIndeks = MB.PeriksaBerkas(MB.almFileIndeks)
        cekFileDir = MB.PeriksaBerkas(MB.almFileDir)
        
        if not cekFileIndeks:
            self.Pesan(QtWidgets.QMessageBox.Critical, "Kesalahan", "File indeks.txt tidak ditemukan")
            return False
        elif not cekFileDir:
            self.Pesan(QtWidgets.QMessageBox.Critical, "Kesalahan", "File direktori.txt tidak ditemukan")
            return False
        else:
            self.DirKeCbo()
            return True
    
    def DirKeCbo(self):
        cekFileDir = MB.PeriksaBerkas(MB.almFileDir)
        if cekFileDir:
            isiFileDir = MB.BacaBerkas(MB.almFileDir)
            self.cboFileDir.clear()
            # isi list dimasukkan ke comboBox
            self.cboFileDir.addItems(isiFileDir)
            #for i in isiFileDir:
            #    self.cboFileDir.addItems(repr(i))
        else:
            self.Pesan(QtWidgets.QMessageBox.Critical, "Kesalahan", "Pembacaan file direktori gagal.")        
    
    def ListDirektori(self, almDir):
        #almDir = self.txtAlmDirektori.text()
        # jika alamat direktori tidak ditemukan -> error
        if not os.path.exists(almDir):
            return None
        with os.scandir(almDir) as entries:
            self.cboDir.clear()
            # pencarian di root directory
            self.cboDir.addItem(".")
            for entry in entries:
                # jika isi adalah direktori/folder, maka tampilkan
                if entry.is_dir():
                    # masukkdan daftar ke combobox
                    self.cboDir.addItem(entry.name)
                    #print(entry.name)

    # Cari buku - by indeks
    def CariBukuIndeks(self):
        self.lstDaftarFile.clear()
        sCari = self.txtCari.text()
        daftarFileIndeks = MB.BacaBerkas(MB.almFileIndeks)
        # pemrosesan ekstensi
        idxExt = self.cboExtensions.currentIndex()
        lstExtNama, lstExtFiles = self.DataExtension() 
        lstExtCari = lstExtFiles[idxExt]
        #print(idxExt)
        for nmFile in daftarFileIndeks:
            nDir, nFile = os.path.split(nmFile)
            if idxExt != 2: # index 2 untuk semua jenis file 
                if nFile.endswith(lstExtCari):
                    # cari teks pada nama file
                    # namafile dan teks cari di set lowercase
                    posCari = nFile.lower().find(sCari.lower())
                    if posCari != -1:
                        self.lstDaftarFile.addItem(nmFile)
            else:
                posCari = nFile.lower().find(sCari.lower())
                if posCari != -1:
                    self.lstDaftarFile.addItem(nmFile)
                    
        jmlBuku = self.lstDaftarFile.count()
        self.lblKeterangan.setText("Jumlah buku: %s." % jmlBuku)
    
    # Cari buku di folder
    def cariBukuDirektori(self):
        #self.Pesan(QtWidgets.QMessageBox.Critical, "Kesalahan", f"File:\n {almFile} \n\ntidak ditemukan!")
        namaDir = self.cboDir.currentText()
        dirUtama = self.cboFileDir.currentText()
        almDir = os.path.join(dirUtama, namaDir)
        # pemrosesan ekstensi
        idxExt = self.cboExtensions.currentIndex()
        lstExtNama, lstExtFiles = self.DataExtension() 
        lstExtCari = lstExtFiles[idxExt]
        if os.path.isdir(almDir):
            self.lstDaftarFile.clear()
            sCari = self.txtCari.text()
            for dirpath, dirnames, files in os.walk(almDir):
                #print(f'Found directory: {dirpath}')
                for file_name in files:
                    # cari teks pada nama file
                    # namafile dan teks cari di set lowercase
                    if idxExt != 2: # index 2 untuk semua jenis file 
                        if file_name.endswith(lstExtCari):
                            posCari = file_name.lower().find(sCari.lower())
                            if posCari != -1:
                                almFile = os.path.join(dirpath,file_name)
                                self.lstDaftarFile.addItem(almFile)
                    else:
                        posCari = file_name.lower().find(sCari.lower())
                        if posCari != -1:
                            almFile = os.path.join(dirpath,file_name)
                            self.lstDaftarFile.addItem(almFile)

            jmlBuku = self.lstDaftarFile.count()
            self.lblKeterangan.setText("Jumlah buku: %s." % jmlBuku)
        else:
            print("Direktori tidak ditemukan.")
    # buka file
    def BukaFile(self, item):
       # mengambil data pada item yang diklik/double klik
       almFile = item.text()
       if os.path.isfile(almFile):
           # buka sesuai default programnya
           os.startfile(almFile)
       else:
           self.Pesan(QtWidgets.QMessageBox.Critical, "Kesalahan", f"File:\n {almFile} \n\ntidak ditemukan!")

    # melakukan pengindeksan ulang
    def ReIndeks(self):
         # set kursor = menunggu (proses)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.lblInfo.setText("Melakukan pengindeksan ulang...")
        if self.CekFile():
            isiFileDir = MB.BacaBerkas(MB.almFileDir)
            lstFileAll = []
            for alamat in isiFileDir:
                for dirpath, dirnames, files in os.walk(alamat):
                        #print(f'Found directory: {dirpath}')
                        for file_name in files:
                            # gabung alamat direktori dan nama file
                            almFile = os.path.join(dirpath,file_name)
                            lstFileAll.append(almFile)
            # simpan ke file
            MB.TulisBerkas(lstFileAll, MB.almFileIndeks)
            # update waktu file indeks n direktori
            self.UpdateWaktu()
        else:
            self.Pesan(QtWidgets.QMessageBox.Critical, "Kesalahan", "Re-Indeks tidak dapat dilakukan.")
            return None

        # set kursor = normal (panah)
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lblInfo.setText("Pengindeksan ulang telah selesai.")
    
    # Simpan data direktori ke file direktori.txt
    def SimpanDirektori(self):
        #self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        #self.lblInfo.setText("Melakukan pengindeksan ulang...")
        if self.CekFile():
            #isiFileDir = MB.BacaBerkas(MB.almFileDir)
            strDir = self.txtAlamatDir.toPlainText()
            lstDir = strDir.split("\n")
            #print(lstDir)
            # simpan ke file
            MB.TulisBerkas(lstDir, MB.almFileDir)
            # update alamat direktori ke combo box
            self.DirKeCbo()
            # update waktu file indeks n direktori
            self.UpdateWaktu()
        else:
            self.Pesan(QtWidgets.QMessageBox.Critical, "Kesalahan", "Penyimpanan data direktori tidak dapat dilakukan.")
            return None

        # set kursor = normal (panah)
        #self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lblInfo.setText("Penyimpanan alamat direktori telah selesai.")
    
    # pengaturan ekstensi file untuk pencarian
    def DataExtension(self, bUpdate = False):
        lstExtNama = ['Docs 1', 'Docs 2', 'Semua']
        lstExtFiles = [
                ('pdf', 'djvu', 'epub', 'mobi'),
                ('doc','docx', 'xls', 'xlsx', 'ppt', 'pptx'),
                ('*.*',)
            ]
        if bUpdate:
            self.cboExtensions.clear()
            self.cboExtensions.addItems(lstExtNama)
        
        strTooltip = ""
        for i,j in list(zip(lstExtNama, lstExtFiles)):
            strTooltip += f"{i} {str(j)}\n"
        self.cboExtensions.setToolTip(strTooltip)
        return lstExtNama, lstExtFiles
        
    # Update waktu modifikasi file indeks dan direktori .txt
    def UpdateWaktu(self):
        waktuFileIndeks = time.ctime(os.path.getmtime(MB.almFileIndeks))
        waktuFileDirektori = time.ctime(os.path.getmtime(MB.almFileDir))
        self.lblWaktuIndeks.setText(f"Waktu update file Indeks : {waktuFileIndeks}")
        self.lblWaktuDir.setText(f"Waktu update file Direktori : {waktuFileDirektori}")
        
    # message box kustom
    def Pesan(self, ikon, judul, teks):
        kotakPesan = QtWidgets.QMessageBox(ikon, judul, teks)
        kotakPesan.exec()
        
if __name__ == "__main__":
    import sys
    import os
    import time
    from libManajemenBerkas import ManajemenBerkas
    dirKerja = os.getcwd()
    MB = ManajemenBerkas(dirKerja)
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

