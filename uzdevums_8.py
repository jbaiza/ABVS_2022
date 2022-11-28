# Lietotāja ievadītam skaitlim, kas reprezentē diennakts stundu (0-23) izvadīt stundai atbilstošu sveicienu. No 6 līdz 11 - "Labrīt!", no 12 līdz 16 - "Labdien!", no 17 līdz 22 - "Labvakar!", no 23 līdz 5 - "Laiks gulēt!".
print("Ievadiet cik pulkstens rada? No 0 lidz 23 : ")
num_1 = int(input())
a = num_1
if (num_1) >= 0 and (num_1) <= 23:
    print()
else:
    print(" Nepareizi ievadits skaitlis, ludzu meiginiet velreiz")


if num_1 >= 6 and num_1 <=11:
    print("Labrīt!")
elif num_1 >=12 and num_1 <=16:
    print("Labdien!")
elif num_1 >=17 and num_1 <=22:
    print("Labvakar!")
elif num_1 := 23 and (0,1,2,3,4,5):
    print("Laiks gulet!")