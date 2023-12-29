# Class Induk: Pertanian
class Pertanian:
    def __init__(self, nama_petani, luas_lahan):
        self._nama_petani = nama_petani
        self._luas_lahan = luas_lahan

    def tanam_tanaman(self, tanaman):
        print(f"\n{self._nama_petani} menanam {tanaman.nama} di lahan seluas {self._luas_lahan} hektar.")

    def perawatan_lahan(self):
        print(f"\n{self._nama_petani} melakukan perawatan lahan.")


# Class Anak 1: Tanaman
class Tanaman(Pertanian):
    def __init__(self, nama, jenis, usia=0):  # Overloading
        super().__init__("Petani 1", 10)
        self.nama = nama
        self.jenis = jenis
        self._usia = usia

    def tanam_tanaman(self, alat_kebun=None):  # Overloading
        if alat_kebun:
            print(f"\nTanaman {self.nama} ditanam dengan bantuan {alat_kebun.nama}.")
        else:
            print(f"\nTanaman {self.nama} ditanam.")

    def perawatan_lahan(self, frekuensi=1):  # Overloading
        print(f"\nMelakukan perawatan lahan untuk tanaman {self.nama} dengan frekuensi {frekuensi} kali dalam seminggu.")

    def info_tanaman(self):
        print(f"\n{self.nama} ({self.jenis}) dengan usia {self._usia} tahun.")


# Class Anak 2: LokasiTanaman
class LokasiTanaman(Tanaman):
    def __init__(self, nama, jenis, usia=0, warna_bunga="", lokasi=""):  # Overloading
        super().__init__(nama, jenis, usia)
        self._warna_bunga = warna_bunga
        self.lokasi = lokasi

    def info_lokasi_tanaman(self):
        print(f"\nTanaman {self.nama} tumbuh di lokasi {self.lokasi}.")

    def info_tanaman(self):  # Overriding
        print(f"\n{self.nama} ({self.jenis}) dengan warna bunga {self._warna_bunga}, usia {self._usia} tahun.")


# Class AlatKebun
class AlatKebun:
    def __init__(self, nama, fungsi, harga):
        self.nama = nama
        self.fungsi = fungsi
        self.harga = harga

    def gunakan_alat(self):
        print(f"\nAlat kebun {self.nama} digunakan.")


# Class Pupuk
class Pupuk:
    def __init__(self, jenis, komposisi):
        self.jenis = jenis
        self._komposisi = komposisi

    def tambahkan_pupuk(self):
        print(f"\nMenambahkan pupuk jenis {self.jenis} dengan komposisi {self._komposisi}.")


# Contoh penggunaan program dengan operator aritmatika, logika, perulangan, dan percabangan
tanaman_padi = Tanaman("Padi", "Padi Sawah", 30)
alat_cangkul = AlatKebun("Cangkul", "Menggali tanah", 50)
pupuk_organik = Pupuk("Organik", "Pupuk kandang dan kompos")

tanaman_padi.tanam_tanaman(alat_cangkul)
tanaman_padi.perawatan_lahan(2)

tanaman_hijau = LokasiTanaman("Hijau", "Pohon", 5, "Hijau", "Taman Depan")
tanaman_hijau.info_tanaman()
tanaman_hijau.info_lokasi_tanaman()

pupuk_organik.tambahkan_pupuk()

# Operator aritmatika
luas_lahan_tambahan = 5
tanaman_padi._luas_lahan += luas_lahan_tambahan
print(f"\nLuas lahan setelah tambahan: {tanaman_padi._luas_lahan} hektar")

# Operator logika, percabangan, dan perulangan
if tanaman_padi._luas_lahan > 15 and tanaman_hijau.jenis == "Pohon":
    print("\nPersyaratan pertumbuhan tanaman terpenuhi.")
    for i in range(3):
        print(f"Perawatan ke-{i+1}")
        tanaman_padi.perawatan_lahan(i+1)
else:
    print("\nTanaman tidak dapat ditanam atau perawatan tidak diperlukan.")
