import os
from datetime import datetime

FILE_NAME = "riwayat_duid.txt"

# ─────────────────────────────────────────
# fungsi untuk baca dan simpan transaksi
# ─────────────────────────────────────────

def baca_transaksi():
    """Baca semua transaksi dari file. Return list of dict."""
    transaksi = []
    if not os.path.exists(FILE_NAME):
        return transaksi
    with open(FILE_NAME, "r") as f:
        for baris in f:
            baris = baris.strip()
            if not baris:
                continue
            bagian = baris.split(",")
            if len(bagian) < 5:
                continue
            transaksi.append({
                "tanggal": bagian[0],
                "nama"   : bagian[1],
                "rek"    : bagian[2],
                "nominal": bagian[3],
                "bank"   : bagian[4],
                "jenis"  : bagian[5] if len(bagian) > 5 else "-"
            })
    return transaksi


def simpan_transaksi(data: dict):
    """Tambah satu baris transaksi ke file."""
    with open(FILE_NAME, "a") as f:
        f.write(
            f"{data['tanggal']},{data['nama']},{data['rek']},"
            f"{data['nominal']},{data['bank']},{data['jenis']}\n"
        )


# ─────────────────────────────────────────
# tampilan tabel
# ─────────────────────────────────────────

def cetak_header():
    print(f"\n{'No':<4} {'Tanggal':<20} {'Nama':<15} {'No. Rek':<16} "
          f"{'Nominal':>14} {'Bank':<10} {'Jenis'}")
    print("─" * 85)


def cetak_baris(i, t):
    try:
        nominal_fmt = f"Rp {int(float(t['nominal'])):>12,}"
    except ValueError:
        nominal_fmt = f"{'??':>14}"
    print(f"{i:<4} {t['tanggal']:<20} {t['nama']:<15} {t['rek']:<16} "
          f"{nominal_fmt} {t['bank']:<10} {t['jenis']}")


def cetak_tabel(data):
    if not data:
        print("  (Tidak ada data.)")
        return
    cetak_header()
    for i, t in enumerate(data, 1):
        cetak_baris(i, t)


JENIS_VALID = {
    "1": "Transfer",
    "2": "Pembayaran"
}

# Semua transaksi dihitung sebagai pengeluaran
JENIS_KELUAR = {"Transfer", "Pembayaran"}


# ─────────────────────────────────────────
# FITUR UTAMA
# ─────────────────────────────────────────

def tambah_transaksi():
    print("\n=== INPUT TRANSAKSI BARU ===")
    nama    = input("Nama pemilik rekening : ").strip()
    while True:
        rek = input("Nomor rekening        : ").strip()
        if rek.isdigit() and len(rek) == 10:
            break
        print("  Nomor rekening harus tepat 10 digit angka.")
    bank    = input("Nama bank             : ").strip()

    while True:
        try:
            nominal = float(input("Nominal (Rp)          : ").replace(",", "").replace(".", ""))
            if nominal <= 0:
                print("  Nominal harus lebih dari 0.")
                continue
            break
        except ValueError:
            print("  Input tidak valid, masukkan angka.")

    print("\nJenis Transaksi:")
    for k, v in JENIS_VALID.items():
        print(f"  {k}. {v}")
    while True:
        pilih_jenis = input("Pilih jenis (1-2): ").strip()
        if pilih_jenis in JENIS_VALID:
            jenis = JENIS_VALID[pilih_jenis]
            break
        print("  Pilihan tidak valid.")

    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "tanggal": tanggal,
        "nama"   : nama,
        "rek"    : rek,
        "nominal": str(int(nominal)),
        "bank"   : bank,
        "jenis"  : jenis
    }
    simpan_transaksi(data)
    print(f"\n✓ Transaksi '{jenis}' sebesar Rp {int(nominal):,} berhasil disimpan.")


def cek_saldo():
    print("\n=== CEK TOTAL PENGELUARAN ===")
    data = baca_transaksi()
    if not data:
        print("Belum ada transaksi.")
        return

    per_jenis = {}
    for t in data:
        jenis = t['jenis']
        per_jenis[jenis] = per_jenis.get(jenis, 0) + float(t['nominal'])

    total = sum(per_jenis.values())

    for jenis, jumlah in per_jenis.items():
        print(f"  {jenis:<15}: Rp {jumlah:>15,.0f}")
    print(f"  {'─' * 35}")
    print(f"  {'Total Keluar':<15}: Rp {total:>15,.0f}")


# ─────────────────────────────────────────
# MENU TAMPILAN
# ─────────────────────────────────────────

def menu_tampilan():
    while True:
        print("\n=== TAMPILKAN RIWAYAT TRANSAKSI ===")
        print("1. Tampilkan Semua Transaksi")
        print("2. Tampilkan Transaksi Berdasarkan Jenis")
        print("3. Tampilkan Urutan Berdasarkan Tanggal")
        print("4. Tampilkan Urutan Berdasarkan Nominal")
        print("5. Kembali ke Menu Utama")
        pilih = input("Pilih opsi (1-5): ").strip()
        data  = baca_transaksi()

        if pilih == '1':
            print("\n─── Semua Transaksi ───")
            cetak_tabel(data)

        elif pilih == '2':
            print("\nJenis yang tersedia: Transfer | Pembayaran")
            cari = input("Masukkan jenis      : ").strip().lower()
            hasil = [t for t in data if t['jenis'].lower() == cari]
            print(f"\n─── Transaksi Jenis '{cari.title()}' ───")
            cetak_tabel(hasil)

        elif pilih == '3':
            urutan = sorted(data, key=lambda x: x['tanggal'])
            print("\n─── Urutan Berdasarkan Tanggal (Terlama → Terbaru) ───")
            cetak_tabel(urutan)

        elif pilih == '4':
            try:
                urutan = sorted(data, key=lambda x: float(x['nominal']), reverse=True)
            except ValueError:
                urutan = data
            print("\n─── Urutan Berdasarkan Nominal (Terbesar → Terkecil) ───")
            cetak_tabel(urutan)

        elif pilih == '5':
            break

        else:
            print("Opsi tidak valid. Silakan pilih antara 1-5.")


# ─────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────

def main():
    while True:
        print("\n=== APLIKASI RIWAYAT KEUANGAN ===")
        print("1. Input Transaksi Baru")
        print("2. Tampilkan Riwayat")
        print("3. Cek Total Saldo")
        print("4. Keluar")

        pilihan = input("Pilih Menu: ").strip()
        if pilihan == '1':
            tambah_transaksi()
        elif pilihan == '2':
            menu_tampilan()
        elif pilihan == '3':
            cek_saldo()
        elif pilihan == '4':
            print("Sistem Berhenti. Data Anda aman di 'riwayat_duid.txt'")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 1-4.")


if __name__ == "__main__":
    main()