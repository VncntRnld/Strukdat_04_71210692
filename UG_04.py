import json

with open("mahasiswa.json","r") as f:
    data = json.load(f)

    temp = dict()
    jmlh = int(input("Masukkan jumlah mahasiswa baru : "))

    for i in range(jmlh):
        nama = input("Masukkan nama anda : ")
        hobi = []

        x_hobi = int(input("Masukkan  jumlah hobi : "))
        for j in range(x_hobi):
            hobi_i = input("Masukkan hobi ke-{} : " .format(j+1))
            hobi.append(hobi_i)
        prestasi = input("masukkan prestasi anda : ")

        print("=== Data berhasil ditambahkan ===")
        print()

        temp[nama] = [{"Biodata" : {"Hobi" : hobi, "Prestasi" : prestasi }}]

    data.update(temp)

with open("mahasiswa.json", "w") as f:
    json.dump(data, f)
