# input
student_score = 80

# Process: Your Solution Code Here

# Output "Nilai A"

print('Berikut Adalah Program Konversi Nilai')
print('-------------------------------------')

nama_siswa = input('nama siswa : ')
nilai = input('nilai : ')
nilai = eval(nilai)

if nilai >= 80:
    na = 'A'
elif nilai >= 65:
    na = 'B+'
elif nilai >= 50:
    na = 'B'
elif nilai >= 35:
    na = 'C'
else:
    na = 'D'

print(f'Konversi nilai siswa : {na}')