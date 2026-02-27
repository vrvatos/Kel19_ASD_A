def menu_tampilan(): #menampilkan riwayat transaksi
    while True: 
        print("\n=== TAMPILKAN RIWAYAT TRANSAKSI ===")
        print("1. Tampilkan Semua Transaksi")
        print("2. Tampilkan Transaksi Berdasarkan Jenis")
        print("3. Tampilkan Urutan Berdasarkan Tanggal")
        print("4. Tampilkan Urutan Berdasarkan Nominal")
        print("5. Kembali ke Menu Utama")
        pilih = input("Pilih opsi (1-5): ").strip()

        if pilih == '1':
            
        elif pilih == '2':
            
        elif pilih == '3':
            
        elif pilih == '4':

        elif pilih == '5':
            break
        else:
            print("Opsi tidak valid. Silakan pilih antara 1-5.")    

def main():
    while True:
        print("\n=== APLIKASI RIWAYAT KEUANGAN ===")
        print("1. Input Transaksi Baru")
        print("2. Tampilkan Riwayat")
        print("3. Cek Total Saldo")
        print("4. Keluar")
        
        pilihan = input("Pilih Menu: ")
        if pilihan == '1': tambah_transaksi()
        elif pilihan == '2': menu_tampilkan()
        elif pilihan == '3':
        elif pilihan == '4':
            print("Sistem Berhenti. Data Anda aman di 'riwayat_transaksi.txt'")
            break

if _name_ == "_main_":
    main()