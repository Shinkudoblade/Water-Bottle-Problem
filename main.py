'''
    Nama    : Andry Syva Maldini
    NPM     : 21083010085
    Kelas   : Elemen Kecerdasan Buatan A

    Permainan Teka-teki Botol
    Seberapa baik Anda mendapatkan jumlah yang tepat dalam botol?
    masukkan aturan yang telah disediakan untuk mengisi, mentransfer, atau mengosongkannya.

    Anda memiliki 2 botol dengan ukuran berbeda & persediaan air tak terbatas. 
    Bisakah Anda mengukur jumlah air yang dibutuhkan dengan tepat?

    level 1 : 2 dari 5 dan 3
    level 2 : 2 dari 5 dan 4
    level 3 : 1 dari 5 dan 3
    level 4 : 4 dari 5 dan 3
    level 5 : 2 dari 4 dan 3
    level 6 : 6 dari 7 dan 5
    level 7 : 4 dari 8 dan 5
    level 8 : 6 dari 9 dan 4
    level 9 : 9 dari 10 dan 7
    level 10 : 8 dari 11 dan 6
    level 11 : 5 dari 11 dan 7
    level 12 : 8 dari 11 dan 9
    level 13 : 6 dari 12 dan 11
    level 14 : 8 dari 13 dan 11
    level 15 : 2 dari 7 dan 3

    SELAMAT BERMAIN
'''

print('\033[1m', '\33[34m')
print('='*80)
print("|" + "\t" * 4 + "TEKA-TEKI BOTOL" + "\t" * 4 + "       |")
print('='*80)
b1 = int(input('\nMasukkan Kapasitas Botol 1 : '))
b2 = int(input('Masukkan Kapasitas Botol 2 : '))
target = int(input('Masukkan target yang ingin dicapai(botol 1, botol 2): '))

print('')
print(" PERATURAN ".center(80,'='))
print(f'''Aturan 1: Isi botol 1
Aturan 2: Isi botol 2
Aturan 3: Pindahkan semua air dari botol 1 ke botol 2
Aturan 4: Pindahkan semua air dari botol 2 ke botol 1
Aturan 5: Pindahkan sedikit air dari botol 1 ke botol 2 sampai botol 2 penuh
Aturan 6: Pindahkan sedikit air dari botol 2 ke botol 1 sampai botol 1 penuh
Aturan 7: Kosongkan botol 1
Aturan 8: kosongkan botol 2''')
print(80*'=')

def start(ano, x, y):
    if ano == 1:
        if x<b1:
            return b1,y
        else:
            print(f'\33[31mAturan {ano} tidak bisa diterapkan')
            return x,y

    elif ano == 2:
        if y<b2:
            return x, b2
        else:
            print(f'\33[31mAturan {ano} tidak bisa diterapkan')
            return x,y
    
    elif ano == 3:
        if x>0 and x+y<=b2:
            return 0, x+y
        else:
            print(f'\33[31mAturan {ano} tidak bisa diterapkan')
            return x,y

    elif ano == 4:
        if y>0 and x+y<=b1:
            return x+y, 0
        else:
            print(f'\33[31mAturan {ano} tidak bisa diterapkan')
            return x,y
    
    elif ano == 5:
        if x>0 and x+y>=b2:
            return x-(b2+y), b2
        else:
            print(f'\33[31mAturan {ano} tidak bisa diterapkan')
            return x,y
    
    elif ano == 6:
        if x>0 and x+y>=b2:
            return b1, y-(b1-x)
        else:
            print(f'\33[31mAturan {ano} tidak bisa diterapkan')
            return x,y

    elif ano == 7:
        if x>0:
            return 0, y
        else:
            print(f'\33[31mAturan {ano} tidak bisa diterapkan')
            return x,y

    elif ano == 8:
        if y>0:
            return x,0
        else:
            print(f'\33[31mAturan {ano} tidak bisa diterapkan')
            return x,y
    # Jika input yang dimasukkan tidak valid maka program berhenti
    else:
        print("\33[31mPilihan tidak valid!")

# Inisialisasi kapasitas botol 0
x = y = 0
while True:
    if(x==target)or(y==target):
        print("YEAY KETEMU..., SELAMAT!")
        print(" TAMAT ".center(30, '='))
        break
    else :
        print('\33[32m')
        ano = int(input("Masukkan Aturan no : "))
        x, y = start(ano, x, y)
        print(" STATUS ".center(30, '='))
        print(f"Kondisi saat ini: \nbotol 1 = {x} \nbotol 2 = {y}\n")
        print(f"({x}, {y})")