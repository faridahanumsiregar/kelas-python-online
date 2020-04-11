keranjang1 = ["melon", "durian", "manggis", "duku", "mangga"]

while True:
    cek = input("> masukkan nama buah: ")
    
    if cek in keranjang1:
        print(cek, "ada di keranjang")
        continue
    else:
        print(cek, "tidak ada di keranjang")
        print("memasukkan", cek, "di keranjang")
        keranjang1.append(cek)
        print(cek, "telah dimasukkan di keranjang")
        print("jumlah buah di keranjang", len(keranjang1))
        print(keranjang1)
