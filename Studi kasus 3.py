print("=== NILAI UJIAN MAHASISWA ===")

Batas_nilai = (65,100)

nilai_masuk = []
lulus = []
remedi = []

while True:
    nilai = input("Masukkan nilai: ")

    if nilai == "selesai":
        break

    nilai = int(nilai)

    if nilai >= 0 and nilai <= Batas_nilai[1]:

        nilai_masuk.append(nilai)

        if nilai >= Batas_nilai[0]:
            lulus.append(nilai)
            print("Status: Lulus")
        else:
            remedi.append(nilai)
            print("Status: Remedi")

print("Nilai masuk:", nilai_masuk)

hapus = input("Apakah ada nilai yang salah input? (Iya/tidak): ")

if hapus == "Iya":

    nilai_hapus = int(input("Masukkan nilai yang salah: "))

    if nilai_hapus in nilai_masuk:
        nilai_masuk.remove(nilai_hapus)

        if nilai_hapus in lulus:
            lulus.remove(nilai_hapus)

        if nilai_hapus in remedi:
            remedi.remove(nilai_hapus)

        print("Nilai berhasil dihapus!")
    else:
        print("Nilai tidak ditemukan.")

print("=== HASIL AKHIR ===")
print("Batas nilai:", Batas_nilai)
print("Nilai masuk:", nilai_masuk)
print("Nilai lulus:", lulus)
print("Nilai remedi:", remedi)