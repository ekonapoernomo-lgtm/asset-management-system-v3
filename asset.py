from db import(
    tampilkan_aset_db,
    tambah_aset_db,
    update_aset_db,
    hapus_aset_db,
    cari_aset_by_kode,
    cari_aset_db
)

def tampilkan_aset():
    data = tampilkan_aset_db()
    if len(data) == 0:
        print("Belum ada data set")
        return
    print("\n--- DAFTAR ASET ---")
    nomor = 1
    for item in data:
        print(f"\nAset ke-{nomor}:")
        print("Kode      : ", item[1])
        print("Nama      : ", item[2])
        print("Lokasi    : ", item[3])
        print("Kondisi   : ", item[4])
        nomor += 1

def tambah_aset():
    kode = input("Kode Aset     : ")
    if cari_aset_by_kode(kode):
        print("Kode aset sudah digunakan. Silakan gunakan kode aset lain!.")
        return
    nama = input("Nama Aset     : ")
    lokasi = input("Lokasi Aset   : ")
    kondisi = input("Kondisi Aset  : ")
    tambah_aset_db(kode, nama,  lokasi, kondisi)
    print("Aset berhasil ditambahkan!")

def update_aset():
    kode = input("Masukkan kode aset : ")
    kondisi_baru = input("Masukkan kondisi baru : ")
    update_aset_db(kode, kondisi_baru)
    print("Data berhasil diperbarui!")

def hapus_aset():
    kode = input("Masukkan kode aset yang ingin dihapus : ")
    hapus_aset_db(kode)
    print("Data berhasil dihapus.")

def cari_aset():
    keyword = input("Masukkan kode/nama aset : ")
    hasil = cari_aset_db(keyword)
    if not hasil:
        print("Data tidak ditemukan.")
        return
    for item in hasil:
        print(f"\nKode     : ", item[1])
        print(f"\nNama     : ", item[2])
        print(f"\nLokasi   : ", item[3])
        print(f"\nKondisi  : ", item[4])
