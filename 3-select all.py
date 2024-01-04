#KONEKSI DB
import sqlite3
koneksi = sqlite3.connect('database_hewan2.db')
kursor = koneksi.cursor()


kursor.execute("SELECT * FROM HEWAN")
baris_tabel = kursor.fetchall()

print("database hewan:")
print("="*129)
print("{:<21} {:<20} {:<20} {:<20} {:<20} {:<20}".format("id_hewan", "nama_hewan", "jenis", "asal", "jml_skrng", "thn_ditemukan"))
print("="*129)
for baris in baris_tabel:
   print("{:<21} {:<20} {:<20} {:<20} {:<20} {:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))
print("="*129)

koneksi.close()
