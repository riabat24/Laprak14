data = "Januari Februari Maret April Mei Juni "
bulan = data.split()
print()

list_set = set(bulan)
print("Konversi List menjadi Set")
print("Sebelum Konversi: ", bulan)
print("Sesudah Konversi: ", list_set)
print()

x = set(bulan)
set_list = list(x)
print("Konversi Set menjadi List")
print("Sebelum Konversi: ", x)
print("Sesudah Konversi : ", set_list)
print()

a = tuple(bulan)
tuple_Set = set(a)
print("Konversi Tuple menjadi Set")
print("Sebelum Konversi: ", a)
print("Sesudah Konversi: ", tuple_Set)
print()

b = set(bulan)
set_tuple = tuple(b)
print("Kpnversi Tuple menjadi Set")
print("Sebelum Konversi: ", b)
print("Sesudah Konversi: ", set_tuple)