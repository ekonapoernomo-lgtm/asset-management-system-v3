from asset import(
    cari_aset,
    tampilkan_aset,
    tambah_aset,
    update_aset,
    hapus_aset
)

while True:
    print("\n--- ASET MANAJEMEN V.3 ---")
    print("1. Tambah Aset")
    print("2. Tampilkan Aset")
    print("3. Update Aset")
    print("4. Hapus Aset")
    print("5. Cari Aset")
    print("0. Keluar")
    pilihan = input("\nSilakan pilih menu (1-5): ")
    if pilihan == "1":
        tambah_aset()
    elif pilihan == "2":
        tampilkan_aset()
    elif pilihan == "3":
        update_aset()
    elif pilihan == "4":
        hapus_aset()
    elif pilihan == "5":
        cari_aset()
    elif pilihan == "0":
        print("Terima kasih.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
