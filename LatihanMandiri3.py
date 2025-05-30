file1 = input("Masukkan nama file 1 : ")
try:
    a = open(file1, 'r')
except: 
    print("File yang anda masukkan tidak ada: ", a)
    exit()

file2 = input("Masukkan nama file 2 : ")
try:
    b = open(file2, 'r')
except: 
    print("File yang anda masukkan tidak ada: ", b)
    exit()

a = a.read()
b = b.read()

x = a.lower()
y = b.lower()

ubh_split = x.split()
ubh_split1 = y.split()

ubh_set1 = set(ubh_split)
ubh_set2 = set(ubh_split1)

print()
kata_sama = ubh_set1 & ubh_set2
print(kata_sama)