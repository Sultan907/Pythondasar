Kondisi = True

def ngulang():
    if nilai >= 75:
        print("Siswa tuntas.")
    else:
        print("Tidak tuntas.")

while Kondisi:
    nilai = float(input("Masukkan nilai siswa: "))
    if nilai >= 75:
        print("Siswa Tuntas.")
        break
    else:
        ui = input("Ingin Mengulang (Ya/Tidak)? : ")
        if ui.lower() == "ya": 
            ngulang()
        else:
            print("Tidak Tuntas.")
            break
