import os

def cetak_pilihan():
    print("Pilihan menu: ")
    print("'cf'")
    print("'cr'")
    print("'ck'")
    print("'fc'")
    print("'rc'")
    print("'kc'")
    print("'fr'")
    print("'fk'")
    print("'rf'")
    print("'kf'")
    print("'rk'")
    print("'kr'")

    print("'q untuk keluar dari program")


def celcius_ke_fanrehit(suhu_c):
    return float(9.0 / 5.0 * suhu_c + 32)


def celcius_ke_reamur(suhu_c):
    return float(9.0 / 5.0 * suhu_c)


def celcius_ke_kelvin(suhu_c):
    return float(suhu_c + 273)


def fanrehit_ke_celcius(suhu_f):
    return float(5.0 / 9.0 * (suhu_f - 32))


def fanrehit_ke_kelvin(suhu_f):
    return float((suhu_f + 459.67) * 5.0 / 9.0)


def fanrehit_ke_reamur(suhu_f):
    return float(4.0 / 9.0 * (suhu_f - 32))


def reamur_ke_celcius(suhu_r):
    return float(5.0 / 4.0 * suhu_r)


def reamur_ke_fanrehit(suhu_r):
    return float(9.0 / 4.0 * (suhu_r + 32))


def reamur_ke_kelvinya(suhu_r):
    return float(5.0 / 4.0 * (suhu_r + 273))


def kelvin_ke_celcius(suhu_k):
    return float(suhu_k - 273)


def kelvin_ke_reamur(suhu_k):
    return float(4.0 / 5.0 * (suhu_k - 273))


def kelvin_ke_fanrehit(suhu_k):
    return float(9.0 / 5.0 * (suhu_k - 273)) + 32


error = False
pilihan = None
while not error:
    os.system("cls")
    cetak_pilihan()
    pilihan = input("pilihan : ")
    if pilihan == 'cf':
        main_c = float(input("suhu celciusnya : "))
        result = celcius_ke_fanrehit(main_c)
        print(f"Fanrehit : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'cr':
        main_c = float(input("suhu celciusnya : "))
        result = celcius_ke_reamur(main_c)
        print(f"reamur : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'ck':
        main_c = float(input("suhu celciusnya : "))
        result = celcius_ke_kelvin(main_c)
        print(f"kelvin : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'fc':
        main_f = float(input("suhu fanrehitnya : "))
        result = fanrehit_ke_celcius(main_f)
        print(f"celcius : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'rc':
        main_r = float(input("suhu reamurnya : "))
        result = reamur_ke_celcius(main_r)
        print(f"celcius : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'kc':
        main_k = float(input("suhu kelvinnya : "))
        result = kelvin_ke_celcius(main_k)
        print(f"celcius : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'fr':
        main_f = float(input("suhu fanrehitnya : "))
        result = fanrehit_ke_reamur(main_f)
        print(f"reamur : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'fk':
        main_f = float(input("suhu fanrehitnya : "))
        result = fanrehit_ke_kelvin(main_f)
        print(f"kelvin : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'rf':
        main_r = float(input("suhu reamurnya : "))
        result = reamur_ke_fanrehit(main_r)
        print(f"Fanrehit : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'kf':
        main_k = float(input("suhu kelvinnya : "))
        result = celcius_ke_fanrehit(main_k)
        print(f"Fanrehit : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'rk':
        main_r = float(input("suhu reamurnya : "))
        result = reamur_ke_kelvinya(main_r)
        print(f"kelvin : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'kr':
        main_k = float(input("suhu kelvinnya : "))
        result = kelvin_ke_reamur(main_k)
        print(f"reamur : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'kf':
        main_k = float(input("suhu kelvinnya : "))
        result = kelvin_ke_fanrehit(main_k)
        print(f"fanrehit : {result}")
        input("tekan Enter untuk kembali ke menu semula")
    elif pilihan == 'q':
        error = True


print("Ok thats the end im tired")