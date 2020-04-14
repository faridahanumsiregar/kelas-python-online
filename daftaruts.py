# program untuk menyaring murid yang boleh ikut uts

daftar_murid = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(daftar_murid)
tidak_boleh_uts = []
boleh_uts = []

# use loop
for siswa in daftar_murid:
    if siswa%2 == 0:
        boleh_uts.append(siswa)
    else:
        print(siswa, "tidak boleh ikut uts")
        tidak_boleh_uts.append(siswa)

print("boleh uts", boleh_uts)
print("tidak boleh uts", tidak_boleh_uts)
print("daftar murid", daftar_murid)
