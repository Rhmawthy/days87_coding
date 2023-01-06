angka = int(input("masukkan angka :"))

if angka %2 == 0 :
	k = [h for h in range (2,angka+1,2)]
	print(k[: : -1])
	
elif angka %2 != 0 :
	j = [b for b in range (1,angka+2, 2)]
	print(j)
