#=======================================================================================
# Tugas KELOMPOK
# Judul : Riwayat Rekening BANK
# 
# Kelompok  : 19
# NIM       : 003, 004, 017 
# Kelas     : A
#=======================================================================================

#---------------------------------------------------------------------------------------
# Fungsi Tambahan Untuk Tampilan
#---------------------------------------------------------------------------------------

def garis(panjang = 50):
    print("=" * panjang)

def garis_tipis(panjang = 50):
    print("=" * panjang)

#---------------------------------------------------------------------------------------
# Fungsi 1 : Membaca Data dari File
#---------------------------------------------------------------------------------------

nama_file = "riwayat_duid.txt"
'''
Membaca data stok dari file text
Dengan Format : nama, no rek, nominal, bank
'''
def liat_riwayat(nama_file):
    riwayat_dict = {}

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for baris in file:
                baris = baris.strip()
                if baris == "":
                    continue

                nama, no_rek, nominal, bank = baris.split(",")

                riwayat_dict[no_rek] = {
                    "nama": nama,
                    "no_rek": no_rek,
                    "nominal": int(nominal),
                    "bank": bank
                }

    except FileNotFoundError:
        pass

    return riwayat_dict

#---------------------------------------------------------------------------------------
# Fungsi 2 : Menyimpan Data ke File
#---------------------------------------------------------------------------------------

def simpan_duid(nama_file, riwayat_dict):
    with open(nama_file, "w", encoding="utf-8") as file: # Membuka file dalam mode write ("w") -> menimpa isi file lama
        for kode in sorted(riwayat_dict.keys()):
            nama = riwayat_dict[kode]["nama"]
            nominal = riwayat_dict[kode]["nominal"]
            file.write(f"{nama}, {no_rek}, {nominal}\n") # Menulis data ke file sesuai format yang ditentukan

#---------------------------------------------------------------------------------------
# Fungsi 3 : Menampilkan semua data dari File
#---------------------------------------------------------------------------------------

def tampilkan_duid(riwayat_dict):
    if len(riwayat_dict) == 0:
        garis()
        print("gada duid 😔")
        garis()
        return

    garis()
    print("📑 Riwayat Rekening")
    garis()

    print(f"{'Nama':<12} | {'No Rekening':<20} | {'Nominal':>10} | {'Bank':<10}")
    garis_tipis()

    for no_rek in riwayat_dict:
        data = riwayat_dict[no_rek]
        print(f"{data['nama']:<12} | {data['no_rek']:<20} | {data['nominal']:>10} | {data['bank']:<10}")

    garis()

#---------------------------------------------------------------------------------------
# Fungsi 4 : Memcari Barang Berdasarkan Kode
#---------------------------------------------------------------------------------------

def cari_rek(riwayat_dict):
    garis()
    print("🔍 CARI REKENING")
    garis()

    no_rek = input("Masukkan No Rek : ").strip()

    if no_rek in riwayat_dict:
        data = riwayat_dict[no_rek]

        garis()
        print("rekening ada")
        garis()
        print(f"Nama    : {data['nama']}")
        print(f"No Rek  : {data['no_rek']}")
        print(f"Nominal : {data['nominal']}")
        print(f"Bank    : {data['bank']}")
        garis()
    else:
        garis()
        print("no rek tidak ada")
        garis()

#---------------------------------------------------------------------------------------
# Fungsi 5 : Fitur Menambah Barang Baru
#---------------------------------------------------------------------------------------

def tambah_rek(riwayat_dict):
    garis()
    print("➕ Tambah Rek Baru")
    garis()

    kode = input("Masukkan NO Rek Baru : ").strip()

    if kode in riwayat_dict: # kode tidak boleh sama dengan yg sudah ada
        print("⚠️ Rekening Sudah Ada . Tambah Rek dibatalkan.")
        garis()
        return

    nama = input("Masukkan rek: ").strip()

    try:
        duid_tf = int(input("Masukkan rekl : ").strip())
    except ValueError:
        print("⚠️ rek harus angka")
        garis()
        return

    if duid_tf < 0:
        print("⚠️ jangan ngutang.")
        garis()
        return

    riwayat_dict[kode] = {"nama" : nama, "no_rek" : tambah_rek} # menyimpan barang baru ke dictionary
    print("✅ tambah norek berhasil")
    garis()

#---------------------------------------------------------------------------------------
# Fungsi 6 : sistem update
#---------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------
# Program Utama
#---------------------------------------------------------------------------------------

def main():
    stok_barang = liat_riwayat(nama_file)

    while True:
        garis()
        print("🏪 Sistem riwayar rekening bank")
        garis()
        print("[1] Tampilkan semua riwayat")
        print("[2] Cari rekening")
        print("[3] Tambah rekening baru")
        print("[4]")
        print("[5]")
        print("[0] Keluar")
        garis_tipis()

        pilihan = input("Pilih menu: ").strip() # membaca data stok dari filr saat program dimulai

        if pilihan == "1":
            tampilkan_duid(stok_barang)

        elif pilihan == "2":
            cari_rek(stok_barang)

        elif pilihan == "3":
            tambah_rek(stok_barang)

        elif pilihan == "4":
            #update_stok(stok_barang)
            print("⚠️  Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan == "5":
            #simpan_stok(nama_file, stok_barang)
            #garis()
            #print("💾 Data berhasil disimpan ke file!")
            #garis()
            print("⚠️  Pilihan tidak valid. Silakan coba lagi.")

        elif pilihan == "0":
            garis()
            print("👋 Program selesai. Terima kasih!")
            garis()
            break

        else:
            print("⚠️  Pilihan tidak valid. Silakan coba lagi.")

# menjalankan program utama
if __name__ == "__main__":
    main()