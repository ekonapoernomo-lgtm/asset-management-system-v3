import sqlite3

DB_NAME = "asset.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def tampilkan_aset_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aset")
    data = cursor.fetchall()
    conn.close()
    return data

def tambah_aset_db(kode, nama, lokasi, kondisi):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO aset (kode, nama, lokasi, kondisi) VALUES (?, ?, ?, ?)""", 
                   (kode, nama, lokasi, kondisi))
    conn.commit()
    conn.close()

def update_aset_db(kode, kondisi_baru):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE aset SET kondisi = ? WHERE kode = ?""", (kondisi_baru, kode))
    conn.commit()
    conn.close()

def hapus_aset_db(kode):
    conn =  get_connection()
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM aset WHERE kode = ?""", (kode,))
    conn.commit()
    conn.close()

def cari_aset_by_kode(kode):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM aset WHERE kode = ?""", (kode,))
    data = cursor.fetchone()
    conn.close()
    return data

def cari_aset_db(keyword):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM aset WHERE kode LIKE ? OR nama LIKE ? """,
                   (f"%{keyword}%", f"%{keyword}%"))
    data = cursor.fetchall()
    conn.close()
    return data