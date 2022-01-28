keluar = 0
list_kontak_nama = ["Jhon", "Bambang"]
list_kontak_nomor = ["081372617278", "081354267378"]
jumlah = len(list_kontak_nama)
while keluar == 0:
    
    #print(list_kontak_nama)
    print("Selamat Datang!")
    print("---Menu---")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Keluar")

    
    pilihan = int(input("Pilih menu : "))
    if pilihan == 1:
        print("\nDaftar kontak : ")
        for x in range(len(list_kontak_nama)):
            print("Nama : {}".format(list_kontak_nama[x]))
            print("Nomor : {}".format(list_kontak_nomor[x]))
            print(" ")

    elif pilihan == 2:
        print(" ")
        nama_tambah = str(input("Nama : "))
        nomor_tambah = (input("Nomor : "))
        list_kontak_nama.append(nama_tambah)
        list_kontak_nomor.append(nomor_tambah)
        print("Kontak berhasil ditambahkan")
        print(" ")
      
    elif pilihan == 3:
        print("\nProgram selesai, sampai jumpa!")
        keluar = 1
    else:
        print("\nMenu tidak tersedia \n")