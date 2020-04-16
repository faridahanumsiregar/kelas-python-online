import csv
f = open("cleaned-data.csv")
reader = csv.reader(f)
for baris in reader:
	print(baris)

