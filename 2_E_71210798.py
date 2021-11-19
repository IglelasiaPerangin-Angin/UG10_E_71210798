#mengambil input
yuzhong = float(input("Masukkan suhu tubuh Anda : "))

#mengambil output
if yuzhong >= 50:
    print("Anda bukan manusia :)")
elif yuzhong <= 32:
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat!")
elif 50 >= yuzhong > 37.5:
    print("Anda demam! Jangan bepergian ke tempat fasilitas umum.")
elif 37.5 >= yuzhong > 32:
    print("Suhu Anda normal!")
