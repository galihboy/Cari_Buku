# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 06:11:45 2021

@author: galih-hermawan
Repository: https://github.com/galihboy/
Web: https://galih.eu
"""

import os

class ManajemenBerkas:
    def __init__(self, namaDirektori):
        # direktori = os.getcwd()
        # gabung path = 
        self.namaDirektori = namaDirektori
        self.almFileIndeks = os.path.join(namaDirektori, "indeks.txt")
        self.almFileDir = os.path.join(namaDirektori, "direktori.txt")
        
    def PeriksaBerkas(self, namaFile):
        # periksa apakah file valid
        if os.path.isfile(namaFile):
            return True
        else:
            try:
                file1 = open(namaFile, "r", encoding='utf-8')
                file1.closed()
            except FileNotFoundError:
                print(f"Berkas {namaFile} tidak ditemukan.")
                return False
            except OSError:
                print(f"Terdapat kesalahan OS saat membuka file {namaFile}")
                return False
            except Exception as err:
                print(f"Terdapat kesalahan tak terduga saat membuka file {namaFile} - ",repr(err))
                return False                
            else:
                return True
    
    # periksa keberadaan direktori
    def CekDirektoriValid(self, namaDirektori):
        return os.path.isdir(namaDirektori)
    
    # membersihkan list dari empty string/values
    def BersihkanEmptyList(self, daftar):
        return [x for x in daftar if x]
    
    # membaca isi file dan dikembalikan dalam bentuk list
    def BacaBerkas(self, namaFile):
        statusFile = self.PeriksaBerkas(namaFile)
        isi = []
        if statusFile:
            file1 = open(namaFile, "r", encoding='utf-8')
            with file1:
                # pisah data file per baris dan hapus data kosong
                isi = file1.read().strip().split("\n")
        
            file1.close()  
        return self.BersihkanEmptyList(isi)
    
    def TulisBerkas(self, listData, namaFile):
        statusFile = self.PeriksaBerkas(namaFile)
        if statusFile:
            file1 = open(namaFile, "w", encoding='utf-8')
            with file1:    
                for d in listData:
                    file1.write(d + "\n")
            file1.close()
    
    def TambahDataBerkas(self, barisData, namaFile):
        statusFile = self.PeriksaBerkas(namaFile)
        if statusFile:
            file1 = open(namaFile, "a", encoding='utf-8')
            with file1:    
                file1.write("\n" + barisData)
            file1.close()  
            self.RapikanBerkas()
        #return self.BersihkanEmptyList(isi)

    # baca file, bersihkan empty values, tulis ulang
    def RapikanBerkas(self, namaFile):
        statusFile = self.PeriksaBerkas(namaFile)
        isiBerkas = self.BacaBerkas(namaFile)
        if statusFile:
            file1 = open(namaFile, "w", encoding='utf-8')
            with file1:
                # pisah data file per baris dan hapus data kosong
                for data in isiBerkas:
                    file1.write(data + "\n")
        
            file1.close()  