import csv
f = open("kelas-online.csv")
reader = csv.reader(f)
for baris in reader:
	print(baris)

