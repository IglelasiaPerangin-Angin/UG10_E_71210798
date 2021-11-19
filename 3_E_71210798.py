#judul
nama_pertama, nama_kedua, nama_ketiga = list(input("Masukkan daftar siswa :") .split(","))

#soal
hba = nama_pertama.title()
hbb = nama_kedua.title()
hbc = nama_ketiga.title()
print("\nDaftar Siswa : ['"+hba+"', '"+hbb+"', '"+hbc+"']")

y = input("\nMasukkan siswa yang ingin ditambahkan : ")
yz = y.title()
xyz = yz.upper()
if (yz == hba) :
    print("\nSiswa atas nama",xyz,"sudah berada dalam daftar siswa1")
elif (yz == hbb) :
    print("\nSiswa atas nama",xyz,"sudah berada dalam daftar siswa2")
elif (yz == hbc) :
    print("\nSiswa atas nama",xyz,"sudah berada dalam daftar siswa3")
else :
    print("\nHasil penambahan pada daftar siswa : ['"+hba+"', '"+hbb+"', '"+hbc+"', '"+xyz+"']")
