import matplotlib.pyplot as plt

class Kambing:
    def __init__(self, nama, berat_awal, tinggi_awal, panjang_awal):
        self.nama = nama
        self.berat = [berat_awal]  # Perkembangan berat disimpan dalam list
        self.tinggi = tinggi_awal
        self.panjang = panjang_awal

    def tambah_perkembangan(self, berat_tambahan, tinggi_tambahan, panjang_tambahan):
        self.berat.append(self.berat[-1] + berat_tambahan)  # Menambahkan perkembangan berat ke dalam list
        self.tinggi += tinggi_tambahan
        self.panjang += panjang_tambahan

    def jual_atau_mati(self):
        print(f"Kambing {self.nama} terjual atau mati dengan berat {self.berat[-1]}, tinggi {self.tinggi}, panjang {self.panjang}")


class PemilikKambing:
    def __init__(self, nama_pemilik):
        self.nama_pemilik = nama_pemilik
        self.daftar_kambing = []

    def tambah_kambing(self, kambing):
        self.daftar_kambing.append(kambing)

    def cek_semua_kambing(self):
        for kambing in self.daftar_kambing:
            print(f"Nama: {kambing.nama}, Berat: {kambing.berat[-1]}, Tinggi: {kambing.tinggi}, Panjang: {kambing.panjang}")

    def jual_kambing(self, nama_kambing):
        for kambing in self.daftar_kambing:
            if kambing.nama == nama_kambing:
                kambing.jual_atau_mati()
                self.daftar_kambing.remove(kambing)
                print(f"Kambing {nama_kambing} dihapus dari data pemilik.")
                break
        else:
            print(f"Kambing dengan nama {nama_kambing} tidak ditemukan.")


def visualisasi_perkembangan_berat(kambing):
    plt.plot(range(len(kambing.berat)), kambing.berat, marker='o')
    plt.title(f"Perkembangan Berat Kambing {kambing.nama}")
    plt.xlabel("Bulan")
    plt.ylabel("Berat (kg)")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    pemilik_slamet = PemilikKambing("Bapak Haji Slamet")

    kambing1 = Kambing("Kambing A", 10, 50, 80)
    pemilik_slamet.tambah_kambing(kambing1)

    kambing2 = Kambing("Kambing B", 8, 45, 75)
    pemilik_slamet.tambah_kambing(kambing2)

    kambing1.tambah_perkembangan(5, 2, 3)
    kambing1.tambah_perkembangan(7, 3, 5)

    kambing2.tambah_perkembangan(4, 1, 2)
    kambing2.tambah_perkembangan(6, 2, 4)

    pemilik_slamet.cek_semua_kambing()

    pemilik_slamet.jual_kambing("Kambing A")

    pemilik_slamet.cek_semua_kambing()

    visualisasi_perkembangan_berat(kambing1)
