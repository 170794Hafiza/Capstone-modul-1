data_siswa = [
    {'Nama' : 'Ari Darmansyah',
     'Umur' : 7,
     'Jenis Kelamin' : 'Pria',
     'Alamat' : 'Balailalang',
     'Nomor Induk Siswa' : 413,
     'Jenis Beasiswa' : 'PIP'},
    {'Nama' : 'Bayu Langit',
     'Umur' : 8,
     'Jenis Kelamin' : 'Pria',
     'Alamat' : 'Singkarak',
     'Nomor Induk Siswa' : 412,
     'Jenis Beasiswa' : 'Yayasan'},
     {'Nama' : 'Cantik Hesada',
     'Umur' : 9,
     'Jenis Kelamin' : 'Wanita',
     'Alamat' : 'Sumani',
     'Nomor Induk Siswa' : 414,
     'Jenis Beasiswa' : 'Silang'},
    {'Nama' : 'Danil Ghafar',
     'Umur' : 8,
     'Jenis Kelamin' : 'Pria',
     'Alamat' : 'Balaigadang',
     'Nomor Induk Siswa' : 415,
     'Jenis Beasiswa' : 'PIP'},
     {'Nama' : 'Endang Trisa',
     'Umur' : 7,
     'Jenis Kelamin' : 'Wanita',
     'Alamat' : 'Pinang',
     'Nomor Induk Siswa' : 416,
     'Jenis Beasiswa' : 'Yayasan'}         
]

#__________MENU UTAMA__________
#1 Report Data Siswa
#2 Menambahkan Data Siswa
#3 Mengubah Data Siswa
#4 Menghapus Data Siswa
#5 Pengelompokan Penerima Beasiswa
#6 Exit



#0 Menu Utama  
def welcome():
    print("__________MENU UTAMA__________\n1 Report Data Siswa \n2 Menambahkan Data Siswa\n3 Mengubah Data Siswa\n4 Menghapus Data Siswa \n5 Pengelompokan Penerima Beasiswa \n6 Exit")
    pilihan = input("Silahkan pilh menu utama diatas [1-6] : ")
    if pilihan == '1':
        readData()
    elif pilihan == '2':
        tambahData()
    elif pilihan == '3':
        ubahData()
    elif pilihan == '4':
        hapusData()
    elif pilihan == '5':
        sortingBeasiswa()
    elif pilihan == '6':
        exit()

#1 Report Data Siswa
def readData():
    print("\n\t\t\t\t^^^^^^^Report Data Siswa^^^^^^^^\n")
    print('No\t Nama\t\tUmur\tJenis Kelamin\tAlamat\tNomor Induk Siswa')
    for i in range(len(data_siswa)):
        print("{}\t{}\t\t{}\t{}\t{}\t {}".format(i+1, data_siswa[i]['Nama'], data_siswa[i]['Umur'], data_siswa[i]['Jenis Kelamin'], data_siswa[i]['Alamat'], data_siswa[i]['Nomor Induk Siswa'], data_siswa[i]['Jenis Beasiswa']))
    welcome()

#2 Menambahkan Data Siswa
def tambahData():
    print('\nSilahkan Bapak/Ibu isi data siswa yang ingin ditambahkan ke database : ')
    nama_i = input('Nama : ')
    umur_i = input('Umur : ')
    jenis_kelamin_i = input('Jenis Kelamin :')
    alamat_i = input('Alamat : ')
    nis_i = int(input('Nomor Induk Siswa : '))
    beasiswa_i = input('Beasiswa : ')

    data_siswa.append({
        'Nama' : nama_i,
        'Umur' :    umur_i,
        'Jenis Kelamin' :   jenis_kelamin_i,
        'Alamat' :  alamat_i,
        'Nomor Induk Siswa' :   nis_i,
        'Jenis Beasiswa' :  beasiswa_i
    })

    
    print('No\t Nama\tUmur\tJenis Kelamin\tAlamat\tNomor Induk Siswa')
    for i in range(len(data_siswa)):
        print("{} {}\t {}\t{}\t{}\t {}".format(i+1, data_siswa[i]['Nama'], data_siswa[i]['Umur'], data_siswa[i]['Jenis Kelamin'], data_siswa[i]['Alamat'], data_siswa[i]['Nomor Induk Siswa'], data_siswa[i]['Jenis Beasiswa']))
    print('\t\t\t***Data sudah berhasil ditambahkan ke database***\n')
    welcome()
    return

#3 Mengubah Data Siswa
def ubahData():
    print('No\t Nama\t\t\tNomor Induk Siswa')
    for i in range(len(data_siswa)):
        print("{}\t {}\t\t {}".format(i+1, data_siswa[i]['Nama'], data_siswa[i]['Nomor Induk Siswa']))
    ubah = int(input('Silahkan masukkan NIS data siswa yang ingin Anda ubah : '))
    for i in range(len(data_siswa)):
        if ubah == data_siswa[i]['Nomor Induk Siswa']:
            ubah_kolom = input('Pilih kolom yang ingin diubah (Nama, NIS, Jenis Kelamin, Alamat, Umur): ').lower()
            if ubah_kolom== data_siswa[i]['Nomor Induk Siswa']:
                ubah_kolom = ubah_kolom.upper()
            else:
                ubah_kolom = ubah_kolom.capitalize()
                ubah_isi = input(f'Masukkan {ubah_kolom} baru : ').capitalize()
            print('**Data Sudah Diubah**\n')

    welcome()

#4 Menghapus Data Siswa
def hapusData():
    print('No\t Nama\t\tNomor Induk Siswa')
    for i in range(len(data_siswa)):
        print("{}\t {}".format(data_siswa[i]['Nama'], data_siswa[i]['Nomor Induk Siswa']))
    hapus = int(input('Silahkan masukkan NIS data siswa yang ingin Anda hapus : '))
    for i in range(len(data_siswa)):
        if hapus == data_siswa[i]['Nomor Induk Siswa']:
            ab = input('Anda yakin menghapus data ini? (Jawab Y/T)').capitalize()
            if ab == 'Y':
                del data_siswa[i]
            else:
                welcome()
    print('**Data Sudah Dihapus**')
    print(data_siswa)
    welcome()
  

#5 Pengelompokan Penerima Beasiswa
def sortingBeasiswa():
    urut = input('Silahkan masukkan Jenis Beasiswa yang ingin Anda ketahui penerimanya (PIP/Yayasan/Silang): ')
    print('No|Nama|Nomor Induk Siswa|Jenis Beasiswa')
    for i in range(len(data_siswa)):
        if urut == data_siswa[i]['Jenis Beasiswa']:
            print("{}\t\t {}\t\t {} \t {}".format(i+1, data_siswa[i]['Nama'], data_siswa[i]['Nomor Induk Siswa'], data_siswa[i]['Jenis Beasiswa']))
    welcome()
    
#6 Exit
def exit():
    print('\n\n*******Thank You for your time*******\n\n')



print('\t\t\t\t==============DATA SISWA SDN 19 SOLOK==============\n')
welcome()



