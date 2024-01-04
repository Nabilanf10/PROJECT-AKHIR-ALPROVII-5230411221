#KONEKSI DB
import sqlite3
conn = sqlite3.connect('database_hewan2.db')
cursor = conn.cursor()

id_hewan = 3
asal = 'Nusa Tenggara Timur'

cursor.execute(f"UPDATE HEWAN SET asal = 'asal' WHERE id_hewan = {id_hewan}")
conn.commit

if cursor.rowcount > 0:
   print(f"Data hewan dengan ID{id_hewan} berhasil diupdate.")
else:
   print(f"Tidak ada data pegawai dengan ID {id_hewan}.")
   
conn.close()
