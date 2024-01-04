#KONEKSI DB
import sqlite3
conn = sqlite3.connect('database_hewan2.db')
cursor = conn.cursor()

jenis = Mamalia
cursor.execute("DELETE FROM HEWAN WHERE jenis = ?", (jenis,))
conn.commit()

if cursor.rowcount > 0:
    print(f"Data hewan dengan jenis {jenis} berhasil dihapus.")
else:
    print(f"Tidak ada data hewan dengan jenis {jenis}.")

conn.close()
