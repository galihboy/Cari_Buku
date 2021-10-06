## Cari Buku
###### Developed by [Galih Hermawan](https://galih.eu).
---

Aplikasi ini digunakan untuk mencari dokumen digital (makalah, ebooks, dan berkas lain). Tadinya saya buat untuk menggantikan aplikasi pencarian buku lama yang masih menggunakan [VB6](https://github.com/galihboy/vb6-pencari-file).

**Requirements:**
- python 3.8
- pyqt 5.9.2

**Berkas penyimpanan:**
- direktori.txt : alamat direktori yang akan diindeks
- indeks.txt :  menyimpan semua alamat file yang ada dalam folder di file direktori.txt

**Terdapat 2 area (tab), meliputi:**
1. Cari
	- Mencari buku dalam file indeks
	- Mencari buku dalam folder secara langsung (real time)
	- Terdapat combobox untuk pilihan jenis file. Saat ini dibuat hardcode, dimana:
		```
		Docs 1 : pdf, djvu, epub, mobi
		Docs 2 : doc, docx, xls, xlsx, ppt, pptx
		Semua  : mencakup semua jenis file
		```
	- Terdapat combobox untuk menampilkan Folder yang sudah disimpan di file direktori.txt, serta terdapat juga pilihan sub folder di dalam direktori tersebut
	- ListBox digunakan untuk menampilkan daftar file hasil pencarian, dan dapat diklik ganda untuk dapat membuka file di program defalult-nya
	
2. Manajemen File
	- Menampilkan (line edit / text box) read-only yang meliputi: current directory (direktori aplikasi), nama file: indeks.txt dan direktori.txt
	- Dapat memperbarui  isi file direktori.txt secara langsung. Buka kunci (uncheck) dan tekan tombol Simpan
	- Dapat melakukan pengindeksan ulang (biasanya setelah update data direktori)
 
Screenshot program untuk tab Cari.
![Cari buku](/screenshot_1.jpg)

Screenshot program untuk tab Manajemen File.
![Manajemen file](/screenshot_2.jpg)

**Tips:**
- File python ini dapat dieksekusi secara langsung di sistem operasi Windows melalui perintah di file .bat (batch files)
- Caranya adalah:
	1. buat file baru dengan ekstensi .bat di notepad
	2. isi dengan:
		> cd /d "D:\PythonKu\gui\Cari_Buku"
		> start "" C:\Users\galih-hermawan\anaconda3\pythonw CariBuku.py
		
	3. Baris pertama memuat direktori dimana source code file python kita berada. Punya saya contohnya: "D:\PythonKu\gui\Cari_Buku"
	4. Baris kedua memuat alamat file pythonw.exe (sesuaikan, baik itu versi standalone atau anaconda), kemudian tambahkan nama file (source code). Punya saya contohnya: CariBuku.py
- File .bat tadi dapat diberi nama apapun, misal. CariBuku.bat
- Buat shortcut-nya , dan taruh di desktop
- Selesai