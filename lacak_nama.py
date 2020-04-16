# BPS punya data nama penduduk
# masalahnya, mereka lupa buat minta data
# suku dari penduduk tersebut

# kita disuruh untuk buat program
# yang bisa membedakan suku dari nama

# contoh: Diki Situmorang
# medan, sumut -> Sinaga, Siregar
# depan -> su, belakang -> o -> jawa
# jawa, medan

# <nama depan> + <nama belakang>
# haswanto -> h a s w a n t o
#                          ---
# -----------------------------
# dari Jawa

# kalau tidak ditemukan pola diatas
# cari di nama belakang
# Situmorang -> s i t u m o r a n g
# s+i 
# ------------------------------
# dari SUMUT

nama = ["Hazmi Wiranto", "Haswanto", "Farida Siregar"]

# nama ke-i di daftar nama
# cek nama depan
# kalau ada o di nama depan -> dari Jawa
# kalau ada si di nama belakang -> dari SUMUT

# 1. list
# 2. fungsi/def
# 3. string
# 4. loop 

# def -> agar operasi general untuk data apapun
# deteksi_nama("Hazim Sinaga")
# deteksi_nama("Purwo Dinoto")

def deteksi_nama(nama):
    # Hadi Sinaga
    nama = nama.lower()
    
    pjg = nama.split(" ")
    if len(pjg) == 2:
        nd, nb = nama.split(" ")

        if nd.endswith("o") == True:
            return "Jawa"
        elif nb.startswith("si") == True:
            return "SUMUT"
        else:
            return None
    return None

import csv
f = open("cleaned-data.csv")
reader = csv.reader(f)
for i in reader:
    nama = i[0]
    """
    asal = deteksi_nama(nama)
    if asal != None:
        print(nama, asal)
    """
    print(i)
