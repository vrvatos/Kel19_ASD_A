file_name = "riwayat_transaksi.txt"

def tambah_transaksi():
    print("\n=== INPUT TRANSAKSI BARU ===")

    tanggal = input("Masukkan tanggal transaksi (YYYY-MM-DD): ").strip()
    jenis = input("Masukkan jenis transaksi (pemasukan/pengeluaran): ").strip().lower()
    if jenis not in ['pemasukan', 'pengeluaran']:
        print("Jenis transaksi tidak valid. Harap masukkan 'Pemasukan' atau 'Pengeluaran'.")
        return
    
    try:
        nominal = int(input("Masukkan nominal transaksi: ").strip())
    except:
        print("Nominal harus berupa angka. Transaksi dibatalkan.")
        return
    
    catatan = input("Masukkan catatan (opsional): ").strip()

    with open(file_name, 'a') as file:
        file.write(f"{tanggal},{jenis},{nominal},{catatan}\n")

print("Transaksi berhasil ditambahkan!")

def baca_transaksi():
    transaksi_list = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) >= 4:
                    transaksi_list.append({
                        'tanggal': data[0],
                        'jenis': data[1],
                        'nominal': int(data[2]),
                        'catatan': data[3]
                    })
    except FileNotFoundError:
        print("Belum ada transaksi yang tercatat.")
    return transaksi_list

def menu_tampilan(): #menampilkan riwayat transaksi
    while True: 
        print("\n=== TAMPILKAN RIWAYAT TRANSAKSI ===")
        print("1. Tampilkan Semua Transaksi")
        print("2. Tampilkan Transaksi Berdasarkan Jenis")
        print("3. Tampilkan Urutan Berdasarkan Tanggal")
        print("4. Tampilkan Urutan Berdasarkan Nominal")
        print("5. Kembali ke Menu Utama")
        pilih = input("Pilih opsi (1-5): ").strip()
        data = baca_transaksi()

        if pilih == '1': 
            for d in data:
                print(d["tanggal"], d["jenis"], d["nominal"], d["keterangan"])

        elif pilih == '2': 
            jenis = input("Masukkan jenis (pemasukan/pengeluaran): ").strip().lower()
            for d in data:
                if d["jenis"] == jenis:
                    print(d["tanggal"], d["jenis"], d["nominal"], d["keterangan"])
                        
        elif pilih == '3':  
            data_sorted = sorted(data, key=lambda x: x["tanggal"])
            for d in data_sorted:
                print(d["tanggal"], d["jenis"], d["nominal"], d["keterangan"]) 

        elif pilih == '4':
            data_sorted = sorted(data, key=lambda x: x["nominal"])
            for d in data_sorted:
                print(d["tanggal"], d["jenis"], d["nominal"], d["keterangan"])

        elif pilih == '5':
            break
        else:
            print("Opsi tidak valid. Silakan pilih antara 1-5.") 

def cek_saldo():
    data = baca_transaksi()
    saldo = 0
    
    for d in data:
        if d["jenis"] == "pemasukan":
            saldo += d["nominal"]
        else:
            saldo -= d["nominal"]
    
    print(f"\nTotal Saldo Saat Ini: {saldo}")   

def main():
    while True:
        print("\n=== APLIKASI RIWAYAT KEUANGAN ===")
        print("1. Input Transaksi Baru")
        print("2. Tampilkan Riwayat")
        print("3. Cek Total Saldo")
        print("4. Keluar")
        
        pilihan = input("Pilih Menu: ")
        if pilihan == '1':
            tambah_transaksi()
        elif pilihan == '2': 
            menu_tampilan()
        elif pilihan == '3': 
            cek_saldo()
        elif pilihan == '4':
            print("Sistem Berhenti. Data Anda aman di 'riwayat_transaksi.txt'")
            break

if __name__ == "_main_":
    main()