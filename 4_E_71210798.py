#judul
print ('Masukkan bilangan yang diinginkan!')

#soal
a=int(input('Masukkan bilangan 1 = '))
b=int(input('Masukkan bilangan 2 = '))
c=int(input('Masukkan bilangan 3 = '))

if a>b and a>c:
    if b>c:
       print(c, b, a)
    else:
       print(b, c, a)
elif b>a and b>c:
    if a>c:
        print(c, a, b)
    else:
        print(a, c, b)
else:
    if a>b:
        print(b, a, c)
    else:
        -print(a, b, c)

