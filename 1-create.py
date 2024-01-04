#KOONEKSI
import sqlite3
koneksi = sqlite3.connect('database_hewan2.db')

#buat data base dan table hewan
koneksi.execute('''
                CREATE TABLE HEWAN(
                id_hewan INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_hewan VARCHAR(50),
                jenis VARCHAR(50),
                asal VARCHAR(50),
                jml_skrng INTEGER(50),
                thn_ditemukan INTEGER(50)
                )
                ''')
koneksi.close()