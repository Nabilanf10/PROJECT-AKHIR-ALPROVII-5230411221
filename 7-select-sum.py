import sqlite3

conn = sqlite3.connect('database_hewan2.db')
cursor = conn.cursor()

cursor.execute("SELECT SUM(jml_skrng) FROM HEWAN")
jml_skrng = cursor.fetchone()[0]

print(f"Total Populasi Hewan Saat Ini: {jml_skrng}")

conn.close